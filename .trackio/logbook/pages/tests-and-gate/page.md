# Tests and gate

## Current gate

```bash
uv run python repro/src/run_publication_gate.py
```

This is a lightweight committed-evidence audit. It checks the pinned source archive, required producer files, and the tracked Slashdot result. It does not launch the full C1–C6 campaign.

Current result: `audit_passed: true`, `finite_contracts_passed: 5/6`, `paper_claims_verified: 0/6`, `overall_status: INCONCLUSIVE`.

## Full experiment driver

```bash
uv run python -m repro.run_all
```

The full driver may be expensive and writes generated claim outputs that are intentionally ignored. Its output must be interpreted with the same finite-versus-paper boundary documented in the README.
