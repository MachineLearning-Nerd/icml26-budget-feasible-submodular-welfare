"""Audit the committed reproduction evidence without launching full experiments."""

from __future__ import annotations

import hashlib
import json
import math
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "source/arxiv-2605.00411.tar"
SOURCE_SHA256 = "1042e7805858b2a82641a5f2e25aaf5a18f564d36b464545950fffa9d7cff746"
CPP_RESULT = ROOT / "outputs/cpp/cpp_slashdot.json"

REQUIRED_FILES = (
    "repro/bfm/mechanisms.py",
    "repro/bfm/symbolic.py",
    "repro/experiments/runtime.py",
    "repro/experiments/economic.py",
    "repro/verify.py",
    "cpp_im/main.cpp",
    "outputs/cpp/cpp_slashdot.json",
)


def check_source() -> None:
    if hashlib.sha256(SOURCE.read_bytes()).hexdigest() != SOURCE_SHA256:
        raise RuntimeError("pinned arXiv source hash does not match")
    with tarfile.open(SOURCE) as archive:
        text = archive.extractfile("example_paper.tex").read().decode()
    for marker in (
        "BFM-SWM",
        "BFM-VM",
        "0.0328",
        "0.0877",
        "1/(12+4\\sqrt{3})",
        "4.49\\times",
    ):
        if marker not in text:
            raise RuntimeError(f"paper source marker missing: {marker}")


def summarize_slashdot() -> dict:
    data = json.loads(CPP_RESULT.read_text())
    rows = []
    for budget, mechanisms in data["results"].items():
        values = {name: mechanisms[name]["welfare"] for name in (
            "BFM-SWM", "Deng-Distorted", "Deng-ROI", "Deng-CostScaled"
        )}
        best_baseline = max(values[name] for name in values if name != "BFM-SWM")
        factor = values["BFM-SWM"] / best_baseline if best_baseline else math.inf
        rows.append({
            "budget": int(budget),
            "bfm_swm_welfare": values["BFM-SWM"],
            "best_baseline_welfare": best_baseline,
            "improvement_factor": factor,
            "bfm_swm_wins": values["BFM-SWM"] >= best_baseline,
        })
    if len(rows) != 10 or not all(row["bfm_swm_wins"] for row in rows):
        raise RuntimeError("committed Slashdot result does not contain ten BFM-SWM wins")
    factors = [row["improvement_factor"] for row in rows]
    return {
        "dataset": data["dataset"],
        "nodes": data["n"],
        "budgets": len(rows),
        "wins": sum(row["bfm_swm_wins"] for row in rows),
        "mean_improvement_factor": sum(factors) / len(factors),
        "min_improvement_factor": min(factors),
        "max_improvement_factor": max(factors),
        "rows": rows,
    }


def main() -> int:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).exists()]
    if missing:
        raise RuntimeError(f"required evidence files are missing: {missing}")
    check_source()
    slashdot = summarize_slashdot()
    gate = {
        "paper": "hqFugMmCqJ",
        "gate": "committed-evidence-audit",
        "audit_passed": True,
        "tests_passed": None,
        "publication_gate_passed": False,
        "finite_contracts_passed": 5,
        "finite_contracts_total": 6,
        "paper_claims_verified": 0,
        "paper_claims_total": 6,
        "overall_status": "INCONCLUSIVE",
        "contract_statuses": {
            "C1": "FINITE_EVIDENCE_RECORDED",
            "C2": "FINITE_EVIDENCE_RECORDED",
            "C3": "FINITE_EVIDENCE_RECORDED",
            "C4": "FINITE_EVIDENCE_RECORDED",
            "C5": "FINITE_EVIDENCE_RECORDED",
            "C6": "PARTIAL_DATASET_PASS",
        },
        "source_sha256": SOURCE_SHA256,
        "slashdot": slashdot,
        "scope": (
            "Committed finite/formula evidence for C1-C5 and one faithful Slashdot "
            "dataset for C6; universal theorem claims and the paper's full "
            "three-dataset influence result remain independently unverified."
        ),
    }
    for path in (ROOT / "outputs/publication_gate.json", ROOT / "outputs/verification.json"):
        path.write_text(json.dumps(gate, indent=2) + "\n")
    print(json.dumps(gate, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
