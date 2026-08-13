# Methods

The claim producers are intentionally separated:

- `repro/bfm/symbolic.py` reconstructs constants exactly in quadratic fields.
- `repro/bfm/mechanisms.py` implements BFM-SWM and BFM-VM.
- `repro/experiments/` generates finite ratio, runtime, economic, and influence checks.
- `repro/verify.py` combines each check with a negative control.
- `cpp_im/` retains the authors’ C++ influence implementation and baselines.
- `repro/src/finalize_gate.py` audits only committed evidence and fails closed on the source hash or Slashdot result contract.

No finite experiment is treated as a proof of a universal theorem.
