from pathlib import Path


def create_target_folder(path: Path) -> None:
    """Ensure that the target folder exists."""
    path.mkdir(parents=True, exist_ok=True)
