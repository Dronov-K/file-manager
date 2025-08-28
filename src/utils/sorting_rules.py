import logging

import yaml

from config import settings
from logger import configure_logging

configure_logging()
logger = logging.getLogger(__name__)


def load_sorting_rules() -> dict:
    path = settings.sort_rules_file

    if not path.exists():
        logger.error(f"Sorting rules file not found: {path}")
        raise FileNotFoundError(f"Sorting rules file not found: {path}")

    with open(path, "r", encoding="utf-8") as file:
        logger.info(f"Sort rules file found and opened: {path}")
        rules = yaml.safe_load(file)

    for category, config in rules.items():
        config["extensions"] = [
            ext.lower().lstrip(".") for ext in config.get("extensions", [])
        ]
        config["mime"] = [m.lower() for m in config.get("mime", [])]

    return rules
