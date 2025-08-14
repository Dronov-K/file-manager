# Description
A cross-platform Python utility to automatically organize and sort files into
structured directories based on configurable rules.
Supports macOS, Windows, and Docker environments, with type-safe configuration
using Pydantic and flexible path handling via pathlib.
Easily installable as a package or used as a CLI tool.

# Project structure

file-manager/
│
├── src/
│   ├── sorter.py            # Sorting logic
│   ├── cli.py               # Argument parser
│   └── utils.py             # Auxiliary functions (categories, backups)
│
├── tests/
│   ├── test_config.py       #
│   └── test_logger.py       #
│
├── config.py                # Configuration via Pydantic
├── logger.py                # Logging
├── main.py                  # Entry point
├── sort_rules.yaml          # Categories and extensions
├── .env                     # Default settings
├── .pre-commit-config.yaml  #
├── pyproject.toml           #
└── Dockerfile               # Docker Image
