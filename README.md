# ArmKit: a Docs-as-Code documentation example

ArmKit is a small Python wrapper around the [PyBullet](https://pybullet.org)
physics engine for loading and moving a simulated robot arm. The code is
deliberately tiny. The real subject of this repository is its **documentation
pipeline**.

It demonstrates an end-to-end Docs-as-Code workflow:

- **Source in Git**: every doc is plain text under version control.
- **Written in Markdown** (via MyST), with reStructuredText where it helps.
- **Built with Sphinx**, using the Furo theme.
- **API reference auto-generated** from docstrings with `autodoc` + `napoleon`,
  so API signatures are generated from the code.
- **Structured with [Diátaxis](https://diataxis.fr)**: tutorials, how-to
  guides, reference, and explanation are kept separate.
- **Published automatically** by GitHub Actions to GitHub Pages on every push to
  `main`. Warnings fail the build, including unresolved internal references.
- **Authoring standards** captured in a [style guide](docs/style-guide.md),
  including translation-friendly writing rules.

## Build the docs locally

```console
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
sphinx-build -b html docs docs/_build/html
```

Then open `docs/_build/html/index.html`.

## Run the example

```console
pip install -e .
python examples/move_arm.py
```

## Repository layout

```
docs/            Documentation source (Markdown), organised by Diátaxis
  tutorials/     Learning-oriented
  how-to/        Task-oriented
  reference/     Auto-generated API reference
  explanation/   Background and concepts
  style-guide.md Authoring standards
src/armkit/      The documented Python package
examples/        Runnable example script
.github/         CI/CD workflow, PR and issue templates
```

## Publishing

Pushing to `main` triggers `.github/workflows/docs.yml`, which builds the site
and deploys it to GitHub Pages. Enable Pages once under
**Settings → Pages → Source: GitHub Actions**.

## Verification and development branches

The headless example was checked on 15 September 2026: after 240 steps, joint 1 reached 0.500 rad for a 0.5 rad command. The documentation build is checked with warnings treated as errors.

The `docs/add-cpp-reference` branch contains an experimental C++/Doxygen extension. It is not part of the default Python package or published main-branch reference; its source and documentation need a separate integration review before release.
