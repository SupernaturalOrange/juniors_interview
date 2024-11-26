import csv

import pytest

from task2.solution.settings.settings import Settings
from task2.solution.tools.csv_tools import write_csv_file


@pytest.mark.csv_tools
def test_write_csv_file_func(settings: Settings) -> None:
    """
    Тестируем функцию write_csv_file.
    Проверим: сохраняются ли в csv файл передаваемые данные.

    :param settings: Изменённые настройки для приложения.
    :return: None.
    """

    # Проверим, что изначально не существует папки с файлом
    path = settings.base_dir_for_csv_files
    assert not path.exists()

    # Пробуем записать файл.
    data = [dict(name="Вася", age=20), dict(name="Петя", age=24)]
    write_csv_file(settings, data)

    file_path = path / settings.csv_file_name
    assert file_path.exists()

    # Проверяем что записано
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        assert "name" in header
        assert "age" in header
        data_list = [item for row in reader for item in row]

        assert "Вася" in data_list
        assert "20" in data_list
        assert "Петя" in data_list
        assert "24" in data_list
