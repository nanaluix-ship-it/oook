"""Модуль для слияния текстовых файлов и сортировки их содержимого по количеству строк."""

import os
from typing import Dict, List, Any


def merge_files_sorted(file_paths: List[str], output_path: str) -> Dict[str, Any]:
    """
    Читает файлы, сортирует их по числу строк и записывает результат в output_path.

    Возвращает словарь с данными: {filename: {"lines": [...], "count": N}}
    Файлы, которые не удалось прочитать, пропускаются.
    """
    files_data: Dict[str, Any] = {}

    for file_path in file_paths:
        key = os.path.basename(file_path)
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                lines = [line.rstrip("\n") for line in f]
            files_data[key] = {"lines": lines, "count": len(lines)}
        except FileNotFoundError:
            continue
        except OSError as e:
            print(f"Ошибка чтения файла {file_path}: {e}")
            continue

    if not files_data:
        return files_data

    sorted_items = sorted(files_data.items(), key=lambda x: x[1]["count"])

    with open(output_path, "w", encoding="utf-8") as out_f:
        for name, data in sorted_items:
            out_f.write(f"{name}\n{data['count']}\n")
            for line in data["lines"]:
                out_f.write(line + "\n")
            out_f.write("\n")

    return files_data
