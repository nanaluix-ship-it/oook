"""Скрипт для запуска слияния файлов."""

import sys
from pathlib import Path

ROOT_PATH = str(Path(__file__).resolve().parent)
if ROOT_PATH not in sys.path:
    sys.path.insert(0, ROOT_PATH)

from file_merger import merge_files_sorted  # noqa: E402,C0413


def main() -> None:
    """Запускает слияние файлов."""
    input_files = ["data/1.txt", "data/2.txt", "data/3.txt"]
    output_file = "output/all_files.txt"

    print(f"Начинаем слияние файлов: {input_files}")
    result = merge_files_sorted(input_files, output_file)
    print(f"Готово. Обработано файлов: {len(result)}")


if __name__ == "__main__":
    main()
