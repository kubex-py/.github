# .github

Organization-wide files for [kubex-py](https://github.com/kubex-py): the org profile,
default community files, reusable workflows and workflow templates.

## Default community files

Repositories without their own copy use these:
[CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md),
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), [FUNDING.yml](.github/FUNDING.yml), the
[issue forms](.github/ISSUE_TEMPLATE) and the
[pull request template](.github/pull_request_template.md). The org page shows
[profile/README.md](profile/README.md).

## Reusable workflows

| Workflow | What it does |
|---|---|
| [python-ci.yml](.github/workflows/python-ci.yml) | pre-commit, ruff, mypy, pytest on 3.11–3.15 plus free-threaded 3.14t and 3.15t, and an optional strict mkdocs build with a lychee link check |
| [python-build.yml](.github/workflows/python-build.yml) | `uv build` into a `dist` artifact; optionally checks the version against the release tag, or adds a `.devN` suffix for TestPyPI |
| [docs-mike.yml](.github/workflows/docs-mike.yml) | Deploys the mkdocs site with mike: the default branch as `dev`, release tags as versions |

Publishing to PyPI isn't a reusable workflow: PyPI trusted publishing doesn't work from
inside one. Each repository keeps a short publish job that downloads the `dist` artifact
from `python-build.yml` and uploads it. The templates below include it.

```yaml
jobs:
  ci:
    uses: kubex-py/.github/.github/workflows/python-ci.yml@main
    with:
      test-sync-args: --all-extras
```

Every input is documented in the workflow file.

## Workflow templates

[workflow-templates](workflow-templates) has `ci.yml`, `publish.yml`, `publish-test.yml` and
`docs.yml`, wired to the reusable workflows. They appear under **Actions → New workflow** in
every org repository. The publish templates list the PyPI trusted-publisher settings to
register.

## Testing changes

[self-test.yml](.github/workflows/self-test.yml) runs the reusable workflows against the
fixture package in [tests/fixture](tests/fixture) on every pull request.
