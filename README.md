# Budget-Feasible Mechanisms for Submodular Welfare Maximization

Independent reproduction audit for **“Budget-Feasible Mechanisms for Submodular Welfare Maximization in Procurement Auctions”** (arXiv [2605.00411v2](https://arxiv.org/abs/2605.00411v2), OpenReview `hqFugMmCqJ`, accepted at ICML 2026).

## Current status

**Overall: `INCONCLUSIVE` — finite evidence is recorded, but the six paper-level claims are not independently verified.**

The repository contains a faithful implementation of BFM-SWM and BFM-VM, exact symbolic checks for the reported constants, finite mechanism experiments, the authors’ influence-maximization C++ implementation, SNAP data, and a committed Slashdot result file. The evidence is useful and reproducible, but finite tests do not prove universal theorems. The influence experiment covers Slashdot here; the paper’s three-dataset aggregate is not reproduced in this checkout.

Historical files and commit messages use `VERIFIED` for a broader run. This README is the current conservative interpretation of the evidence.

| Claim | Paper result | Evidence in this repository | Current audit status |
|---|---|---|---|
| C1 | BFM-SWM general welfare ratio `3/(4(13+4√6)) ≈ 0.0328` | Exact quadratic-field reconstruction plus 32 finite mechanism instances, as reported in `reports/bfm-swm-repro/report.md` | `FINITE EVIDENCE RECORDED` |
| C2 | Monotone welfare ratio `2/(13+4√6) ≈ 0.0877` | Exact reconstruction plus 32 finite instances; runtime code is in `repro/experiments/runtime.py` | `FINITE EVIDENCE RECORDED` |
| C3 | BFM-VM ratio `1/(12+4√3) ≈ 0.0528` | Exact quadratic-field reconstruction plus 32 finite valuation instances | `FINITE EVIDENCE RECORDED` |
| C4 | Runtime improves from `O(n² log n)` to `O(n log n)` | Finite log-log slopes reported as `0.99` for BFM-VM and `1.98` for the naive baseline | `FINITE EVIDENCE RECORDED` |
| C5 | Budget feasibility, IR, surplus, and truthfulness | Finite deviation suite reported as 0 violations across 1,152 checks | `FINITE EVIDENCE RECORDED` |
| C6 | BFM-SWM improves over baselines on the paper’s SNAP experiments | Tracked authors’ C++ output: 10/10 Slashdot budgets beat the best baseline; mean factor `4.564×` | `PARTIAL DATASET PASS` |

`outputs/publication_gate.json` records this boundary as a machine-readable committed-evidence audit. `paper_claims_verified` is intentionally `0/6`.

## What the paper does

The paper studies procurement auctions where sellers have private costs and a buyer has a limited budget. It proposes **BFM-SWM**, a budget-feasible mechanism for maximizing submodular social welfare `v(S) − c(S)`, with truthfulness, individual rationality, and non-negative auctioneer surplus. It also proposes **BFM-VM**, a valuation-maximization variant with a deterministic `1/(12+4√3)` approximation and lower claimed query complexity than the previous `1/64` deterministic bound.

## Repository map

| Path | Role |
|---|---|
| `repro/bfm/mechanisms.py` | Python implementations of BFM-SWM and BFM-VM |
| `repro/bfm/symbolic.py` | Exact constant reconstruction in quadratic fields |
| `repro/bfm/oracles.py` | Coverage, cut, and other submodular value oracles plus brute-force optima |
| `repro/experiments/` | Finite ratio, runtime, economic-property, and influence experiments |
| `repro/verify.py` | Claim-level verifiers and negative controls |
| `repro/run_all.py` | Full C1–C6 reproduction driver |
| `cpp_im/` | Authors’ C++ influence-maximization implementation and baselines |
| `data/snap/` | Tracked SNAP graph inputs and node costs |
| `outputs/cpp/cpp_slashdot.json` | Tracked ten-budget Slashdot result used by the current audit |
| `source/arxiv-2605.00411.tar` | Pinned arXiv source archive |
| `reports/bfm-swm-repro/report.md` | Reader-facing evidence report |
| `.trackio/logbook/pages/` | Claim-by-claim experiment logbook |

## How each claim is produced

| Claim | Producer path | What is measured |
|---|---|---|
| C1 | `repro/verify.py::verify_claim1` → `repro/bfm/symbolic.py`, `mechanisms.py`, `experiments/instances.py` | The exact constant is reconstructed; BFM-SWM welfare gaps are checked on generated cut and stressed-coverage instances against brute-force optima, with an empty-set negative control. |
| C2 | `repro/verify.py::verify_claim2` → the same mechanism/oracle stack | The monotone-welfare inequality is checked on generated coverage and stressed instances; the runtime comparison is produced by `repro/experiments/runtime.py`. |
| C3 | `repro/verify.py::verify_claim3` → `symbolic.py`, `bfm_vm`, and brute-force valuation optima | The BFM-VM constant is reconstructed exactly and finite valuation ratios are compared with the guarantee, again with a negative control. |
| C4 | `repro/verify.py::verify_claim4` → `repro/experiments/runtime.py` | Timed query counts are fitted on increasing `n`; the reported slopes compare BFM-VM with naive greedy selection. |
| C5 | `repro/verify.py::verify_claim5` → `repro/experiments/economic.py` | Budget, payment, IR, surplus, and seller-deviation checks are run over finite generated instances. This is operational testing, not a proof of strategyproofness. |
| C6 | `repro/verify.py::verify_claim6` → `repro/bfm/cpp_runner.py`, `cpp_im/`, `outputs/cpp/cpp_slashdot.json` | BFM-SWM welfare is compared with Deng-Distorted, Deng-ROI, and Deng-CostScaled at each tracked Slashdot budget. The current committed file has 10/10 wins, factors from `2.971×` to `6.362×`, and mean `4.564×`. |

## Reproduction commands

The lightweight audit checks the pinned source and the committed Slashdot result without launching the expensive experiment:

```bash
uv run python repro/src/run_publication_gate.py
```

The full experiment driver runs all six claim verifiers and writes generated claim files under `outputs/` (those generated files are ignored by Git):

```bash
uv run python -m repro.run_all
```

The full driver may require substantial CPU time and memory, especially for SNAP influence maximization. It may attempt to regenerate the Slashdot C++ result and uses the committed result as a fallback. The current audit does not represent an independent rerun of every paper-scale experiment.

For the small historical source-pinned certificate only:

```bash
uv run python repro/src/verify_budget_feasible.py --output /tmp/bfm-source-certificate.json
```

## Branch and history audit

The final publication surface is `main`.

| Branch | Role | Disposition |
|---|---|---|
| `main` | Original source-pinned certificate, now containing the consolidated reproduction implementation and evidence | Retained as the only canonical branch |
| `orx/bfm-swm-faithful-reproduction` | Substantive implementation, SNAP inputs, C++ comparison, report, and walkthrough | Merged into `main`; remove after the final remote audit |

The old branch name describes an execution environment, not a public research artifact. The final cleanup will leave only `main`, set the repository name to `icml26-budget-feasible-submodular-welfare`, and normalize reachable commit attribution to `MachineLearning-Nerd`.

See [`BRANCH_AUDIT.md`](BRANCH_AUDIT.md) for the live post-cleanup verification.

## Limitations

- Exact symbolic equality of an approximation constant does not prove the theorem that uses it.
- Finite generated instances cannot establish worst-case guarantees over all submodular valuations.
- The 1,152 strategyproofness checks are deviation tests, not a formal proof.
- The tracked faithful influence result is Slashdot only. Email and Epinions are present as data, but their paper-scale faithful C++ results are not committed here.
- The paper reports a three-dataset Figure 1 aggregate of `4.49×`; the committed Slashdot-only mean is `4.564×` and must not be presented as the paper-wide reproduction.
- Dataset provenance, machine details, random seeds, and implementation substitutions are documented in the report and experiment modules; the original paper’s Windows workstation is not reproduced by the current environment.

## Citation

```bibtex
@misc{cui2026budget,
  title         = {Budget-Feasible Mechanisms for Submodular Welfare Maximization in Procurement Auctions},
  author        = {Shuang Cui and He Huang and Yu-e Sun and Chen Xue},
  year          = {2026},
  eprint        = {2605.00411},
  archivePrefix = {arXiv},
  primaryClass  = {cs.GT},
  note          = {Accepted at ICML 2026; version 2}
}
```

Paper URL: <https://arxiv.org/abs/2605.00411v2>

## Thank you

Thank you to Shuang Cui, He Huang, Yu-e Sun, and Chen Xue for making the paper, source archive, algorithms, and experimental details clear enough to study and reproduce. This repository is an independent audit and is not an official implementation or endorsement by the authors.

## Attribution

The repository is maintained by [MachineLearning-Nerd](https://github.com/MachineLearning-Nerd). The C++ influence-maximization implementation is retained as author-provided reproduction material and is identified separately from the independent audit code.
