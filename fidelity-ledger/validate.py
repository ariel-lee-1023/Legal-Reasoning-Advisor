#!/usr/bin/env python3
"""Validate the established advisor layout using the books-to-skill-refs checks.

The generic validator intentionally remains unmodified. Its filename-based source
count is supplemented by the four source modules recorded in the manifest.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--metatool', required=True, type=Path)
    parser.add_argument('--write', action='store_true', help='Save reports in fidelity-ledger/')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    ledger = root / 'fidelity-ledger'
    metatool = args.metatool.resolve()
    sys.path.insert(0, str(metatool / 'tools'))
    sys.path.insert(0, str(metatool))
    import validate_library as v
    from bookrefs.tokens import estimate_tokens

    report = v.Report()
    manifest = json.loads((ledger / 'source-manifest.json').read_text())
    references = [root / s['runtime_reference'] for s in manifest['sources']]
    expected_sources = {
        'hohfeld-toolkit.md', 'reference-coke-institutes.md',
        'common-law-method.md', 'precedent-method.md',
    }
    expected_modules = expected_sources | {'move-taxonomy.md', 'precedent-extraction.md'}
    if manifest['source_count'] != 4 or len(references) != 4:
        report.error('Exactly four supplied sources must be recorded')
    if {p.name for p in references} != expected_sources:
        report.error('Manifest must map to the four canonical source modules')
    actual_modules = {p.name for p in (root / 'references').iterdir() if p.is_file()}
    if actual_modules != expected_modules:
        report.error('Runtime module set changed; review architecture and manifest')

    master = (root / 'SKILL.md').read_text()
    v.check_master_frontmatter(master, report, 'legal-reasoning-advisor')
    all_modules = [root / 'references' / n for n in sorted(expected_modules)]
    v.check_router(master, root, all_modules, report)
    v.check_master_budget(master, 4, 0, report)
    if re.search(r'\]\([^)]*fidelity-ledger', master):
        report.error('Maintainer records must not be domain-answer loading links')
    for source, path in zip(manifest['sources'], references):
        if not path.is_file():
            report.error(f'Missing source module: {path.name}')
            continue
        v.check_reference(path, 'study', report)
        if not re.fullmatch(r'[0-9a-f]{64}', source['sha256']):
            report.error(f'Invalid source hash for {path.name}')
        if report.facts['references'][path.name]['sections'] != source['verified_structure_units']:
            report.error(f'Section count differs from manifest for {path.name}')
    for name in sorted(expected_modules - expected_sources):
        body = (root / 'references' / name).read_text()
        count = estimate_tokens(body)
        report.facts.setdefault('synthesis_modules', {})[name] = {'tokens': count, 'cap': 6000}
        if count > 6000:
            report.error(f'{name} exceeds the local 6,000-token synthesis cap')
        if 'synthesis' not in body.lower():
            report.error(f'{name} must identify its repository-synthesis status')

    alias = root / '.agents/skills/legal-reasoning-advisor'
    if not alias.is_symlink() or alias.readlink().as_posix() != '../..' or alias.resolve() != root:
        report.error('Discovery alias must be legal-reasoning-advisor -> ../.. resolving to root')

    checked_links = 0
    for path in [root / n for n in ('SKILL.md', 'README.md', 'AGENTS.md', 'CHANGELOG.md', 'NOTICE.md')] + all_modules:
        body = re.sub(r'```.*?```', '', path.read_text(), flags=re.S)
        for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', body):
            link = link.strip('<>').split('#', 1)[0]
            if not link or re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', link):
                continue
            target = path.parent / link
            checked_links += 1
            if not target.exists():
                report.error(f'Broken relative link in {path.name}: {link}')
    report.facts['relative_links_checked'] = checked_links

    digest = (root / 'references/precedent-extraction.md').read_text()
    examples = re.findall(r'```json\s*\n(.*?)```', digest, re.S)
    if len(examples) != 1:
        report.error('Expected one optional JSON record example')
    else:
        data = json.loads(examples[0])
        if data.get('schema_version') != '2.0' or data['current_force']['status'] != 'not_checked':
            report.error('JSON version or default authority status is inconsistent')

    runtime = [root / 'SKILL.md'] + all_modules
    for path in runtime:
        body = path.read_text()
        if any(term in body for term in ('asset:sha256:', 'This content downloaded from', '/Users/Extracurriculars/', '/tmp/legal-advisor-')):
            report.error(f'Source artifact or private build path leaked into {path.name}')
    for path in root.iterdir():
        if path.suffix.lower() in {'.pdf', '.epub'} or path.name == 'full_text.txt':
            report.error(f'Raw source artifact at repository root: {path.name}')

    generic = v.validate(root, layout='published-repo')
    generic_data = {'errors': generic.errors, 'warnings': generic.warnings, 'facts': generic.facts}
    scans = {}
    for label, target in [('core', root / 'SKILL.md'), ('references', root / 'references')]:
        result = subprocess.run(
            [sys.executable, str(metatool / 'tools/scan_generated_skill.py'), str(target), '--json', '--strict'],
            check=False, capture_output=True, text=True,
        )
        try:
            findings = json.loads(result.stdout)
        except json.JSONDecodeError:
            findings = {'unparsed_output': result.stdout, 'stderr': result.stderr}
            report.error(f'{label} instruction scan did not return JSON')
        scans[label] = {'exit_code': result.returncode, 'findings': findings}
        if result.returncode:
            report.error(f'{label} instruction scan returned {result.returncode}')

    result = {
        'status': 'passed' if not (report.errors or generic.errors) else 'failed',
        'layout': 'existing advisor; published-repo plus manifest-driven source checks',
        'source_count': 4,
        'runtime_module_count': 6,
        'errors': report.errors + generic.errors,
        'warnings': report.warnings,
        'generic_profile': generic_data,
        'compatibility_note': 'The generic profile recognizes only reference-* names as books. Its existing-name warnings and book count are retained; the four-source measurements below are authoritative for this rebuild.',
        'facts': report.facts,
        'instruction_scans': scans,
        'runtime_sha256': {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in runtime},
        'limits': 'Structural, routing, budget, and advisory scan checks; not semantic proof or an independent behavioral benchmark.',
    }
    if args.write:
        (ledger / 'generic-validation.json').write_text(json.dumps(generic_data, indent=2) + '\n')
        for label, data in scans.items():
            (ledger / f'scan-{label}.json').write_text(json.dumps(data, indent=2) + '\n')
        (ledger / 'validation.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
    return 0 if result['status'] == 'passed' else 1


if __name__ == '__main__':
    raise SystemExit(main())
