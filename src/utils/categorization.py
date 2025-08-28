import logging
import mimetypes
from pathlib import Path

from logger import configure_logging

configure_logging()
logger = logging.getLogger(__name__)


def categorize_file(file_path: Path, rules: dict) -> str:
    """
    Determine a target folder for a given file based on MIME type and extension.

    :param file_path: Path to the file to categorize
    :param rules: Sorting rules loaded from YAML
    :return: target_folder
    """
    file_path = Path(file_path)
    if not file_path.exists() or not file_path.is_file():
        logger.warning(f"File not found or is not a file: {file_path}")
        return rules.get("other", {}).get("target", "Other")

    ext = file_path.suffix.lower().lstrip(".")
    # Guess MIME type
    mime_type, _ = mimetypes.guess_type(file_path)

    if mime_type:
        mime_type = mime_type.lower()
        for category, config in rules.items():
            if mime_type in config.get("mime", []):
                return config.get("target", category)

    for category, config in rules.items():
        if ext in config.get("extensions", []):
            return config.get("target", category)

    return rules.get("other", {}).get("target", "Other")
