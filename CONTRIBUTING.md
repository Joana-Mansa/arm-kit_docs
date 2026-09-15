# Contributing to the docs

This project uses a **Docs-as-Code** workflow. Documentation is treated like
source code: it lives in Git, changes go through pull requests, and a CI
pipeline builds and publishes it.

## The workflow

1. Create a branch for your change.
2. Edit or add Markdown files under `docs/`.
3. Build locally and check your change renders:
   ```console
   sphinx-build -b html docs docs/_build/html -W
   ```
   The `-W` flag turns warnings into errors, matching CI.
4. Open a pull request. Fill in the template, including the Diátaxis category.
5. CI builds your branch. A green build means the docs compile with no warnings.
6. After review and merge to `main`, the site deploys to GitHub Pages
   automatically.

## Writing standards

All content follows the [style guide](docs/style-guide.md). The short version:
short sentences, active voice, consistent terminology, explicit units, and the
right Diátaxis category for each page.

## Adding to the API reference

The reference is generated from docstrings in `src/armkit/`. To document new
code, write a Google-style docstring on the function or class: it will appear
in the reference automatically on the next build. Do not hand-write API docs.
