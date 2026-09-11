> This is the four-source baseline coverage record. The current nine-source library adds five verified books and excludes one mismatched submission; see [expansion-coverage.md](expansion-coverage.md) and the updated [source manifest](source-manifest.json). Earlier corpus line locators below refer only to the original extraction batch.

# Source, coverage, and fidelity ledger

Build date: 2026-09-11. Purpose: rebuild the existing legal-reasoning-advisor as an expert for live diagnosis and development of legal arguments. Architecture: existing root `SKILL.md`, task-loaded modules, optional digest procedure, and discovery alias retained. This is an existing-repository rebuild under books-to-skill-refs' adaptation rule, not a new library forced into its default naming convention.

## What was wrong and what changed

| Earlier commitment | Problem | Rebuilt behavior |
|---|---|---|
| A category is legitimate only to the extent courts have placed comparable facts in it | Excludes statutory definitions, instrument effects, recognized principles, and legitimate novel applications; overstates Coke | Identify the source that gives the category legal work and justify its scope |
| Common law forbids deduction from definitions | Confuses unsupported premises with the form of inference; Coke expressly defines and divides concepts and uses syllogisms | Test premises and inference separately; retain source-sensitive deduction |
| “We are bound” is always a rebuttable presumption for the deciding court | Conflates a philosophical explanation of precedent with jurisdiction-specific power to depart | Verify hierarchy and available exceptions; separate disagreement from competence |
| Formal justice is the strongest basis for precedent | Flattens Duxbury's critique of equality as a sufficient account of stare decisis | Preserve competing justifications, their limitations, and combined force |
| Most arguments have exactly one true joint | Fails with alternative sufficient grounds and independent claims | Map cumulative and independent routes; no forced single weakness |
| Narrowest defensible holding is the default | Can erase a supported principle and mishandle fragmented opinions | Select the best-supported scope; preserve alternatives and apply local aggregation rules |
| Hohfeld as a short relation-word glossary | Misses operative/evidential facts, timing, power without privilege, and conditioned legal change | Relational and temporal analysis with explicit source examples |
| Coke sources treated as complete collections | Supplied PDFs contain one volume each | Identify actual volumes and separate source/editor voices |

## Input identity and extraction

`source-manifest.json` records input filenames, byte sizes, SHA-256 hashes, extraction metadata, actual coverage, and canonical destination modules. It deliberately omits private absolute input paths and download-account information from the source transcriptions.

The first-party `scripts/extract.py` extracted all four supplied paths together in text mode with installation disabled, producing a fenced corpus and metadata in temporary storage. System Python lacked a PDF backend; the bundled Python runtime had PyMuPDF, pdfplumber, and pypdf, so no dependency installation was needed. All four extractions succeeded. Estimated corpus tokens use `bookrefs.tokens` script density, not actual model billing.

| File identity | Extractor result | Verified structure used for planning | Study/text budget |
|---|---|---|---|
| Hohfeld Markdown | ~30,522 source tokens; “68 pages” is a prose estimate | Three main analytical sections; journal pp. 16–59 | 5,898 tokens |
| Institutes PDF | 790 pages; ~666,590 source tokens; automated count 26 | Volume II, Book III, thirteen chapters | 8,708 tokens |
| Selected Writings PDF | 620 pages; ~370,429 source tokens; automated count 30 | Volume One; selections from thirteen Parts of the Reports | 8,708 tokens |
| Duxbury Markdown | ~141,587 source tokens; “315 pages” is a prose estimate; automated count 2 | Five main chapters, subdivisions recovered from contents/headings | 6,654 tokens |

The automatic chapter counts were not used as a substitute for reading the contents. Text mode was suitable for these legal prose sources. The Hohfeld and Duxbury transcriptions have pipe-table artifacts from earlier conversion, not computational tables requiring a different PDF parser. Flattening a damaged line would not restore missing characters, so uncertainty remains visible.

### Reading and source quality

The combined corpus was never loaded as one whole reading. Source spans from metadata were copied into separate temporary text files, then queried by headings, names, and locators. Body passages were read selectively. Some terminal outputs were truncated; no claim of complete line-by-line reading or exact cumulative input-token accounting is made. Several probes were too broad, a workflow limitation to improve in later builds. The source budgets were used as output ceilings/targets, not as mandatory lengths.

- **Hohfeld:** right-edge loss, false table cells, duplicated navigation, and embedded unavailable asset links. Surviving section headings and examples support the distillation, but the transcription is not suitable for reliable verbatim quotation. Removed the old runtime's signature quotations rather than claiming textual restoration. The complete later treatment of in rem/in personam relations is not in the supplied installment.
- **Institutes:** the title page identifies the eighteenth edition, Volume II, 1823; front matter identifies the 1985 Legal Classics Library reprint. Main text begins at Littleton §241, Coke folio 163a. English, Law French, Latin, marginal citations, tables, and editorial notes can interleave in OCR. Chapter openings, operative distinctions, and selected passages were inspected; extensive later editorial essays were not exhaustively distilled.
- **Selected Writings:** the title page identifies Volume One. The collection-wide contents advertise later volumes, but the supplied body is the Reports selection. Marginal handwriting and marks contaminate some OCR. The source's “Ed.” descriptions are not Coke's words. Key conclusions were taken from the report body as well as the introductory locator.
- **Duxbury:** the five chapters are recoverable and readable despite merged words, table artifacts, and footnote interruptions. Attributions to Raz, Hart, Goodhart, Montrose, Kronman, and others are kept as views examined by Duxbury. Current status of the illustrative cases was not researched for this historical-method rebuild.

