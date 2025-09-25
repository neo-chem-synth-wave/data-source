# -- Project info -------------------------------------------------------------
project = "data-source"
author = "NeoChemSynthWave"
release = "2025.9.1"

# -- Extensions ---------------------------------------------------------------
extensions = [
    "autoapi.extension",  # Sphinx AutoAPI: static parsing (no imports)
]

# AutoAPI: point to your package directory (adjust if needed)
# This path is from docs/source → repo root → package folder
import os
autoapi_type = "python"
autoapi_dirs = [os.path.abspath("../../data_source")]  # <--- your package path

# Recommended options for a rich API
autoapi_add_toctree_entry = True
autoapi_keep_files = True                # keeps generated .rst for debugging
autoapi_member_order = "bysource"        # preserve source order
autoapi_python_class_content = "both"    # class docstring + __init__ docstring
autoapi_options = [
    "members",
    "undoc-members",
    "private-members",        # drop if you don’t want _private in docs
    "special-members",        # includes __call__, __iter__, etc.
    "show-inheritance",
    "show-module-summary",
    "imported-members",
]

# -- PDF via rinohtype -------------------------------------------------------
# Build the PDF starting from the root index.rst
# (startdocname, targetname, title, author)
rinoh_documents = [
    ("index", "data-source", "data-source", author),
]

# -- HTML --------------------------------------------------------------------
html_theme = "alabaster"
