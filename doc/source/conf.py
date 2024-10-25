# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

project = 'Examen'
copyright = '2024, Venera'
author = 'Venera'
release = '25/10/24'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',   # Génère automatiquement la documentation à partir des docstrings Python (par ex. palin.py)
    'sphinx.ext.napoleon',  # Supporte les styles de docstrings NumPy et Google
    'sphinx.ext.viewcode',  # Ajoute des liens vers le code source dans la documentation générée
    'sphinx.ext.intersphinx',  # Permet de créer des liens vers la documentation d'autres projets externes
    "sphinx_autodoc_typehints"  # Inclut automatiquement les annotations de types Python dans la documentation
]


templates_path = ['_templates']
exclude_patterns = []
add_module_names = False
language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
napoleon_google_docstring = True