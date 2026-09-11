# Logical Tools for Modelling Legal Argument — Henry Prakken

**Source:** Henry Prakken, *Logical Tools for Modelling Legal Argument: A Study of Defeasible Reasoning in Law* (Kluwer Academic Publishers, 1997), supplied Markdown transcription. **Format**: md | **Pages**: main chapters pp. 1–282, followed by notation/glossary, references, and index | **Sections**: 11 | **Depth**: study | **Type**: technical

## Mental Model (read first)

A supported argument can lose its justification when new information enables a successful counterargument. Its conclusion may nevertheless survive through another argument. Represent the premises, rules, subarguments, conflicts, and priorities separately; reassess the resulting argument system whenever an input changes.

Prakken supplies formal theories of nonmonotonic reasoning and inconsistency handling, not a rule that the newest or most detailed assertion wins. The book distinguishes local defeat from global justification, and the status of arguments from the status of their conclusions. Its logical, dialectical, procedural, and strategic layers must also be kept separate.

The operational procedure below is an **informal advisor adaptation**, not an implementation of the book's logic or a later framework such as ASPIC+. The supplied OCR has severely damaged formulas and tables. The reference preserves prose-confirmed definitions and examples but does not claim verified theorem transcription, executable completeness, or a mathematical proof certificate for natural-language advice.

## Frameworks & Structure

### 1. Introduction — pp. 1–16

The book investigates what logic can contribute to AI and legal reasoning. A logical account is not a complete model of a lawyer. Formal structure, interpretation, knowledge acquisition, procedure, and strategy raise different problems. Declare which one an analysis addresses.

**Use:** if a user requests a formal model, state the language, premises, rule types, priorities, attack definitions, and consequence notion before claiming a result. If the task is ordinary argument criticism, use a compact dependency record and give reasons rather than decorative symbols.

### 2. The Role of Logic in Legal Reasoning — pp. 17–32

Prakken rejects the ideas that formalizing means completely defining a legal concept, that formalization leaves no room for interpretation, or that logic is confined to deduction. He also rejects naive deductivism: a valid inference does not establish the truth or acceptability of its premises.

**Rule-based and case-based reasoning:** a logical representation can clarify the relation between a proposed premise and conclusion while leaving premise discovery and justification to other methods. Prakken treats analogy as potentially a heuristic for suggesting premises, rather than necessarily a distinctive inference rule. This differs from treatments in Walton and MacCormick; the advisor preserves the difference rather than attributing one unified theory to them.

### 3. The Need for New Logical Tools — pp. 33–66

Explicit exceptions, open texture, defeasible concepts, vagueness, and inconsistent information motivate nonstandard techniques. Distinguish a known exception from uncertainty over classification and from a direct conflict between sources. They need different representations and further inquiry.

**Monotonicity:** in a monotonic consequence relation, adding premises does not remove previous consequences. Nonmonotonic reasoning permits such withdrawal. This does not make the original inference careless; its support was relative to the information and defaults then available.

**Inconsistency:** two conflicting assertions need not destroy every inference in a dispute. Isolate their provenance and the arguments depending on them. Do not resolve the conflict by deleting an inconvenient source without reason, and do not infer arbitrary unrelated conclusions from the contradiction.

### 4. Logics for Nonmonotonic Reasoning — pp. 67–100

The survey includes consistency-based approaches, autoepistemic logic, minimization, conditional approaches, and inconsistency handling; it also examines consequence properties, preferential entailment, truth maintenance, and objections about logic and tractability.

**Practical distinctions retained:**

- Lack of support for P is different from support for not-P.
- A default permitting a conclusion in the absence of an established exception differs from a strict conditional with every exception explicitly negated in its antecedent.
- Different consequence notions can license different conclusions from the same apparent defaults.
- Maintaining conclusions after updates requires preserving the dependencies that justified them.

Do not choose a formalism by vocabulary alone. The survey's implementations and proofs are outside this reference's operational coverage; this is a source-method module, not a general theorem prover.

### 5. Representing Explicit Exceptions — pp. 101–140

Prakken compares default logic, circumscription, Poole's framework, and logic-programming approaches, including negation as failure and classical negation. How a rule and exception are represented affects directionality, contraposition, and reinstatement. An encoding is a substantive modeling choice.

**Rebutting defeater:** supports an opposing consequence. **Undercutting defeater:** blocks the application of an inference without necessarily supporting its opposite. A broken timestamp mechanism can undercut an inference from a timestamp to an event time; it does not establish a contrary event time.

**Soft and hard exceptions:** in the book's terminology, an exception may itself be subject to exceptions or may be treated as not so defeasible. This is separate from the rebutting/undercutting distinction. Do not label an exception “hard” merely because its rhetorical presentation sounds decisive.

**Exception to an exception:** determine whether it removes the defeating reason and reinstates the general inference, or supplies only a new, narrower consequence. In particular, an exception to a rebutting rule need not restore every part of the original rule's conclusion. State which legal consequences actually return.

