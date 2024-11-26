from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict


@dataclass(frozen=True)
class Https:
    base_url: str = "https://ru.wikipedia.org"
    url: str = base_url + "/w/index.php"
    base_params: Dict[str, str] = field(
        default_factory=lambda: {"title": "Категория:Животные_по_алфавиту"}
    )
    search_letters: str = "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЭЮЯ"


@dataclass(frozen=True)
class Settings:
    base_path: Path = Path(__file__).parent.parent
    base_dir_for_csv_files: Path = base_path / "data" / "csv"
    csv_file_name: str = "beasts.csv"
    https: Https = Https()
