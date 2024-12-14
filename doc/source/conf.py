import os
import sys
## Le chemin depuis conf.py vers les fichiers .py que l'on veut documenter.
sys.path.insert(0, os.path.abspath('../../'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Jeu_Pendu'
copyright = '2024, Venera'
author = 'Venera'
release = '2024'

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
napoleon_numpy_docstring = True 
language = 'fr'
add_module_names = False 
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
