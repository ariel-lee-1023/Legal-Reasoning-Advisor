# Five-source expansion: provenance, coverage, and limits

Build date: 2026-09-11. Baseline: `bc9fbef4b8da46cf6548e15d94349d7da5e4c315`. Method: books-to-skill-refs, existing-repository adaptation. Six submitted Markdown files were extracted in one fenced batch; **five were verified and distilled**. With the four baseline sources, the runtime now has nine source modules and two repository-synthesis modules. The four original source modules and optional digest remain unchanged.

## Source identity is a gate

The submission named `Modeling-Legal-Arguments-Reasoning-with-Cases-and-Hypotheticals-Artificial-Intel.md` is not Ashley's book. Its title, author text, contents, and body identify *Probabilistic Similarity Networks* and David E. Heckerman, with additional anomalous front matter. Searches found Pathfinder and medical-diagnostic material, no Ashley attribution and no trade-secret content. The neighboring PDF named for Kevin D. Ashley has the same mismatch (265 PDF pages; title and contents inspected). Neither was distilled or used to justify a HYPO claim.

An additional recovery search checked the [MIT Press book record](https://mitpress.mit.edu/9780262011143/modeling-legal-arguments/) and the [UMass research group bibliography](https://people.cs.umass.edu/~cbr/publications.html) on 2026-09-11. They confirm the intended Ashley/HYPO work and distinguish the book from its dissertation antecedent. This search did not recover a verified complete copy for distillation; descriptions and secondary discussions were not substituted for the book.

The manifest records the rejected Markdown's hash and extraction span separately, with no runtime reference. A correct copy remains necessary for the requested Ashley-specific work. Prakken's discussion of HYPO is secondary discussion and is identified as such. Generic counterexample and comparison operations already supported by MacCormick, Walton, and Duxbury are retained without branding them HYPO.

*Interpreting Statutes: A Comparative Study* was suggested as a future extension but not supplied. MacCormick's own interpretive treatment is distilled; the edited comparative volume is not counted as read. The separately hosted appendices advertised in *Analysis of Evidence* are likewise not claimed as supplied or distilled.

## Extraction and reading

`scripts/extract.py` accepted all six Markdown inputs. Extraction success did not imply source identity or content fidelity. Converter page counts are character-based estimates, not bibliographic pagination. The source manifest preserves file sizes, SHA-256 hashes, estimates, batch identifiers, and exact corpus line bounds. Do not interpret the original and expansion batches' line numbers as positions in the same corpus.

Automatic chapter detection returned 2, 0, 1, 3, 13, and 7 for the six submissions. TOCs, chapter-opening headings, printed page headers, and structure probes were used to distinguish true chapters from running heads and malformed tables. The five accepted books have 13, 5, 12, 12, and 11 top-level chapters/essays respectively. Toulmin's introduction and concluding discussion do not become extra essays; Prakken's bibliography and appendix do not become chapters.

Reading was sliced, not a full read of 1.35 million estimated tokens. Targeted slices preserved the corpus and removed only conversion separators in displayed copies. `reading-record.json` records the principal slice ranges and actual shown character counts. Preliminary identity/TOC searches and several ad hoc checks are explicitly outside that detailed log; it is not a complete token-billing record. Some long slices were capped before the end, and early tool outputs were truncated. The record does not treat unshown text as read. High-value definitions and examples were subsequently checked in narrower slices.

MacCormick and Toulmin have line wrapping and page-layout artifacts. Walton has substantial OCR spelling, table, and symbol damage; Prakken has particularly severe table/formula corruption. *Analysis of Evidence* has broken chart layouts and some missing visual content. The new references synthesize prose-confirmed distinctions; they do not reproduce damaged formal expressions, reconstruct missing figures as originals, or claim theorem-level fidelity.

## Per-source coverage and exclusions

The table maps chapter structure to retained operations. It is a coverage inventory, not a claim that every page or every example was read in depth. The reference token targets are ceilings for useful distillation, not minimum lengths; compression below target is intentional where additional material would repeat the method or exceed the available transcription fidelity.

### MacCormick — thirteen chapters

| Chapters | Retained | Deliberately bounded or excluded |
|---|---|---|
| 1–2: institutions, lawmaker, arguability and Rule of Law | Operative facts/normative consequences; institution and competence; qualified certainty; rhetorical/proceduralist reconciliation | Full institutional ontology and the entire debate with every interlocutor |
| 3–4: syllogism and deductivism | Inference versus justification; proof, interpretation, classification, relevancy; Dignity Funerals and Daniels route distinctions | Full technical treatment of normative predicates and every philosophical objection |
| 5: universals and particulars | Universalization versus induction/generalization; qualified reasons; material variation | Solomon as a current custody or psychological test |
| 6: consequences | Juridical implications versus causal predictions; consistency/coherence/consequences; ruling-level counterexample | A numerical optimization formula; current necessity doctrine |
| 7: interpretation | Linguistic; six systemic types; teleological-evaluative; intention distinctions; competing readings | Universal priority across jurisdictions; claim to have distilled the separate comparative volume |
| 8: precedent | Ruling, issue, reasons; faithful reconstruction versus improvement; Duxbury handoff | Replacement of institutional-force analysis with philosophical justification |
| 9: reasonableness | Topic, legally relevant factors, judgment, institutional role | Complete doctrine for each historical legal standard |
| 10: coherence and analogy | Consistency/coherence; principle-backed similarity; car-color counterexample | A unique-answer guarantee or automatic analogy metric |
| 11: narratives | Narrative/normative coherence; evidential and procedural limits; washhouse example | Complete historical case reanalysis |
| 12–13: defeasibility and error | Pragmatic defeat, qualified universals, finality/correctness, correction | Conflation with Prakken's technical semantics; automatic power to disregard precedent |

Principal source locations: ch. 3 pp. 32–48; ch. 4 pp. 49–77; ch. 5 pp. 88–100; ch. 6 pp. 104–120; ch. 7 pp. 124–142; ch. 8 pp. 147–161; ch. 9 pp. 173–188; ch. 10 pp. 190–212; ch. 11 pp. 221–235; ch. 12 pp. 237–253; ch. 13 pp. 276–280. The source's future-facing EU constitutional discussion is not republished as a current fact.

### Toulmin — five essays

| Essay | Retained | Deliberately bounded or excluded |
|---|---|---|
| I: fields and modals | Phases; force/criteria; field-invariance/dependence | Full survey of modal usages and epistemological positions |
| II: probability | Proper assertion versus eventual truth; time-indexed grounds; gardening example | A legal proof threshold or numerical probability model |
| III: layout | D/C/W/B/Q/R; functional rather than sentence labels; warrant-using/establishing; analytic/substantial; distinct classification axes | Treating the six-part diagram as the whole book; historical nationality or demographic examples as current facts |
| IV: working and idealised logic | Applicability of formal models; critique of analytic paradigm | Adoption of every criticism of formal logic as the advisor's position |
| V: epistemological theory | Temporal evaluation and induction; substantial arguments need appropriate standards | Detailed transcendentalist/phenomenalist/intuition controversies; a universal epistemological resolution |

The conclusion is pp. 233–238; references begin 239. The reference preserves the five-essay structure rather than silently making the conclusion part of Essay V. Worked source loci: pp. 53–55, 93–98, 114–130; temporal assessment pp. 217 onward. Reconstructed-premise labels and the portal case are repository design applications.

### Walton, Reed, and Macagno — twelve chapters

Chapters 1–7 supply scheme/critical-question discipline, linked/convergent argument structure, analogy/classification, knowledge and practical schemes, commitments/character, causation, enthymeme attribution, and attack/refutation. Chapters 8 and 10 retain classification limits and historical context, not a full history of topics. Chapter 9 supplies the selected operational cards. Chapters 11–12 retain distinctions needed for formalization and dialogue; software encodings and integrations are not reproduced or implemented.

The compendium's sixty primary entries receive the following explicit disposition. Grouped exclusions below are intentional; the runtime is not advertised as an exhaustive sixty-scheme library. The authors themselves note that their scheme list and subspecies classification are not final.

| Entries | Disposition |
|---|---|
| 1 position to know; 2 expert opinion; 3 witness testimony | Retained in detail, with matching question families |
| 4 popular opinion; 5 popular practice | General distinction retained; all popularity subtypes omitted as lower priority for this advisor |
| 6 example, illustration, model and anti-model | Comparison context retained; dedicated subtype procedures omitted; single example not treated as deductive proof |
| 7 analogy; 8 practical reasoning from analogy | Retained with disanalogy and counterexample tests |
| 9 composition; 10 division | Directional distinction retained; damaged/transposed parentheticals not reproduced |
| 11 oppositions; 12 rhetorical oppositions; 13 alternatives | Distinction of opposition types and alternative routes retained; complete scheme syntax omitted |
| 14 verbal classification; 15 definition; 16 vagueness; 17 arbitrariness | Retained, including facts/definition split and context-appropriate precision |
| 18 act/person interaction; 19 values; 20 sacrifice; 21 group/members | Values covered within practical reasoning; standalone variants omitted to avoid broadening into a general persuasion library |
| 22 practical reasoning | Retained, including goal, means, alternatives, feasibility, values, side effects; not all subtype formulas |
| 23 two-person practical reasoning; 24 waste; 25 sunk costs | Dedicated bargaining and investment variants omitted; general alternatives/goals procedure remains |
| 26 ignorance; 27 epistemic ignorance | Retained with search completeness and burden questions |
| 28 cause/effect; 29 correlation/cause; 30 sign; 31 abduction; 32 evidence/hypothesis | Retained core forms and tests; character-based abduction subtypes not adopted as factual shortcuts |
| 33 consequences | Retained with empirical and evaluative premises separated |
| 34 pragmatic alternatives; 35 threat; 36 fear; 37 danger; 38 help; 39 distress | Family context retained; dedicated emotional/coercive appeal procedures omitted as not central to evidential legal assessment |
| 40 commitment; 41 ethotic; 42 generic ad hominem; 43 pragmatic inconsistency; 44 inconsistent commitment; 45 circumstantial ad hominem; 46 bias; 47 bias ad hominem | Commitment/source-relevance distinctions retained; detailed procedures focus on 40 and 44–47; no exhaustive ad hominem ontology |
| 48 gradualism; 49 slippery slope; 50 precedent slope; 51 sorites slope; 52 verbal slope; 53 full slope | Slope mechanism/stopping tests retained for 49–53 as a family; separate gradualism and subtype formalizations omitted |
| 54 constitutive-rule claims; 55 rules; 56 exceptional case; 57 precedent; 58 excuse | Retained; 57 explicitly recognized as exception argument from a legitimate counterinstance, not simply analogy transfer |
| 59 perception; 60 memory | Reliability/undercutting discipline retained; no substitute for a cognitive psychology of witness accuracy |

Source-example locus: corporate-income-tax reconstruction, ch. 6 pp. 199–201. Critical-question roles and burdens: ch. 11 pp. 373–375. Primary scheme cards: ch. 9 pp. 309–346. Legal remedy/authority checks in the cards are advisor applications, not an additional authorial scheme.

### Anderson, Schum, and Twining — twelve chapters

| Chapters | Retained | Deliberately bounded or excluded |
|---|---|---|
| 1–2: inference and investigation | Standpoint; E*/E; probanda; relevance/credibility/force; direct, indirect, opinion and tangible evidence | All exercises and exhaustive evidence taxonomy |
| 3: proof | PA/OD/OR/OE/PC; conjunction, convergence, corroboration, catenate inference; author disagreement about generalizations | Treating analytical independence as statistical independence |
| 4–6: methods | Seven-step chart protocol; key-list, sector chart, opposing theories, iterative revision; outline/chronology/narrative | Original visual palette and every diagram; diagram completion as proof |
| 7: Bywaters and Thompson | Statement/content/inference distinctions; letters, temporal context, prejudice | Full exhibit republication or independent historical verdict |
| 8: evaluation | Stage-specific questions and standards; legal/proof/advice differences | Universal threshold or present procedural doctrine |
| 9: probability and weight | Bayesian likelihood/posterior; Shafer support; Baconian coverage; Wigmore/fuzzy weight | Full calculation systems; online appendices; numerical confidence without inputs |
| 10: stories and generalizations | Types of generalization; story audit, rival explanation, speculation/prejudice | Treating narrative coherence or cultural consensus as sufficient proof |
| 11: law of evidence | Purpose-specific relevance and admissibility analysis | Current evidence-law manual across jurisdictions |
| 12: trial standpoint | Investigation, opponent's theory, presentation constraints | Solutions to every case exercise and complete advocacy training |

Worked source loci: Able, ch. 5 pp. 125–133; E*/E and credibility ch. 2 pp. 60–69; proof relationships ch. 3 pp. 96–109; competing weight accounts ch. 9 pp. 250–261; story protocol ch. 10 pp. 280–282. The altered-record case and compact textual chart are constructed adaptations.

### Prakken — eleven chapters

| Chapters | Retained | Deliberately bounded or excluded |
|---|---|---|
| 1–2: role of logic | Formalization limits; naive deductivism; premise discovery versus inference; analogy as heuristic | Full philosophy of AI and logic |
| 3–4: need and alternatives | Exceptions, inconsistency, nonmonotonicity, absence/negation; survey of formalism families | Formula transcription, implementation, and all consequence-property proofs |
| 5: explicit exceptions | Rebutting/undercutting; soft/hard; exceptions to exceptions; contraposition caution | Full encodings in default logic, circumscription, Poole, and logic programming |
| 6: argument assessment | Subarguments, local/global defeat, dialogue branches, non-repetition, justified/overruled/defensible, argument/conclusion status | OCR-damaged worked racial stereotypes; exact theorem-certified dialogue solver |
| 7: inconsistent information | Skeptical/credulous distinction, floating conclusions, extension-based alternative, accrual limits | Silent adoption of an alternative semantics; automatic argument-count aggregation |
| 8: priority relations | Priorities as argued conclusions; collision rules; legal basis for specificity; conflict/revision | Universal hierarchy of legal maxims |
| 9: comparison | Formal systems have different attacks and consequences | Full reconstruction of every compared theory |
| 10: applications | Toulmin mapping limits; logical/dialectical/procedural/strategic layers; time-indexed reassessment | Existing software implementations; Ashley monograph via secondary HYPO mention |
| 11: conclusion | Defined scope and unfinished modeling tasks | Claim of exhaustive natural-language formal verification |

Principal loci: §5.1 pp. 102–104; §6.5 pp. 163–170; §7.5.3 pp. 196–197; §7.5.4 pp. 198 onward; ch. 8 pp. 203 onward; §10.5 pp. 270–274. Termination example and update protocol are advisor adaptations. “Overruled argument” is not judicial overruling; technical “justified” is not an implemented criminal proof standard.

## Cross-source design and retained disagreement

MacCormick organizes the distinction between inferential structure and justified legal premises. Toulmin identifies the hidden bridge and its support. Anderson–Schum–Twining provide the evidence method. Walton–Reed–Macagno specialize objections. Prakken makes updates and argument interaction explicit. Hohfeld and Duxbury remain specialist foundations; Coke retains focused historical-method coverage.

This integration is repository design, including the user's proposed division of labor. It does not erase disagreements: Toulmin's criticisms of formal logic are not Prakken's position; analogy has different theoretical roles across authors; MacCormick's pragmatic defeasibility is not identical to a technical defeat relation; probabilistic traditions remain distinct; and multiple consequence semantics are not interchangeable.

The integrated late-notice demonstration came from the user's proposal. It is deliberately labeled a training example and excluded from any claim of unfamiliar-test performance. See [expansion-evaluation.md](expansion-evaluation.md) for test design and the limits of the available evidence.
