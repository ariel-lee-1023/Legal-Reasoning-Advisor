#!/usr/bin/env python3
"""Export blinded runtime snapshots and two-round transfer probes; does not call a model."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import secrets
import subprocess

BASELINE = 'bc9fbef4b8da46cf6548e15d94349d7da5e4c315'


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git(repo: Path, *args: str) -> bytes:
    return subprocess.run(['git', '-C', str(repo), *args], check=True,
                          capture_output=True).stdout


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    root = Path(__file__).resolve().parent.parent
    parser.add_argument('--repository', type=Path, default=root)
    parser.add_argument('--candidate', type=Path, default=root)
    parser.add_argument('--baseline-ref', default=BASELINE)
    parser.add_argument('--output', type=Path, required=True,
                        help='New directory; never overwrites an existing export')
    args = parser.parse_args()
    if args.output.exists():
        parser.error('Output must not already exist')
    baseline_commit = git(args.repository, 'rev-parse', '--verify',
                          args.baseline_ref + '^{commit}').decode().strip()
    names = git(args.repository, 'ls-tree', '-r', '--name-only',
                baseline_commit, '--', 'SKILL.md', 'references/').decode().splitlines()
    baseline = {name: git(args.repository, 'show', f'{baseline_commit}:{name}')
                for name in names}
    candidate = {p.relative_to(args.candidate).as_posix(): p.read_bytes()
                 for p in [args.candidate / 'SKILL.md',
                           *sorted((args.candidate / 'references').glob('*.md'))]}
    suite_bytes = (root / 'fidelity-ledger/transfer-probes.json').read_bytes()
    suite = json.loads(suite_bytes)
    labels = ['A', 'B']
    secrets.SystemRandom().shuffle(labels)
    snapshots = {labels[0]: baseline, labels[1]: candidate}
    args.output.mkdir(parents=True)
    for label, files in snapshots.items():
        for name, data in files.items():
            target = args.output / 'conditions' / label / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
    (args.output / 'evaluator-only').mkdir()
    manifest = {
        'kind': 'evaluation export; no model calls performed',
        'baseline_commit': baseline_commit,
        'mapping': {labels[0]: 'baseline', labels[1]: 'candidate'},
        'suite_sha256': sha(suite_bytes),
        'runtime_sha256': {label: {n: sha(b) for n, b in files.items()}
                           for label, files in snapshots.items()},
        'isolation': 'Labels conceal versions from graders; filesystem access must be isolated by the runner.',
    }
    (args.output / 'evaluator-only/manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    (args.output / 'evaluator-only/rubric.json').write_bytes(suite_bytes)
    for case in suite['cases']:
        target = args.output / 'prompts' / case['id']
        target.mkdir(parents=True)
        (target / 'round-1.txt').write_text(
            'Use the assigned condition’s SKILL.md and load relevant references as needed. '
            'Do not inspect another condition, evaluator-only files, or the later update. '
            'Use only the fictional rules and facts supplied. Answer the question directly. '
            'Separately record the reference filenames loaded.\n\n' + case['prompt'] + '\n')
        (target / 'round-2.txt').write_text(
            'Revise your earlier answer using this update. State what changes and why, '
            'including what remains supported or unresolved.\n\n' + case['update'] + '\n')
    print(json.dumps({'output': str(args.output), 'cases': len(suite['cases']),
                      'rounds_per_case': 2, 'conditions': 2, 'model_calls': 0}, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
