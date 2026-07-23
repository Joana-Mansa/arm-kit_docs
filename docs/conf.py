"""Sphinx configuration for the ArmKit documentation.

This file is deliberately commented so a reviewer can see *why* each setting is
here, not just what it is.
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

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
    "breathe",              # render Doxygen XML for the C++ reference
]

# PyBullet is a heavy, compiled dependency. We don't need it installed just to
# build the docs, so we mock it for autodoc. This keeps CI fast and reliable.
autodoc_mock_imports = ["pybullet", "pybullet_data"]
autodoc_member_order = "bysource"

# MyST extensions that the guides rely on.
myst_enable_extensions = ["colon_fence", "deflist"]

templates_path = ["_templates"]
# _doxygen holds the Doxygen XML output; it is a build artefact, not source.
exclude_patterns = ["_build", "_doxygen", "Thumbs.db", ".DS_Store"]

# -- Breathe: bridge Doxygen XML into Sphinx ---------------------------------
# The C++ headers live under ../cpp/include and are parsed by Doxygen into
# _doxygen/xml/ (see docs/Doxyfile). Breathe reads that XML so the C++ and
# Python references render into the same site with the same theme and search
# index.
_docs_dir = Path(__file__).parent
breathe_projects = {"armkit_cpp": str(_docs_dir / "_doxygen" / "xml")}
breathe_default_project = "armkit_cpp"


def _run_doxygen(app):
    """Run Doxygen before Sphinx reads the sources.

    Keeping this here means `sphinx-build` is the single entry point: a local
    build and the CI build are exactly the same command, so a contributor
    cannot produce a passing local build that fails in the pipeline.
    """
    doxyfile = _docs_dir / "Doxyfile"
    if not doxyfile.exists():
        return
    if shutil.which("doxygen") is None:
        raise RuntimeError(
            "doxygen is not on PATH. Install it (winget install "
            "DimitriVanHeesch.Doxygen on Windows, apt-get install doxygen on "
            "Ubuntu) so the C++ reference can be built."
        )
    subprocess.run(["doxygen", str(doxyfile)], cwd=str(_docs_dir), check=True)


def setup(app):
    app.connect("builder-inited", _run_doxygen)


# -- HTML output -------------------------------------------------------------
html_theme = "furo"
html_static_path = ["_static"]
html_title = "ArmKit Documentation"
