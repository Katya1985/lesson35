import os
import time
directory = "."
for root, dirs, files in os.walk(directory): # os.walk для обхода каталога
    for file in files:
        print(os.path.join(root, file))

os.path.join(directory) # os.path.join для формирования полного пути к файлам.
current_dir = os.getcwd()
for file_name in directory:
    file_path = os.path.join(current_dir, file_name)
    print(file_path)

# Путь к файлу/directory    # os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла
file_time = os.path.getmtime(file_path)
formatted_time = time.strftime(f'%d.%m.%Y, %H:%M',  time.localtime(file_time))


file_size = os.path.getsize(file_path) # os.path.getsize для получения размера файла

os.path.dirname(os.path.realpath(__file__)) # os.path.dirname для получения родительской директории файла
parent_dir = os.path.dirname(file_path)


print(f'Обнаружен файл: {file}, Путь: {file_path}, Размер: {file_size} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')