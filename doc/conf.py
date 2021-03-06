# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

_HERE = os.path.dirname(__file__)
_ROOT_DIR = os.path.abspath(os.path.join(_HERE, '..'))
_SRC_DIR = os.path.abspath(os.path.join(_HERE, '../src'))

sys.path.insert(0, _ROOT_DIR)
sys.path.insert(0, _SRC_DIR)

# -- Project information -----------------------------------------------------

project = 'photonomist'
copyright = '2022, Panagiotis Karydakis'
author = 'Panagiotis Karydakis'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
                'sphinx.ext.autodoc',
             ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- WARNING: autodoc: failed to import module 'gui' from module 'src.GUI'; the following exception was raised: -------------------------------------------------
# -- libtk8.6.so: cannot open shared object file: No such file or directory -------------------------------------------------

# If sphinx can not import a module while trying to autogenarate documentation from docstrings
# It gives a warning and skips this module
# autodoc_mock_imports helps with ingoring the modules that it can not import
autodoc_mock_imports = ['tkinter', 'languages', 'widgets', 'byte_stream', 'info', 'exclude', 'loading']

master_doc = 'index'