### Visual checks

PDF render inspection confirmed Institutes PDF p. 11 (edition and Volume II), Selected Writings PDF p. 5 (Volume One), and Selected Writings PDF p. 366 / printed p. 274 (Bonham's whole-text reasoning and separate clauses). Institutes PDF p. 323 / folio 254a was additionally rendered and checked for the corrected case reference. The supplied images were not altered or published. Visual checks are samples, not page-by-page OCR certification.

## Coverage inventory

Each row records a retained group, its source locus, and limits. Chapter headings in the runtime references provide finer navigation. “Compressed” means selected methodological content survives; it does not mean the entire underlying doctrine was reconstructed.

### Hohfeld → `references/hohfeld-toolkit.md`

| Source unit | Retained concepts | Treatment |
|---|---|---|
| Opening, pp. 16–20 | Trust debate; Coke's use; insufficiency of a simple rem/personam division | Compressed; theories in quoted opening footnotes not adopted as Hohfeld's final conclusions |
| Legal/non-legal, pp. 20–25 | Physical and mental facts; property thing/interest; transfer; license; capacity; possession/title ambiguity | Retained; no blanket abolition of doctrinal classifications |
| Operative/evidential, pp. 25–28 | Constitutive/dispositive facts; affirmative/negative conditions; later evidence of January document; pleaded generic facts | Retained; no inferred modern allocation of proof burdens |
| Fundamental relations, pp. 28–32 | Exact opposites and correlatives; strict right/claim and duty | Retained with counterpart, content, time, and opposite-content qualification |
| Privileges, pp. 32–44 | Duty to act compatible with privilege to act; salad variations; Quinn; Mogul; license as operative facts | Retained; case doctrines not represented as current |
| Powers, pp. 44–55 | Volitional legal change; transfer; abandonment; agency; escrow; right of entry; offer/option; innkeeper; juror liability; beneficial liability | Retained; smaller supporting authorities compressed into mechanism |
| Immunities, pp. 55–58 | Disability; actor/asset specificity; sheriff; tax exemption interpretation and alienability | Retained with contrary transfer treatment; no universal alienability rule |
| Conclusion, pp. 58–59 | Lowest common denominators; cross-field comparison; reserved later analysis | Retained; later terminology and later installment explicitly excluded |

### Institutes → `references/reference-coke-institutes.md`

| Book III chapter | Locators sampled | Retained / excluded |
|---|---|---|
| 1. Parceners | §§241, 276 | Descent and shared title; agreement versus writ; detailed inheritance calculations excluded |
| 2. Parceners by custom | §§265, 275 | Custom as premise; pleading; hotchpot limited to its legal category; genealogy tables excluded |
| 3. Joint tenants | §277 and discussion of joint conveyances | Joint acquisition; share versus whole; textual correction; exhaustive joint-tenancy incidents excluded |
| 4. Tenants in common | §292 | Several titles with common occupation; transition after conveyance; long editorial histories compressed |
| 5. Estates upon condition | §325, 201a–b; §366 passage | In deed/in law; precedent/subsequent; affirmative/negative; logical form; automatic/entry-based effects; jury/estoppel excursus not developed into a separate doctrine |
| 6. Descents tolling entries | §385, 237a–b | Entry versus action; operation of law; detailed limitations and exceptions excluded |
| 7. Continual claim | §§414, 420–421, 250b and 254a | Preservation and purpose-specific entry; authority check and citation correction; historical periods not offered as current law |
| 8. Releases | §§444–445, 465; 264b, 272b | Right/action distinction; effect depends on existing relations; uses and Chancery; full uses/conveyancing doctrine excluded |
| 9. Confirmation | §515, 295b | Existing estate; void/voidable; bounded maxim; full formalities excluded |
| 10. Attornment | §551, 309a | Third-party act, timing, relational rationale; later statutory changes not represented as Coke's law |
| 11. Discontinuance | §592; closing qualification before §659 | Remedy versus entitlement; qualification by estate; later editor's expanded history separated |
| 12. Remitter | §659, 347b | Older remediable right and later estate; operation of law; no-folly qualification |
| 13. Warranty | §697, 365a | Lineal/collateral/disseisin; real covenant; remedy/bar; communis opinio; full feudal warranty system excluded |

Volume I, Books I–II, and their unsupplied explanatory context are not claimed as directly distilled. The edition's closing contents describe more than the supplied main text; that does not cure the missing volume.

### Selected Writings → `references/common-law-method.md`

| Retained unit | Printed locator | Treatment |
|---|---|---|
| Part One preface | 4–6 | Reporting failure modes and connected study practice |
| Shelley's Case | 6–38 | Words of limitation/purchase and chronology only; complete rule reconstruction excluded |
| Heydon's Case | 78–83 | Four considerations, enacted remedy, copyhold classification |
| Slade's Case | 116–124, especially 120 | Established course, contrary instances, unexamined precedents, law/reason where precedents unavailable |
| Semayne's Case | 135–141 | General maxim and process-specific limits |
| Rooke's Case | 141–144 | Discretion under law; identity of repairers; statutory distribution and reasons |
| Calvin's Case | 166–232, especially 224–225 | Natural-law premises and syllogisms as a counterexample to an anti-deduction reading; other nationality and historical arguments excluded |
| Dr. Bonham's Case | 264–283, especially 274–276 | Distinct clauses, whole text, imprisonment power, interested adjudicator, contested broader reading |
| Sutton's Hospital | 347–378 | Legal corporation versus natural body only; complete incorporation doctrine excluded |
| Isle of Ely | 378–384, especially 381 | Repair/new river, textual authority, separate harm inquiry |
| Prohibitions del Roy | 478–481 | Conference account, artificial reason, designated court, remedy, source status |
| Proclamations | 486–489 | Existing offence versus new offence; bounded prerogative; deliberation and examination of prior instances |

All other reports and prefaces are omitted from detailed distillation. The contents inventory, not a read of their full bodies, informed that selection. In particular, Parts Two, Six, Nine, Eleven, and Thirteen do not receive a substantive chapter reconstruction. Their individual bankruptcy, tithes, nuisance, criminal, municipal-office, monopoly, jurisdictional, and other rules are not available as silently distilled doctrine. The rationale is focus on transferable legal reasoning within a whole-module loading budget, not a claim that the omitted material lacks importance. The volume's fifty-eight selected cases therefore must not be described as fifty-eight completed case digests.

### Duxbury → `references/precedent-method.md`

| Chapter | Retained named concepts and arguments | Compression / exclusions |
|---|---|---|
| 1, pp. 1–30 | Precedent/analogy/rule/custom; past decision as reason; unintended/undiscovered precedent; forward reach; positivism; no comprehensive theory | Case illustrations and extended polemics compressed |
| 2, pp. 31–57 | Formation before stare decisis; reports/abridgements; classical positivism; artificial reason/coherence; questions shaped by precedent | Historical details and secondary bibliographies compressed; no one-date origin claim |
| 3, pp. 58–110 | Ratio; dicta; multiple/no ratio; Wambaugh inversion; Goodhart material facts; Montrose and notation burden; generality; information management; shortcuts/piggybacking; correlated repetition; Hart/Raz pre-emption/exclusion | Detailed symbolic notation excluded as not useful to the intended expert; not all discussed theories adopted |
| 4, pp. 111–149 | Within/between-case distinguishing; Black/White/Grey; added condition; overruling; self-binding; Practice Statement; constitutional propriety; self-reference | Stone and respondents compressed into the institutional/logical distinction; no current hierarchy claim |
| 5, pp. 150–183 | Consequentialist reasons; economy, planning, stability, reliance; pastness; formal justice; relevance; permissible/mandatory difference; consistency/error; path-dependence; plural support | Full philosophical disputes and case lists compressed; equality not declared a sufficient or universally strongest justification |

## Cross-source synthesis and tensions

1. **Operative transition:** Hohfeld's relations plus Coke's conditions and remedies support an actor/event/power/exercise/result analysis. This is the advisor's synthesis, not a named historical joint framework.
2. **Source-sensitive classification:** Coke's instruments and whole-statute reasoning qualify the old “only cases can earn categories” stance; Duxbury helps distinguish authority from factual analogy.
3. **Institutional competence:** Coke's jurisdiction and prerogative examples and Duxbury's departure questions both require specifying the actor. Hohfeld clarifies the asserted legal change. No uniform current constitutional doctrine is inferred.
4. **Records and revisability:** Coke's wish to stabilize accurate reports is compatible with Duxbury's qualified account of later interpretation, but not identical to a modern binding-ratio doctrine.
5. **Coke and Hohfeld on uses:** Coke's historically forum-specific remedial vocabulary is preserved beside Hohfeld's criticism of coarse conceptions; neither is silently made to speak the other's terminology.
6. **Reason:** Coke's natural-law and deductive arguments remain visible alongside artificial reason. Duxbury's critical accounts of theorists remain attributed rather than collapsed into agreement.
7. **Taxonomy and digest:** Both are repository procedures. Contemporary evidence, remedies, statutory interpretation, and opinion-aggregation rules are verification needs, not additional books silently included in the source count.

## Limits of acceptance

Budgets and scans do not establish jurisprudential fidelity. The editorial cases in `evaluation.md` test whether the written commitments address the observed failure modes, with actual sample responses recorded. They are not independent model experiments. The generic validator recognizes only the new `reference-*` file as a book; its seven naming/packaging warnings are expected under this pre-existing architecture. `validate.py` supplements it by checking all four canonical source modules without renaming or duplicating them. Both results are preserved, not silently filtered.
