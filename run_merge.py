import os
from file_merger import merge_files_sorted

if __name__ == "__main__":
    file_paths = [
        os.path.join(os.getcwd(), "1.txt"),
        os.path.join(os.getcwd(), "2.txt"),
        os.path.join(os.getcwd(), "3.txt")
    ]
    output_path = os.path.join(os.getcwd(), "all_files.txt")

    result = merge_files_sorted(file_paths, output_path)

    if not result:
        print("Нет данных для обработки — остановимся.")
    else:
        print(f"\n✅ Данные записаны в {output_path}")
        with open(output_path, "r", encoding="utf-8") as file:
            for line in file:
                print(line.strip())