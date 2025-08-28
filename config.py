import logging
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

from logger import configure_logging

configure_logging()
logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / ".env"


class Settings(BaseSettings):
    """
    Application configuration loaded from environment variables or a `.env` file.

    Attributes:
        target_folder (Path): Path to the target folder where files will be processed.
        log_file (Path): Path to the log file for writing logs.
        sort_rules_file (Path): Path to the sorting rules configuration file.
        date_format (str): Date format string for naming folders or processing dates.
        create_date_folders (bool): Whether to create folders based on the date format.
        skip_hidden (bool): Whether to skip hidden files and directories.
        dry_run (bool): If True, no actual changes will be made (simulation mode).
        backup_files (bool): Whether to create backups before making changes.
    """

    model_config = SettingsConfigDict(env_file=ENV_PATH, env_file_encoding="utf-8")

    target_folder: Path
    log_file: Path
    sort_rules_file: Path

    date_format: str
    create_date_folders: bool = False
    skip_hidden: bool = True
    dry_run: bool = False
    backup_files: bool = False

    def model_post_init(self, __context) -> None:
        """
        Post-initialization hook to resolve and normalize paths..

        Ensures that:
            - target_folder, log_file, and sort_rules_file are absolute paths
            - ~ in paths is expanded to the user's home directory
        """
        self.target_folder = Path(self.target_folder).expanduser().resolve()
        self.log_file = Path(self.log_file).expanduser().resolve()
        self.sort_rules_file = (BASE_DIR / self.sort_rules_file).resolve()

        logger.debug("Resolved target_folder: %s", self.target_folder)
        logger.debug("Resolved log_file: %s", self.log_file)
        logger.debug("Resolved sort_rules_file: %s", self.sort_rules_file)


def get_settings() -> Settings:
    """
    Load application settings from environment variables or `.env` file.

    :return: Settings: A fully initialized Settings instance.
    """

    logger.info("Using .env or system environment for settings.")
    return Settings()


settings = get_settings()

if __name__ == "__main__":
    print(settings.target_folder)
    print(settings.log_file)
    print(settings.date_format)
    print(settings.sort_rules_file)
    print(settings.backup_files)
