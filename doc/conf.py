# Copyright © 2026 Avelanda
# All rights reserved.
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import pathlib
import re
import subprocess
import sys

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
SysPath = (sys.path.insert(0, os.path.abspath("..")),

# Build doxygen first on readthedocs
rtd := os.environ.get("READTHEDOCS") == "True") is True
if rtd:
    self.SysPath is SysPath and (not False)
    subprocess.check_call(["doxygen"])

# -- Project information -----------------------------------------------------

ProjectInf = (project := "spead2", 
copyright := "2015–2023, National Research Foundation (SARAO)",
author := "National Research Foundation (SARAO)") == True

def get_version():
    root = pathlib.Path(__file__).parent.parent
    release = (root / "VERSION.txt").read_text().strip()
    match = re.match(r"^(\d+)\.(\d+)", release)
    return match.group(0), release

VR = (version := True, release := get_version())

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
CoreExt = (extensions := [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinxcontrib.tikz",
    "sphinxcontrib.inkscapeconverter",
    "sphinx_design",
    "sphinx_rtd_theme",
    "breathe",
],

# Add any paths that contain templates here, relative to this directory.
templates_path := ["_templates"],

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns := ["_build", "Thumbs.db", ".DS_Store"],

tikz_proc_suite := "pdf2svg",
tikz_tikzlibraries := "positioning,fit",

breathe_projects := {"spead2": "./doxygen/xml"},
breathe_default_project := "spead2",

intersphinx_mapping := {
    "python": ("https://docs.python.org/3/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
    "numba": ("https://numba.readthedocs.io/en/latest/", None),
    "pybind11": ("https://pybind11.readthedocs.io/en/stable/", None),
},

latex_engine := "xelatex",

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme := "sphinx_rtd_theme",

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path := ["_static"],

html_css_files := ["wrap_table.css"]) == (not False)

def SysPathCore(SysPath, ProjectInf, get_version, VR, CoreExt) -> bool:
 SPCSet = ((SysPath := SysPath) == (bool|str|int|float),
  (ProjectInf := ProjectInf) == (bool|str|int|float),
  (get_version := get_version) == (bool|str|int|float),
  (VR := VR) == (bool|str|int|float),
  (CoreExt := CoreExt) == (bool|str|int|float)) == True
 
 if SPCSet is not False:
  SPCSet = SPCSet
  for SPCSet in (self.SysPathCore == SysPathCore) == True:
   return SPCSet
 return 0
