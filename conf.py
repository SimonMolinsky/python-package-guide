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


# -- Project information -----------------------------------------------------

project = "python-package-guide"
copyright = "2023, pyOpenSci"
author = "pyOpenSci Community"

# The full version, including alpha/beta/rc tags
release = "0.1"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_nb",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx.ext.intersphinx",
    "sphinx_sitemap",
    "sphinxcontrib.gtagjs",
    "sphinxext.opengraph",
]

# colon fence for card support in md
myst_enable_extensions = [
    "colon_fence",
    "deflist",
]
myst_heading_anchors = 3

# For generating sitemap
html_baseurl = "https://www.pyopensci.org/software-peer-review/"

# Link to our repo for easy PR/ editing
html_theme_options = {
    "announcement": "🚧 This guide is currently under heavy construction 🚧 ",
    "external_links": [
        {
            "url": "https://www.pyopensci.org",
            "name": "pyOpenSci Website",
        },
        {
            "url": "https://www.pyopensci.org/python-package-guide",
            "name": "Python Packaging Guide",
        },
        {
            "url": "https://pyopensci.org/governance",
            "name": "Governance",
        },
    ],
    "icon_links": [
        {
            "name": "Mastodon",
            "url": "https://fosstodon.org/@pyOpenSci",
            "icon": "fa-brands fa-mastodon",
        },
    ],
    "logo": {
        "text": "Python Package Guide",
        "image_dark": "logo.png",
        "alt_text": "pyOpenSci Python Package Guide. The pyOpenSci logo is blue and yellow following the Python logo",
    },
    "header_links_before_dropdown": 4,
    "use_edit_page_button": True,
    "show_toc_level": 1,
    # "navbar_align": "left",  # [left, content, right] For testing that the navbar items align properly
    "github_url": "https://github.com/pyopensci/python-package-guide",
    "twitter_url": "https://twitter.com/pyopensci",
    "footer_items": ["copyright"],
}

html_theme_options["analytics"] = {
    "google_analytics_id": "UA-141260825-1",
}

html_context = {
    "github_user": "pyopensci",
    "github_repo": "python-package-guide",
    "github_version": "main",
}

# Add analytics to furo theme
gtagjs_ids = [
    "UA-141260825-1",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    ".github",
    ".nox",
    "README.md",
]

# For sitemap
html_baseurl = "https://www.pyopensci.org/package-review-guide/"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_css_files = ["pyos.css"]
html_title = "pyOpenSci Python Packaging Guide"
html_js_files = ["matomo.js"]
html_logo = "images/logo/logo.png"
