from pathlib import Path

from task2.solution.settings.settings import Settings

base_path: Path = Path(__file__).parent
base_dir_for_csv_files: Path = base_path / "t_data" / "csv"
csv_file_name: str = "t_beasts.csv"

t_settings = Settings(
    base_path=base_path,
    base_dir_for_csv_files=base_dir_for_csv_files,
    csv_file_name=csv_file_name,
)
