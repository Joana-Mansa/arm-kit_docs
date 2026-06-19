"""Sphinx configuration for the ArmKit documentation.

This file is deliberately commented so a reviewer can see *why* each setting is
here, not just what it is.
"""

import os
import sys

# Make the source package importable so autodoc can read its docstrings.
sys.path.insert(0, os.path.abspath("../src"))

# -- Project information -----------------------------------------------------
project = "ArmKit Docs"
author = "Joana Owusu-Appiah"
copyright = "2026, Joana Owusu-Appiah"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
extensions = [
    "myst_parser",          # write docs in Markdown
    "sphinx.ext.autodoc",   # pull docstrings from the armkit package
    "sphinx.ext.napoleon",  # understand Google-style docstrings
    "sphinx.ext.viewcode",  # add "view source" links to the API reference
]

# PyBullet is a heavy, compiled dependency. We don't need it installed just to
# build the docs, so we mock it for autodoc. This keeps CI fast and reliable.
autodoc_mock_imports = ["pybullet", "pybullet_data"]
autodoc_member_order = "bysource"

# MyST extensions that the guides rely on.
myst_enable_extensions = ["colon_fence", "deflist"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- HTML output -------------------------------------------------------------
html_theme = "furo"
html_static_path = ["_static"]
html_title = "ArmKit Documentation"
