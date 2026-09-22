import sys
from pathlib import Path

# Добавляем корень проекта в путь поиска модулей, чтобы Python видел file_merger.py
root_path = Path(__file__).resolve().parent.parent
if str(root_path) not in sys.path:
    sys.path.insert(0, str(root_path))

from file_merger import merge_files_sorted

def test_basic_merge(tmp_path):
    # Создаём тестовые файлы внутри tmp_path (это безопасно и для CI)
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

    # Проверяем, что в выходном файле порядок правильный: 2.txt, 1.txt, 3.txt
    content = output.read_text(encoding="utf-8").splitlines()
    assert content[0] == "2.txt"
    assert int(content[1]) == 1


def test_missing_file_handled(tmp_path):
    f1 = tmp_path / "1.txt"
    missing = tmp_path / "missing.txt"  # этого файла не будет
    f2 = tmp_path / "2.txt"

    f1.write_text("A\n", encoding="utf-8")
    f2.write_text("X\nY\nZ\n", encoding="utf-8")

    output = tmp_path / "all_files.txt"
    result = merge_files_sorted([str(missing), str(f1), str(f2)], str(output))

    assert "missing.txt" not in result
    assert len(result) == 2
    assert output.exists()


def test_empty_input_list(tmp_path):
    output = tmp_path / "all_files.txt"
    result = merge_files_sorted([], str(output))
    assert not output.exists()
    assert result == {}