from pathlib import Path
# Создать папку 'files'  в текущей папки
file_dir_path = Path('files')
# Если папка есть Python не сгенирует ошибку и не создаст и не перезапишет папку
file_dir_path.mkdir(exist_ok=True)

# Добавь два файла 'first.txt' и 'second.txt' в эту папку и запиши в них по 2-3 строки текста
first_file = file_dir_path / 'fisrt.txt'
second_file = file_dir_path / 'second.txt'

with open(first_file, 'w') as f:
    f.write('First line\n')
    f.write('Second line\n')

with open(second_file, 'w') as f:
    lines = [
        'First line in the second file',
        'Second line in the second file',
        'Last line in the second file'
    ]
    for line in lines:
        f.write(line + '\n')

# Прочитать все строки первого файла
with open(first_file) as f:
    print(f.read())

# Прочитай строки второго файла одна за другой
with open(second_file) as f:
    # ВАРИАНТ 1
    for line in f:
        print(line.strip())
    # ВАРИАНТ 2
    # while True:
    #     line = f.readline()
    #     if not line:
    #         break
    #     print(line.strip())  # Метод strip убирает лишнии пробелы и строки.

# Удалить оба файла
first_file.unlink()
second_file.unlink()

# Удалить папку 'files'
file_dir_path.rmdir()
