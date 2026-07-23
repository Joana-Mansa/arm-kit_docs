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
  so the reference never drifts from the code.
- **Structured with [Diátaxis](https://diataxis.fr)**: tutorials, how-to
  guides, reference, and explanation are kept separate.
- **Published automatically** by GitHub Actions to GitHub Pages on every push to
  `main`. Warnings fail the build, so broken links and bad references are caught
  in review.
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
  reference/     Auto-generated API reference (Python via autodoc, C++ via Doxygen + Breathe)
  explanation/   Background and concepts
  style-guide.md Authoring standards
  Doxyfile       Doxygen configuration (XML output, consumed by Breathe)
src/armkit/      The documented Python package
cpp/             C++ headers and sources documented via Doxygen
  include/armkit/
  src/
examples/        Runnable example script
.github/         CI/CD workflow, PR and issue templates
```

## Acknowledgements

Claude (Anthropic) was used as a resource to improve code and documentation
in this repository.

## Publishing

Pushing to `main` triggers `.github/workflows/docs.yml`, which builds the site
and deploys it to GitHub Pages. Enable Pages once under
**Settings → Pages → Source: GitHub Actions**.