**Failure condition:** applying contraposition to a defeasible rule without justification. “Normally A supports B” and “not-B” do not by themselves establish “not-A.” Similarly, absence of recorded exception evidence is not a factual finding that the exception did not occur; the legal or modeled burden must justify proceeding on a default.

### 6. Preferring the Most Specific Argument — pp. 141–178

Prakken first explores specificity, identifies problems in earlier formulations, and defines argument construction, comparison, defeat, and a dialogue-game account of justification. An argument cannot be justified while an essential subargument fails the required status.

**Local versus global assessment, §6.5.1:** A's defeating B does not establish A's global justification. C may defeat A and thereby reinstate B. Inspect the relevant system of arguments and their subarguments, not only the last exchange.

**Dialogue game, §§6.5.2–6.5.3:** the proponent of a justified argument must answer every available attacking branch with the required strictly defeating response; the opponent can prevent justification with a defeating argument. The proponent's non-repetition condition prevents winning by circular repetition. A victory on one selected branch is insufficient to establish victory across the tree.

**Statuses in the book:**

| Object | Status | Meaning and limit |
|---|---|---|
| Argument | Justified | Supported by a winning proponent dialogue tree under the defined system and premises |
| Argument | Overruled | Attacked by a justified argument under the book's definition |
| Argument | Defensible | Neither justified nor overruled; this is a technical residual class, not ordinary praise |
| Conclusion | Justified under §6.5.9 | At least one justified argument concludes it |
| Conclusion | Defensible under §6.5.9 | No justified argument concludes it, but a defensible one does |
| Conclusion | Overruled under §6.5.9 | Neither of those higher statuses applies, and an overruled argument concludes it |

A proposition with no argument is not automatically in the overruled class. “Overruled” here is also not judicial overruling of a precedent. Prakken's descriptive use of “beyond reasonable doubt” when motivating argument status does not by itself implement the criminal standard of proof.

**Equal opposition example, §6.5.8:** equally unprioritized defeasible arguments for P and not-P need not make either justified. Both can remain defensible. “Not justified” does not entail “the opposite is justified.” Preserve uncertainty instead of picking a side by tone or arrival order.

### 7. Reasoning with Inconsistent Information — pp. 179–202

The treatment extends priority-based conflict handling and examines skeptical/credulous reasoning, floating conclusions, and accrual. The choice of consequence notion changes what can be said to follow.

**Floating conclusions, §7.5.3, pp. 196–197:** suppose an unresolved conflict supports P on one side and not-P on the other. Each side, through a different defeasible route, also supports Q. Under the earlier argument-centered notion, Q need not have a justified argument. Under an extension-based notion, Q can occur in all admissible alternatives through different arguments. Prakken treats these as different notions of support, not a question settled by declaring one meaning universally correct.

**Advisor consequence:** distinguish a genuinely independent surviving argument for Q from a conclusion shared only across alternative resolutions. In the second situation, state the alternative branches and the assumption that they exhaust the relevant possibilities. Do not silently certify one branch, or silently change semantics to retain a favored conclusion.

**Accrual, §7.5.4:** combining reasons can matter, but it requires an account of how the reasons interact. Several weak arguments are not automatically one decisive argument. Preserve dependence, counterarguments, and whether a stronger combination changes the grounds used. No majority vote over argument counts substitutes for this analysis.

### 8. Reasoning about Priority Relations — pp. 203–220

Priorities may themselves be conclusions supported and contested by arguments. The book's collision-rule examples include **lex superior**, **lex posterior**, **lex specialis**, and special statutory preferences. Deciding to prefer the more specific rule is a legal decision, even if identifying logical specificity is a formal operation.

**Priority record:** which rule or argument prevails over which, on what authority or reason, for what issue and conditions, and subject to which challenge. A later lower-level instrument does not automatically defeat a superior norm. A general collision principle may yield to a supported special collision rule. Do not invent a universal order among these maxims.

**Revision:** if priority support changes, recompute the affected defeats and their descendants. If priority arguments themselves conflict or depend circularly on the conclusion they are meant to establish, expose that unresolved dependency; do not choose the priority that produces the desired outcome.

### 9. Systems for Defeasible Argumentation — pp. 221–244

The book compares approaches associated with Bondarenko–Dung–Kowalski–Toni, Pollock, Simari and Loui, Vreeswijk, Nute, Geffner and Pearl, and related research. Attack definitions, the handling of assumptions and priorities, and consequence notions differ.

**Use:** name the selected framework and its limits if a formal answer is requested. For ordinary analysis, explain support, conflict, and the basis of preference directly. This reference retains the comparison's methodological lesson, not all formal systems or proofs.

### 10. Using the Argumentation System — pp. 245–274

The applications discuss representing exceptions, implementation concerns, Toulmin's layout, existing AI-and-law systems, and a layered account of legal argumentation. Mapping Toulmin to a formal account requires specifying semantics; a warrant is not automatically a strict rule and a rebuttal condition is not automatically an established defeater.

