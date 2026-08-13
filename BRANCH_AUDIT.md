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

The live values below were checked against GitHub after the remote rename, branch deletion, and history audit.

## Live verification

- Repository: `MachineLearning-Nerd/icml26-budget-feasible-submodular-welfare`.
- Default branch: `main`; remote heads contain `main` only at `1ea0a53f234aa838fc4ef8b00a3e7f3635891327`.
- Legacy `orx/bfm-swm-faithful-reproduction`: deleted and absent from the live branch list.
- Homepage: <https://arxiv.org/abs/2605.00411v2>.
- Description: records finite evidence, the one-dataset influence result, `0/6` independently verified paper claims, and the inconclusive status.
- Reachable local `main` commits: all author and committer identities are `MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>`.
- Local `main` tracks `origin/main` with no uncommitted changes.
