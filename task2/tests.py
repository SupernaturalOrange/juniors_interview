import pytest
from solution import extract_first_letter, save_json, save_csv

def test_extract_first_letter():
    assert extract_first_letter("Японский полоз") == "П"
    assert extract_first_letter("Обыкновенный ёрш") == "Ё"
    assert extract_first_letter("Abactochromis labrosus") == "L"
    assert extract_first_letter("Ёргия") == "Ё"

def test_save_json(tmp_path):
    data = ["Японский полоз", "Обыкновенный ёрш"]
    filepath = tmp_path / "test.json"
    save_json(filepath, data)
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
    assert "Японский полоз" in content
    assert "Обыкновенный ёрш" in content

def test_save_csv(tmp_path):
    data = {"А": 10, "Б": 20, "Ё": 5}
    filepath = tmp_path / "test.csv"
    save_csv(filepath, data)
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
    assert "А,10" in content
    assert "Ё,5" in content
