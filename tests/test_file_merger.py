"""Тесты для модуля file_merger."""

import sys
from pathlib import Path

ROOT_PATH = str(Path(__file__).resolve().parent.parent)
if ROOT_PATH not in sys.path:
    sys.path.insert(0, ROOT_PATH)

from file_merger import merge_files_sorted  # noqa: E402,C0413


def test_basic_merge(tmp_path):
    """Проверяет базовое слияние файлов."""
    f1 = tmp_path / "1.txt"
    f2 = tmp_path / "2.txt"
    f3 = tmp_path / "3.txt"

    f1.write_text("A\nB\n", encoding="utf-8")
    f2.write_text("X\n", encoding="utf-8")
    f3.write_text("L1\nL2\nL3\nL4\n", encoding="utf-8")

    output = tmp_path / "all_files.txt"
    result = merge_files_sorted([str(f1), str(f2), str(f3)], str(output))

    assert output.exists()
    assert len(result) == 3
    assert result["2.txt"]["count"] == 1
    assert result["1.txt"]["count"] == 2
    assert result["3.txt"]["count"] == 4

    content = output.read_text(encoding="utf-8").splitlines()
    assert content[0] == "2.txt"
    assert int(content[1]) == 1


def test_missing_file_handled(tmp_path):
    """Проверяет обработку отсутствующих файлов."""
    f1 = tmp_path / "1.txt"
    missing = tmp_path / "missing.txt"
    f2 = tmp_path / "2.txt"

    f1.write_text("A\n", encoding="utf-8")
    f2.write_text("X\nY\nZ\n", encoding="utf-8")

    output = tmp_path / "all_files.txt"
    result = merge_files_sorted([str(missing), str(f1), str(f2)], str(output))

    assert "missing.txt" not in result
    assert len(result) == 2
    assert output.exists()


def test_empty_input_list(tmp_path):
    """Проверяет поведение при пустом списке файлов."""
    output = tmp_path / "all_files.txt"
    result = merge_files_sorted([], str(output))
    assert not output.exists()
    assert not result
