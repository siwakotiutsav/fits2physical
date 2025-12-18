import os
import sys
sys.path.insert(0, os.path.abspath('..'))  # make f2p importable

# Project info
project = 'fits2physical'
author = 'Utsav Siwakoti'
release = '0.1'

# Sphinx extensions
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']

# Paths
templates_path = ['_templates']
exclude_patterns = []

# HTML output
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
