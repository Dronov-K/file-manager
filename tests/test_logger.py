import logging
from pathlib import Path

import pytest

from logger import configure_logging


@pytest.fixture
def temp_log_file(tmp_path: Path) -> Path:
    """Create a temporary log file path."""
    log_file = tmp_path / "logs" / "test.log"
    return log_file


def test_configure_logging_creates_log_file_and_writes(temp_log_file: Path):
    """
    Test that configure_logging:
      - Creates the log file directory
      - Writes log messages to the file
    """
    configure_logging(log_file=temp_log_file, level=logging.DEBUG)

    assert temp_log_file.parent.exists(), "Log file directory was not created."

    logger = logging.getLogger("test_logger")
    test_message = "Hello, logging!"
    logger.debug(test_message)

    for handler in logger.handlers:
        handler.flush()

    assert temp_log_file.exists(), "Log file was not created."
    content = temp_log_file.read_text(encoding="utf-8")
    assert test_message in content, "Log file does not contain the logged message."
