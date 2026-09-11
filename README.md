# Legal Reasoning Advisor

An expert Agent Skill for developing and testing legal arguments. It connects evidence and operative facts to legal relations, authoritative sources, institutional powers, and remedies, then identifies what supports the proposed result and what would change the assessment.

The central task is **live reasoning inside an argument**: improving a brief, assessing a judgment, resolving a statutory puzzle, explaining a relation, or building the strongest counterargument. A full case digest is an optional tool.

## What the advisor does

- Separates allegations, evidence, operative events, classifications, precedent, and policy where their different burdens matter.
- Distinguishes a permission from a claim against interference, a duty from a legal disability, and a triggering event from exercise of a power.
- Tests statutory definitions and instrument effects alongside cases and legally relevant comparisons.
- Assesses a precedent's proposition, scope, hierarchy, reasons, and available routes of departure without treating it as either mechanical or optional.
- Preserves alternative sufficient grounds and issue-specific opinion alignments instead of forcing every argument to have one weak premise or every case one ratio.
- Delivers a conclusion, a supported objection, and the next useful revision or verification step.

The four-move taxonomy—factual, interpretive/classificatory, precedent application, and policy/normative—is this repository's synthesis. It is a diagnostic aid, not a claimed framework from Coke, Hohfeld, or Duxbury.

## Examples

> “A promised not to transfer the asset, then transferred it. Does the breach mean the transfer was ineffective?”

The advisor distinguishes a duty not to transfer from a power to transfer and identifies the legal premise needed to invalidate the transaction.

> “The statute defines this category expressly, but no case has applied it to this new device. Is the answer necessarily open?”

It tests the definition and its scope; lack of a factual twin does not automatically prevent an established rule from applying.

> “This judgment gives two independent grounds for dismissal. Which would my appeal have to answer?”

It preserves both routes, distinguishes removal of a dismissal ground from success on the merits, and identifies the relevant procedural limits.

> “Compare the majority and concurrences, extract the holding, and tell me what remains unresolved.”

It maps propositions and agreement by issue, then uses the applicable aggregation rule if verified. It does not select the shortest opinion and label it controlling.

Other useful requests include improving an argument paragraph, comparing candidate holdings, diagnosing a shift in the meaning of “right,” and explaining how a historical case reasons without presenting it as current law.

## Sources and their actual coverage

| Source | Supplied material | Contribution |
|---|---|---|
| Wesley Newcomb Hohfeld, *Some Fundamental Legal Conceptions as Applied in Judicial Reasoning*, 23 Yale Law Journal 16–59 (1913) | Markdown transcription of the 1913 article, with conversion damage | Legal/non-legal and operative/evidential distinctions; eight jural positions; options, transfers, powers, immunities |
| Sir Edward Coke, *The First Part of the Institutes of the Laws of England; or, A Commentary upon Littleton*, eighteenth edition (1823), Legal Classics Library reprint (1985) | **Volume II**, beginning with Littleton's Book III; 790 PDF pages | Thirteen-chapter methodological coverage: title, conditions, release, confirmation, attornment, discontinuance, remitter, warranty |
| Sir Edward Coke, *The Selected Writings and Speeches of Sir Edward Coke*, ed. Steve Sheppard (Liberty Fund, 2003) | **Volume One**; 620 PDF pages, selected Reports and prefaces | Selected passages on reporting, interpretation, discretion, legal competence, and the limits of authority |
| Neil Duxbury, *The Nature and Authority of Precedent* (Cambridge University Press, 2008) | Markdown transcription; all five main chapters represented | Formation and authority of precedent, ratio tests and their limits, distinctions, overruling, self-binding, consequential and deontological arguments |

The filenames overstate the Coke volumes available. The Institutes file is not both volumes; the Selected Writings file's collection-wide contents list does not mean the later volumes are included. The rebuild records those limits and separates Littleton, Coke, later editorial notes, and Sheppard's introductions.

Source modules synthesize the material in original prose, preserving technical names and verified source locators. The Coke material is selected for reasoning method rather than exhaustive historical doctrine. Hohfeld's later installment is not silently imported. Coverage, exclusions, hashes, extraction quality, and evaluations are recorded in [fidelity-ledger](fidelity-ledger/source-and-coverage-ledger.md).