**Four layers, §10.5:**

1. **Logical:** what supports a conclusion given premises and inference rules?
2. **Dialectical:** which arguments attack or defeat others, and which survive under the selected criteria?
3. **Procedural:** who may introduce or challenge information, when, and with which burdens or permissible moves?
4. **Strategic:** how should a participant conduct an effective argument within that procedure?

A convincing newly discovered argument can alter an analytical assessment yet be procedurally unavailable at a particular stage. A lawful procedural move need not be strategically wise. An effective strategy need not establish factual truth. Keep the questions separate.

The book discusses HYPO at the strategic layer. This is secondary discussion, not a substitute for a verified distillation of Ashley's monograph. No HYPO implementation or complete dimension method is claimed here.

### 11. Conclusion — pp. 275–282

The results support logical analysis of defeasibility and inconsistency while leaving substantial tasks in representation, interpretation, procedure, and strategy. An advisor using these ideas must still justify the inputs and disclose the portion of the argument space actually examined. A finite natural-language review cannot claim to have generated every legally possible argument.

## Worked Example

### Source pattern: defeat, reinstatement, and unresolved opposition

Section 6.5.1 explains why A's defeating B is insufficient: an undefeated C may defeat A and reinstate B. Section 6.5.8 gives equally ranked opposing defaults, leaving neither side justified. These patterns motivate the constructed legal example below; its rules and facts are stipulated, not borrowed law.

### Constructed termination routes and updates

**Supplied fictional rules:** R1: late notice ordinarily makes termination invalid. R2: an agreed emergency exception blocks R1. R3: termination without the required panel authorization independently makes it invalid. R4: a forged emergency consent does not establish the R2 exception. No other rules are assumed.

**Initial record:** a verified receipt establishes late notice; the supplied panel register and agreed completeness assumption establish absence of required authorization. The argument map is A1 = receipt + R1 → invalidity; A2 = register + completeness + R3 → invalidity. Each has its own conditions and evidence.

| Update | Local change | Result after reviewing all routes |
|---|---|---|
| Authentic emergency consent is added | B1 invokes R2 and blocks A1 | A2 remains; invalidity still has an independent sufficient route |
| The consent is shown to be forged | C1 invokes R4 against B1 | A1 can be reinstated if no other supported defeater remains; A2 was unaffected |
| A valid authorization entry is discovered | The completeness premise supporting A2 fails; A2 loses support | Reassess A1 using the current consent record; do not infer validity solely from the failure of A2 |
| Two supported, equally ranked interpretations of emergency consent remain | Conflict about B1 is unresolved | Describe A1 as unresolved on that issue; do not invent a priority |

**Critical boundary:** if A2 actually used the same unreliable database as A1's timing evidence, the routes might share a vulnerability. “Two arguments” is insufficient to establish independence. Conversely, a reply to an objection concerning one premise does not repair a different subargument.

**Floating variant:** R5 says employee status supports relief; R6 says contractor status supports the same relief on a different basis; the status dispute remains unresolved. This is not the same as the independent authorization route. Explain whether those two statuses exhaust the supplied alternatives, whether both conditional routes are sound, and whether relief is supported across alternatives without resolving status. Do not label a branch's argument justified just because both branches point to relief.

## Decision Rules & Judgment

### Update procedure — advisor adaptation

1. Preserve the earlier record of premises, rule interpretations, arguments, priorities, and conclusion. Mark what is new, withdrawn, contradicted, or merely queried.
2. Identify the exact target: an evidential premise, legal premise, inference application, contrary conclusion, or priority claim. Distinguish an undercutter from a rebuttal.
3. Construct the supported objection and its best supported replies. Track its dependencies and any exception to it; do not let repetition count as new support.
4. Reassess the affected argument and every argument relying on it. Follow attacks on attackers as well as forward support links.
5. Check all other sufficient routes. Test whether apparently separate routes share the failed premise, source, inference, or priority.
6. Separate route status from conclusion status. Where alternatives produce a shared result, identify the branch assumptions and consequence notion rather than silently changing them.
7. State what changes, what remains supported, and the fact, authority, or priority ruling that would resolve the remaining uncertainty. Apply the relevant procedural constraints and proof standard separately.

**Stopping condition:** for the supplied finite dispute, stop when the material supported attacks and replies have been addressed and the remaining uncertainty is explicit. If the record or argument space is incomplete, qualify the review's scope. Do not call an unexamined branch refuted or claim formal exhaustiveness.

## Key Takeaways

Defeat is relational and justification depends on the argument system. Reinstatement requires reassessment, priorities need grounds, and inconclusive opposition is not proof of the opposite. Preserve alternative routes and distinguish independently supported conclusions from conclusions shared only across alternative resolutions. These procedures support inspectable revision; they do not constitute an implemented formal reasoner.
