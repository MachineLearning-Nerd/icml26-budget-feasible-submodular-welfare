# Budget-Feasible Mechanisms for Submodular Welfare — Reproduction Report

**Paper:** Shuang Cui, He Huang, Yu-e Sun, and Chen Xue, *Budget-Feasible Mechanisms for Submodular Welfare Maximization in Procurement Auctions*, arXiv 2605.00411v2, OpenReview `hqFugMmCqJ`.

## Executive result

This checkout preserves substantial reproduction evidence but does not establish the paper’s universal claims. C1–C5 have exact/formula or finite experimental evidence recorded by the faithful reproduction branch. C6 has a tracked faithful C++ result for Slashdot at ten budgets. The paper’s Figure 1 combines three datasets, so the current repository status is **INCONCLUSIVE** rather than “all claims verified.”

## What was implemented

- BFM-SWM (Algorithm 1) and BFM-VM (Algorithm 2) in [`repro/bfm/mechanisms.py`](../../repro/bfm/mechanisms.py).
- Exact quadratic-field reconstruction of the three reported approximation constants in [`repro/bfm/symbolic.py`](../../repro/bfm/symbolic.py).
- Coverage, cut, and stressed-coverage finite instance families with brute-force optima.
- Runtime, economic-property, and influence-maximization experiment drivers under [`repro/experiments/`](../../repro/experiments/).
- The authors’ C++ influence code and baselines under [`cpp_im/`](../../cpp_im/), with tracked Slashdot input/output.

## Claim ledger

| Claim | Evidence preserved | Boundary |
|---|---|---|
| C1, Theorem 4.8 | Exact constant reconstruction and the report’s 32 finite welfare checks | Does not prove the general-submodular theorem. |
| C2, Theorem 4.10 | Exact constant reconstruction, 32 finite monotone-welfare checks, and runtime producer | Does not prove the monotone theorem or asymptotic bound. |
| C3, Theorem 5.4 | Exact BFM-VM constant and 32 finite valuation checks | Does not prove the worst-case approximation theorem. |
| C4, runtime | Finite slope comparison `0.99` versus `1.98` in the faithful report | A finite fit is not an asymptotic proof. |
| C5, Theorem 4.1 properties | 0 violations in 1,152 finite deviation/property checks | Operational checks are not a truthfulness proof. |
| C6, Figure 1 | `outputs/cpp/cpp_slashdot.json`: 10/10 Slashdot budget wins, mean `4.564×` | Email/Epinions faithful outputs and the paper-wide `4.49×` aggregate are not reproduced here. |

## Slashdot calculation

The tracked file contains ten budgets from 100 through 1,000 for a graph with 77,360 nodes. For every budget, BFM-SWM welfare is at least the strongest of Deng-Distorted, Deng-ROI, and Deng-CostScaled. The resulting improvement factors range from `2.971×` to `6.362×`, with arithmetic mean `4.564×`. This is a one-dataset result, not the paper’s full aggregate.

## Reproduction

```bash
uv run python repro/src/run_publication_gate.py  # cheap committed-evidence audit
uv run python -m repro.run_all                    # full C1–C6 experiment driver
```

The full driver can be expensive. Generated `outputs/claim_*.json`, `outputs/EVAL.md`, and `outputs/claim_verdicts.json` are ignored; the raw Slashdot result is tracked. The current gate intentionally audits committed evidence without silently presenting an unrun full campaign as verified.

## Honest limitations

The paper’s theorems remain paper claims. Finite mechanisms and symbolic constants are valuable checks, but they cannot replace the proofs. The current influence evidence uses one dataset and retains author-provided C++ code as a separately identified input. See the repository README for the complete producer map, branch history, citation, and thank-you note.