## Architecture and progressive loading

```text
legal-reasoning-advisor/
├── SKILL.md                         # always-loaded reasoning core and task triggers
├── references/
│   ├── move-taxonomy.md             # diagnostic synthesis
│   ├── common-law-method.md         # Coke: Selected Writings, Volume One
│   ├── reference-coke-institutes.md  # Coke on Littleton, Volume II
│   ├── hohfeld-toolkit.md            # Hohfeld: 1913 article
│   ├── precedent-method.md           # Duxbury: five chapters
│   └── precedent-extraction.md       # optional digest procedure
├── .agents/skills/legal-reasoning-advisor -> ../..
├── AGENTS.md
├── fidelity-ledger/                 # maintainer records, not domain-answer modules
├── README.md
├── CHANGELOG.md
├── NOTICE.md
├── LICENSE
└── .gitignore
```

There is one canonical root skill and one canonical set of references. The discovery symlink resolves to the repository root. The books-to-skill-refs rebuild follows this repository's existing architecture and preserves all five original module paths; the additional Institutes module gives the fourth supplied source its own reference. It deliberately does not rename the existing modules into the metatool's default generated naming scheme.

A consultation loads the core, then only the module or small combination relevant to the problem. Maintainer records are not included in the task-triggered loading table. Routine advice does not require a full case note, relation table, or bibliography.

## Installation

Open the repository as an agent project; [AGENTS.md](AGENTS.md) directs domain questions to the root skill. For hosts using project skill discovery, the `.agents/skills/` alias exposes the same canonical files. Hosts must preserve directory symlinks or be directed to the root skill explicitly.

For a personal skill installation, clone the **whole repository**, including `references/`, into the host's supported skill directory. Examples:

```bash
git clone https://github.com/ariel-lee-1023/legal-reasoning-advisor.git \
  ~/.agents/skills/legal-reasoning-advisor
```

```bash
git clone https://github.com/ariel-lee-1023/legal-reasoning-advisor.git \
  ~/.claude/skills/legal-reasoning-advisor
```

Choose a supported location for the host in use. Do not copy `SKILL.md` alone or create a second divergent runtime copy inside this repository. The advisor answers in the user's language even though the source instructions are English.

## Scope and verification

This is a reasoning aid grounded mainly in common-law materials, not a current law database or a substitute for jurisdiction-specific professional judgment. Present statutes, hierarchy, case status, procedural rules, remedies, and binding force require appropriate primary-source verification when they affect an actual conclusion. A closed-record analysis should identify its limits instead of silently supplying contemporary law from memory.

Historical examples are attributed as historical examples. Constructed scenarios explicitly state their assumed legal premises. A legal concept can reveal a missing premise without establishing the opposite legal result. Non-common-law use requires attention to the local institution and source hierarchy; the corpus does not itself establish them.

The optional JSON record is now version `2.0`; see [Precedent Extraction](references/precedent-extraction.md). It is an illustrative record structure, not a machine-enforced JSON Schema or a claim of backward-compatible fields.

## Maintenance and validation

The rebuild uses books-to-skill-refs extraction, targeted reading, source-level budgets, source-boundary discipline, coverage accounting, and instruction scanning. The ledger distinguishes structural checks from editorial assessment; it does not claim an independent model benchmark.

From a checkout of Books-to-Skill-Refs, run its published-repository validator against this repository. Existing module names generate documented compatibility warnings. The supplementary checker validates **all four source modules**, the two synthesis modules' routing, relative links, discovery alias, source manifest, and JSON example:

```bash
python3 fidelity-ledger/validate.py --metatool /path/to/Books-to-Skill-Refs
```

See [validation.json](fidelity-ledger/validation.json), [evaluation.md](fidelity-ledger/evaluation.md), and the separate runtime scan reports for the recorded run. Preserve source authorship, scope, existing paths, and the distinction between runtime content and maintainer records when extending the advisor. Add a worked regression case whenever changing a substantive reasoning commitment.

## License

MIT © 2026 Ariel Lee applies to the repository's original instructions, synthetic reference prose, and supporting code. It does not relicense source publications or editorial apparatus. See [LICENSE](LICENSE) and [NOTICE.md](NOTICE.md).
