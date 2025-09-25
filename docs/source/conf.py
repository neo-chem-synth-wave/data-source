""" The ``docs.source`` directory ``conf`` script. """

from os.path import abspath


project = "data-source"
author = "NeoChemSynthWave"
release = "2025.9.1"

extensions = ["autoapi.extension", ]

autoapi_type = "python"
autoapi_dirs = [abspath("../../data_source"), ]
autoapi_add_toctree_entry = True
autoapi_keep_files = True
autoapi_member_order = "bysource"
autoapi_python_class_content = "both"
autoapi_options = [
    "members",
    "undoc-members",
    "private-members",
    "special-members",
    "show-inheritance",
    "show-module-summary",
    "imported-members",
]

html_theme = "alabaster"
