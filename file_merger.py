import os

file_paths = [
    os.path.join(os.getcwd(), "1.txt"),
    os.path.join(os.getcwd(), "2.txt"),
    os.path.join(os.getcwd(), "3.txt")
]
files_data = {}

for file_path in file_paths:
    key = os.path.basename(file_path)
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = [line.rstrip("\n") for line in f]
        files_data[key] = {"lines": lines, "count": len(lines)}
        print(f"✅ Прочитан файл: {key} ({len(lines)} строк)")
    except FileNotFoundError:
        print(f"⚠️ Файл не найден: {file_path}")
    except PermissionError:
        print(f"❌ Нет прав на чтение файла: {file_path}")
    except UnicodeDecodeError:
        print(f"⚠️ Ошибка кодировки в файле: {file_path} (проверь, что это UTF-8)")
    except Exception as e:
        print(f"❌ Непредвиденная ошибка при чтении {file_path}: {e}")

if not files_data:
    print("Нет данных для обработки — остановимся.")
else:
    sorted_files = sorted(files_data.items(), key=lambda x: x[1]["count"])
    output_path = os.path.join(os.getcwd(), "all_files.txt")

    with open(output_path, "w", encoding="utf-8") as out_f:
        for name, data in sorted_files:
            out_f.write(f"{name}\n{data['count']}\n")
            for line in data["lines"]:
                out_f.write(line + "\n")
            out_f.write("\n")

    print(f"\n✅ Данные записаны в {output_path}")

    # Вывод результата
    with open("all_files.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line.strip())