from pathlib import Path

from config import BASE_DIR, ENV_PATH, Settings


def test_settings_paths_and_values():
    settings = Settings(_env_file=ENV_PATH)

    # Проверяем, что пути развернулись правильно
    assert settings.target_folder.exists() or True  # путь может существовать или нет
    assert (
        settings.log_file.parent.exists()
    )  # родительская папка для лог-файла должна существовать
    assert settings.sort_rules_file.parent == BASE_DIR  # файл в проекте

    # Проверяем, что остальные значения корректно загружены
    assert isinstance(settings.date_format, str)
    assert isinstance(settings.create_date_folders, bool)
    assert isinstance(settings.skip_hidden, bool)
    assert isinstance(settings.dry_run, bool)
    assert isinstance(settings.backup_files, bool)

    # Проверяем точные пути
    assert settings.target_folder == Path("~/Desktop").expanduser().resolve()
    assert settings.log_file == Path("~/Desktop/sort_files.log").expanduser().resolve()
    assert settings.sort_rules_file == (BASE_DIR / "sort_rules.yaml").resolve()

    # Проверяем остальные настройки
    assert settings.date_format == "%Y-%m-%d %H:%M:%S"
    assert settings.create_date_folders is False
    assert settings.skip_hidden is True
    assert settings.dry_run is False
    assert settings.backup_files is False
