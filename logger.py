import logging
from dataclasses import dataclass
from pathlib import Path

from colorama import Fore, Style, init

# Initializing colorama (for Windows really important)
init(autoreset=True)


class ColorFormatter(logging.Formatter):
    """
    A custom logging formatter that adds color to log messages based on severity level.

    Colors are applied using the `colorama` library:
    - DEBUG and INFO: Green
    - WARNING: Yellow
    - ERROR and CRITICAL: Red (CRITICAL is also bold)

    This formatter enhances readability, especially in terminal output.
    """

    COLORS = {
        "DEBUG": Fore.GREEN,
        "INFO": Fore.GREEN,
        "WARNING": Fore.YELLOW,
        "ERROR": Fore.RED,
        "CRITICAL": Fore.RED + Style.BRIGHT,
    }

    def format(self, record: logging.LogRecord) -> str:
        """
        Apply color formatting to a log record based on its severity level.

        :param record: A log record containing all relevant log message information.
        :return: A string with ANSI color codes applied, ready for terminal output.
        """
        color = self.COLORS.get(record.levelname, "")
        message = super().format(record)

        return f"{color}{message}{Style.RESET_ALL}"


@dataclass(frozen=True)
class LogConfig:
    """
    Immutable configuration for logging format and date format.

    Attributes:
        format (str): Format string for log messages.
        datefmt (str): Date format string for timestamps in logs.
    """

    format: str = (
        "[%(asctime)s.%(msecs)03d] %(module)-30s:%(lineno)3d "
        "%(levelname)-7s - %(message)s"
    )
    datefmt: str = "%Y-%m-%d %H:%M:%S"


def configure_logging(
    level: int = logging.INFO,
    log_file: Path | None = None,
    config: LogConfig = LogConfig(),
) -> None:
    """
    Configure logging with colored console output and optional file logging.

    :param level: Logging level (e.g., logging.INFO, logging.DEBUG).
    :param log_file: Optional Path to log file.
    :param config: An instance of LogConfig containing format and date format settings.
            Defaults to a new LogConfig instance.

    :return: None
    """
    console_handler = logging.StreamHandler()
    console_formatter = ColorFormatter(fmt=config.format, datefmt=config.datefmt)
    console_handler.setFormatter(console_formatter)
    handlers = [console_handler]

    # Optional file handler (no colors)
    if log_file:
        log_file.parent.mkdir(parents=True, exist_ok=True)  # Ensure directory exists
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_formatter = logging.Formatter(fmt=config.format, datefmt=config.datefmt)
        file_handler.setFormatter(file_formatter)
        handlers.append(file_handler)

    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    root_logger.handlers.clear()

    for handler in handlers:
        root_logger.addHandler(handler)
