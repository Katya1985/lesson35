import os
import time
directory = "."
for root, dirs, files in os.walk(directory):
    for file in files:
        print(os.path.join(root, file))


os.path.join(directory)
current_dir = os.getcwd()
for file_name in directory:
    file_path = os.path.join(current_dir, file_name)
    print(file_path)


# Путь к файлу/directory
path = "myfile.txt"

ti_c = os.path.getctime(path)
ti_m = os.path.getmtime(path)

c_ti = time.ctime(ti_c)
m_ti = time.ctime(ti_m)




file_size = os.path.getsize('example.txt')


os.path.dirname(os.path.realpath(__file__))




# for root, dirs, files in os.walk(directory):
#   for file in files:
#     filepath = ?
#     filetime = ?
#     formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
#     filesize = ?
#     parent_dir = ?
print(f'Обнаружен файл: {file}, Путь: {file_path}, Размер: {file_size} байт, Время изменения: {m_ti}, Родительская директория: {parent_dir}')