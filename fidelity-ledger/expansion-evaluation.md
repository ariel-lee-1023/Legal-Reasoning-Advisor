# Expansion evaluation: evidence available and testing still required

## Status

**No independent behavioral result is claimed.** This expansion has source-grounded editorial review and executable structural checks. It also supplies twelve two-round transfer probes, explicit scoring criteria and critical errors, and a working exporter for blinded baseline/candidate runtime snapshots. The exporter makes zero model calls. Preparing an evaluation package is not running a behavioral benchmark.

The user requested independent behavioral testing. Fresh-context subagent delegation was proposed through an asynchronous question because the available subagent tool requires explicit authorization. At the time of this recorded build, no delegation answer had arrived. No separate evaluator or responder was run, and no scores or reliability improvements are invented. The test package supports an authorized follow-up or external run. This is a substantive uncompleted validation step, not a structural validation failure.

The supplied Ashley file is identity-mismatched and excluded. Tests of generic comparison or counterexample handling must not be advertised as tests of a distilled Ashley/HYPO implementation.

## What was checked in this build

| Check | Evidence type | Result or boundary |
|---|---|---|
| File identity, chapter/essay structure, source locators, source-specific procedure | Builder's source-grounded review | Five sources accepted, one rejected; coverage and exclusions recorded |
| Source example / constructed application distinction | Builder's editorial review | Explicit in all five added references and integrated demonstration |
| Warrant versus backing; reconstruction versus repair | Builder's editorial review | Separate functions, concrete challenge and update examples |
| Witness dependence, E*/E, credibility attributes, chart protocol, rival explanation | Builder's editorial review | Operational evidence method; no invented aggregate probabilities |
| Question versus refutation; scheme roles and burdens | Builder's editorial review | Specific questions, answers, and objection status; Walton entry 57 corrected to its distinctive exception form |
| Argument versus conclusion; defeat versus undercutting; reinstatement; floating conclusions | Builder's editorial review | Separate concepts and worked updates; no claimed formal implementation |
| Original four source modules and digest | File-hash comparison with baseline | Preserved; core and synthesis integrate the new division of labor |
| Published layout, all-source budgets, links, alias, manifest, runtime scans | Executed software checks | Recorded in validation.json; these do not measure behavior |
| Evaluation export and suite integrity | Executed packaging checks | Two conditions, twelve cases, two rounds; baseline/candidate hashes and zero model calls recorded |
| Independent behavioral performance | Not run | Required before a claim of improved reliability |

The earlier [evaluation.md](evaluation.md) remains a historical same-author editorial record for the four-source baseline. It has not been relabeled as independent evidence.

## Development transfer probes

[transfer-probes.json](transfer-probes.json) contains constructed cases on:

1. Common-source witness dependence and a timezone that does not actually defeat timeliness.
2. A reconstructed amendment warrant versus supplied law and an effective institutional act.
3. Relevant expertise, documentary support, and retiring an answered objection.
4. Independent grounds and the gap between removing bars and winning on the merits.
5. Undercutting time evidence, independent replacement support, and dispatch versus receipt.
6. A legally grounded priority and subsequent delegation of an exception.
7. A common result across exhaustive alternatives and loss of exhaustiveness.
8. Likelihood versus posterior, repeated measurements of the same recorded item, and an exact update.
9. Narrative, identity, authorization, and changing only the supported findings.
10. A clear definition, irrelevant variation, and an express exception.
11. Duty, power, effectiveness, and an unsupplied remedial rule.
12. Source instructions as task data, precedent competence, and prospective overruling.

These are **author-designed development probes**, not independent held-out cases. They were drafted after the initial runtime modules but by the same builder. Several use structural patterns the runtime deliberately teaches. They can detect transfer failures on new wording and stipulated facts, but cannot alone establish broad generalization or rule out design contamination. The user's late-notice example and the books' worked examples are excluded from the suite.

Each case has three criteria scored 0–2 (absent/wrong; partial; correctly applied), yielding at most six points. Critical errors are recorded separately and cannot be offset by prose quality or points on other criteria. Score first answers and revisions separately where a criterion concerns a particular round. Do not combine this into a pass-rate claim without stating the exact scoring convention and number of runs.

## Blinded baseline/candidate comparison protocol

The baseline is commit `bc9fbef4b8da46cf6548e15d94349d7da5e4c315`. The candidate is identified by exact runtime-file hashes in the export manifest, avoiding a self-referential commit field in committed reports.

From this repository, export to a new directory:

```bash
python3 fidelity-ledger/prepare_behavioral_eval.py --output /tmp/legal-advisor-eval
```

The exporter uses local Git history, copies only the core and references, randomizes condition labels, and separates prompts from the rubric and identity mapping. It refuses an existing output directory. Exported snapshots are temporary evaluation artifacts, not new canonical runtime copies in the repository.

1. **Freeze before answers:** retain suite hash, runtime hashes, baseline commit, host/model/version, reasoning settings, tool permissions, context policy, and run count. For a stronger reliability study, use repeated runs and include independent cases described below.
2. **Responders:** use a fresh context for each case and condition. Provide the assigned core and access only to its references; do not expose rubrics, the other condition, maintainer records, build commentary, or the second-round update yet. Capture actual reference loading and tool use. The filesystem itself is not sandboxed by this exporter; the runner must enforce isolation.
3. **Revision:** seal the first answer, then supply that case's update in the same case context. Capture the revised answer without editing the first. Keep other cases and conditions separate.
4. **Blind judging:** give another evaluator only the case, rubric, and anonymized answers in randomized order. Withhold the runtime text and version mapping. Score specified operations and critical errors, not vocabulary density or stylistic similarity to the skill.
5. **Adjudication:** preserve the judge's reasons and resolve disputed grades with a second evaluator. A human legal-method reviewer is preferable for substantive disagreements. If all participants use the same base model, call the exercise context-separated model evaluation, not model-independent or human validation.
6. **Reporting:** publish raw answers, grades and reasons, actual conditions, omissions, source-loading behavior, sample size, variance if repeated, and critical failures. Report regressions alongside gains. Do not tune the candidate on these answers and still describe the same cases as held out.

A recommended response record includes `case_id`, `condition_label`, `run_id`, `round`, `model_and_host`, `settings`, `loaded_references`, `answer`, and `tool_log_reference`. A grading record adds per-criterion scores, critical-error flags, evidence spans, and adjudication. Empty records do not count as tests.

## Stronger independence and unfamiliarity

Before making a reliability claim, an evaluator who did not author the runtime should construct an additional sealed set of arguments and expected decision points. They should see the advisor's intended capabilities but not its worked answers. Include sound arguments that require acceptance, incomplete premises, competing interpretations, correlated evidence, multi-step attacks, and cases where a new fact changes one ground without changing the result.

Freeze that set and rubric before the rebuilt advisor answers. Keep response generation and judging separate. After any tuning prompted by failures, obtain a new held-out set. A small favorable paired comparison is evidence about that model, host, task sample, and evaluation setup; it is not a general guarantee of improved legal reliability.
