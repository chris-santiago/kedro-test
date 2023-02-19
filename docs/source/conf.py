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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import re

from kedro.framework.cli.utils import find_stylesheets

from kedro_test import __version__ as release

# -- Project information -----------------------------------------------------

project = "Kedro Test"
copyright = "2021, Chris Santiago"
author = "Chris Santiago"

# The short X.Y version.
version = re.match(r"^([0-9]+\.[0-9]+).*", release).group(1)

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.imgmath",
    "sphinx.ext.viewcode",
    "sphinx.ext.mathjax",
    "nbsphinx",
    "sphinx.ext.githubpages",
    "sphinx.ext.napoleon",
    "myst_parser",
    "sphinx_copybutton",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]

# -- Additional user options -------------------------------------------------
source_suffix = [".rst", ".md"]
master_doc = "index"

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_title = "Kedro Test"
html_theme_options = {"collapse_navigation": False, "style_external_links": True}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
htmlhelp_basename = "kedro_testdoc"

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    #
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    #
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    #
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "kedro_test.tex",
        "kedro_test Documentation",
        "Kedro",
        "manual",
    )
]

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (
        master_doc,
        "kedro_test",
        "Kedro Test Documentation",
        [author],
        1,
    )
]

# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "kedro_test",
        "kedro_test Documentation",
        author,
        "kedro_test",
        "Project kedro_test codebase.",
        "Data-Science",
    )
]

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Extension configuration -------------------------------------------------

# nbsphinx_prolog = """
# see here for prolog/epilog details:
# https://nbsphinx.readthedocs.io/en/0.3.1/prolog-and-epilog.html
# """

# -- NBconvert kernel config -------------------------------------------------
nbsphinx_kernel_name = "python3"


def remove_arrows_in_examples(lines):
    for i, line in enumerate(lines):
        lines[i] = line.replace(">>>", "")


def autodoc_process_docstring(app, what, name, obj, options, lines):
    remove_arrows_in_examples(lines)


def skip(app, what, name, obj, skip, options):
    if name == "__init__":
        return False
    return skip


def setup(app):
    app.connect("autodoc-process-docstring", autodoc_process_docstring)
    app.connect("autodoc-skip-member", skip)
    # add Kedro stylesheets
    for stylesheet in find_stylesheets():
        app.add_css_file(stylesheet)


# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = False
napoleon_use_param = False
napoleon_use_rtype = False
napoleon_use_keyword = False
napoleon_custom_sections = None

# Autodoc
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "undoc-members": True,
    "inherited-members": True,
    "show-inheritance": True,
}
autoclass_content = "both"
autodoc_member_order = "bysource"
autodoc_typehints = "signature"
