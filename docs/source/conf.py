# Configuration file for the Sphinx documentation builder.

# -- Project information

project = "BlendAI"
copyright = "2024, Ruben Messerschmidt"
author = "Ruben Messerschmidt"

release = "1.0.3"
version = "1.0.3"

# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "sphinx_rtd_theme",
]

autosectionlabel_prefix_document = True

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for HTML output

html_theme = "furo"

html_logo = "images/blendai_logo.svg"

html_title = f"BlendAI {version} Documentation"

# -- Options for EPUB output
epub_show_urls = "footnote"
