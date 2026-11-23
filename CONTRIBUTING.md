# Contributing

Thanks for helping with kubex-py. This guide applies to every repository in the
organization. A repository can add its own `CONTRIBUTING.md` or `CLAUDE.md` / `AGENTS.md`
with project-specific details; those take precedence.

## Before you start

- For a bug, open an issue with a minimal reproduction, unless the fix is obvious and small.
- For a new feature or an API change, open an issue first so the design can be agreed
  before you write the code.
- Security problems are not reported in issues. See [SECURITY.md](SECURITY.md).

## Development setup

The projects use [uv](https://docs.astral.sh/uv/) for environments and dependencies,
[ruff](https://docs.astral.sh/ruff/) for linting and formatting, [mypy](https://mypy-lang.org/)
in strict mode, and [pytest](https://docs.pytest.org/). Most repositories also have a
[mise](https://mise.jdx.dev/) file with the common tasks and a
[pre-commit](https://pre-commit.com/) configuration.

```bash
uv sync                # create the virtualenv with the dev dependencies
pre-commit install     # run the hooks on every commit
uv run pytest          # tests
uv run ruff check .    # lint
uv run ruff format .   # format
uv run mypy .          # type check (some repos check `src tests` instead)
```

CI runs the tests on every supported Python version, including the free-threaded
(no-GIL) builds `3.14t` and `3.15t`. Code that shares state between threads must be safe
without the GIL.

## Pull requests

- Keep a pull request to one change. Split refactors from behaviour changes.
- Add or update tests for the behaviour you change.
- Update the docs and the `CHANGELOG.md` (under "Unreleased") when users will notice the
  change.
- CI must pass: lint, format, mypy and the test matrix.
- Write commit messages in the imperative ("Add …", "Fix …") and explain why in the body
  when it isn't obvious from the diff.

## Working on several repositories at once

kubex depends on kubex-core and the generated model packages; kubex-runtime depends on
kubex. To test a change across repositories, point the dependent project at your local
checkout without committing the override, for example:

```bash
uv pip install -e ../kubex-core
```

## Code of conduct

Everyone taking part is expected to follow the [code of conduct](CODE_OF_CONDUCT.md).
