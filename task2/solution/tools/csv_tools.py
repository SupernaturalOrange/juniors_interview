import csv
from typing import Any, Dict, List

from task2.solution.settings.settings import Settings


def write_csv_file(settings: Settings, data: List[Dict[str, Any]]) -> None:
    """
    Функция запишет данные в csv файл, который указан в настройках.

    :param settings: Настройки (экземпляр класса Settings).
    :param data: Список из словарей.
    :return: None.
    """
    if not isinstance(data, list):
        raise ValueError("Передавать нужно список.")
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Список должен состоять из словарей")
    path = settings.base_dir_for_csv_files
    path.mkdir(parents=True, exist_ok=True)
    file_path = path / settings.csv_file_name
    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = [name for name in data[0].keys()]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
