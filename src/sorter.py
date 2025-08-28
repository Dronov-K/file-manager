import logging
import shutil

from config import settings
from logger import configure_logging
from src.utils.categorization import categorize_file
from src.utils.sorting_rules import load_sorting_rules
from src.utils.target_folder import create_target_folder

configure_logging()
logger = logging.getLogger(__name__)


def sort_files() -> None:
    """
    Sort files according to rules.
    """
    target_folder = settings.target_folder
    rules = load_sorting_rules()

    for item in target_folder.iterdir():
        if item.is_dir():
            continue
        if settings.skip_hidden and item.name.startswith("."):
            continue

        # Determine category and destination folder
        folder_name = categorize_file(item, rules)
        destination_folder = target_folder / folder_name
        create_target_folder(destination_folder)

        destination_path = destination_folder / item.name

        # Backup if enabled
        if settings.backup_files:
            backup_path = destination_path.with_suffix(
                destination_path.suffix + ".backup"
            )
            shutil.copy2(item, backup_path)
            logger.info(f"Backup created: {backup_path}")

        # Move file or dry-run
        if settings.dry_run:
            logger.info(f"[DRY RUN] {item.name} -> {destination_folder}")
        else:
            try:
                shutil.move(str(item), str(destination_path))
                logger.info(f"{item.name} -> {destination_folder}")
            except Exception as e:
                logger.error(f"Error moving {item.name}: {e}")
