# Evidence gate

This repository has a **committed-evidence audit**, not a universal theorem verifier.

- `uv run python repro/src/run_publication_gate.py` checks the pinned arXiv source, required producer files, and the tracked ten-budget Slashdot result.
- C1–C5 are recorded as finite/formula evidence.
- C6 is a one-dataset pass: ten of ten tracked Slashdot budgets beat the best baseline, with mean factor `4.564×`.
- `paper_claims_verified` is `0/6` and `overall_status` is `INCONCLUSIVE`.
- The full `uv run python -m repro.run_all` campaign remains available but is not silently treated as the current gate result.
