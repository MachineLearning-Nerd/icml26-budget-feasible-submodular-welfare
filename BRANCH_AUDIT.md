# Branch audit

## Intended roles

| Ref | Role | Evidence |
|---|---|---|
| `main` | Canonical publication surface; began as the source-pinned certificate and now contains the consolidated implementation and evidence | `git log --all`, README, report |
| `orx/bfm-swm-faithful-reproduction` | Substantive mechanism implementation, exact symbolic checks, finite experiments, authors’ C++ influence code, SNAP data, report, and walkthrough | Merged into `main` by commit `ae159e0` |

The `orx/` prefix referred to the execution environment used for the experiment. It is not part of the public branch vocabulary.

## Cleanup contract

The final remote state for this repository is intended to be:

- repository name: `icml26-budget-feasible-submodular-welfare`
- default branch: `main`
- retained branches: `main` only
- homepage: <https://arxiv.org/abs/2605.00411v2>
- reachable commit author and committer: `MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>`

The live values are filled in below after the remote rename, branch deletion, and history audit.

## Live verification

- Repository: pending final remote audit.
- Default branch and sole-branch check: pending.
- Legacy `orx/*` branch deletion: pending.
- Reachable author/committer check: pending.
