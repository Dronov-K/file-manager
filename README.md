# Description
A cross-platform Python utility to automatically organize and sort files into
structured directories based on configurable rules.
Supports macOS, Windows, and Docker environments, with type-safe configuration
using Pydantic and flexible path handling via pathlib.
Easily installable as a package or used as a CLI tool.

# Project structure

```
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
```
**Configuring TARGET_FOLDER on macOS**

In the .env file, specify the folder where the script will work:

```env
TARGET_FOLDER=~/Desktop/tmp
LOG_FILE=~/Desktop/app.log
SORT_RULES_FILE=sort_rules.yaml
DATE_FORMAT=%Y-%m-%d
CREATE_DATE_FOLDERS=false
SKIP_HIDDEN=true
DRY_RUN=false
BACKUP_FILES=false
```

🔹 Important: use ~ to denote your home directory. Python automatically expands ~ via Path.expanduser(). There is no need to use ${HOME}.

**macOS Specifics**

macOS protects folders like Downloads, Documents, and sometimes Desktop via the TCC (Transparency, Consent, and Control) system. Even if the folder exists, the Python script may encounter:

```makefile
PermissionError: [Errno 1] Operation not permitted
```


If this happens:

1. **Check if the folder exists:**
Make sure the folder actually exists:

```bash
ls ~/Downloads
```

2. **Grant permissions to your application:**

Open System Settings → Privacy & Security → Files and Folders.

Locate your application (IDE or Terminal) and enable access to the required folders.

3. **Alternative folders for testing:**

For temporary work or testing, use folders without macOS protection:

```bash
~/Desktop/tmp
~/Projects/tmp
```


**Handling Errors in Code**

The script safely handles paths via Pydantic Settings and Path.expanduser().
If a folder is inaccessible, it’s recommended to either check folder permissions beforehand or select an alternative folder.
