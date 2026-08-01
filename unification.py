import os

file_paths = os.path.join(os.getcwd(), "1.txt")
lines = []

with open(file_paths, "r", encoding="utf-8") as f:
    for line in f:
        if line != " " and line != "\n":
            lines.append(line.strip())
    quantity = len(lines)
    # print(lines)
    # print(quantity)

file_paths_2 = os.path.join(os.getcwd(), "2.txt")
lines2 = []

with open(file_paths_2, "r", encoding="utf-8") as file:
    for line in file:
        if line != " " and line != "\n":
            lines2.append(line.strip())
    quantity2 = len(lines2)
    # print(lines2)
    # print(quantity2)

file_paths_3 = os.path.join(os.getcwd(), "3.txt")
lines3 = []

with open(file_paths_3, "r", encoding="utf-8") as file3:
    for line in file3:
        if line != " " and line != "\n":
            lines3.append(line.strip())
    quantity3 = len(lines3)
    # print(lines3)
    # print(quantity3)

with open("all_files.txt", "w", encoding="utf-8") as file:
    if quantity < quantity2 and quantity < quantity3:
        if quantity2 < quantity3:
            file.write(f'1.txt\n{quantity}\n{("\n").join(lines)}\n2.txt'
                       f'\n{quantity2}\n{("\n").join(lines2)}\n3.txt'
                       f'\n{quantity3}\n{("\n").join(lines3)}')
        else:
            file.write(f'1.txt\n{quantity}\n{("\n").join(lines)}\n3.txt'
                       f'\n{quantity3}\n{("\n").join(lines3)}\n2.txt'
                       f'\n{quantity2}\n{("\n").join(lines2)}')
    elif quantity2 < quantity and quantity2 < quantity3:
        if quantity < quantity3:
            file.write(f'2.txt\n{quantity2}\n{("\n").join(lines2)}\n'
                       f'1.txt\n{quantity}\n{("\n").join(lines)}\n'
                       f'3.txt\n{quantity3}\n{("\n").join(lines3)}')
        else:
            file.write(f'2.txt\n{quantity2}\n{("\n").join(lines2)}\n'
                       f'3.txt\n{quantity3}\n{("\n").join(lines3)}\n'
                       f'1.txt\n{quantity}\n{("\n").join(lines)}')
    elif quantity3 < quantity and quantity3 < quantity2:
        if quantity < quantity2:
            file.write(f'3.txt\n{quantity3}\n{("\n").join(lines3)}\n'
                       f'1.txt\n{quantity}\n{("\n").join(lines)}\n'
                       f'2.txt\n{quantity2}\n{("\n").join(lines2)}')
        else:
            file.write(f'3.txt\n{quantity3}\n{("\n").join(lines3)}\n'
                       f'2.txt\n{quantity2}\n{("\n").join(lines2)}\n'
                       f'1.txt\n{quantity}\n{("\n").join(lines)}')

with open("all_files.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

