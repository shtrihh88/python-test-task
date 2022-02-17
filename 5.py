import os
import re


def traver_folders(root_dir: str, list_files=None):
    """Получаем список не пустых файлов"""
    if list_files is None:
        list_files = []
    for lists in os.listdir(root_dir):
        path = os.path.join(root_dir, lists)
        if os.path.isdir(path):
            traver_folders(path, list_files)
        else:
            if os.path.getsize(path):
                list_files.append(path)

    return list_files


def get_email(list_files: list):
    """Получение списка email адресов"""
    email_list = []
    pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"
    if list_files is None:
        return email_list
    for file in list_files:
        with open(file, 'r') as file_text:
            for line in file_text.read().split('\n'):
                if re.match(pattern, line):
                    email_list.append(line)

    return email_list


def task1():
    # в папке test найти все файлы filenames вывести колличество
    count = 0
    for root, dirs, files in os.walk('.'):
        for name in files:
            if 'filenames' == name.split('.')[0]:
                count += 1
    print(count)


def task2():
    # в папке test найти все email адреса записанные в файлы
    result = get_email(traver_folders('.'))
    for email in result:
        print(email)


def main():
    os.chdir('test')
    task1()
    task2()
    # дополнительно: придумать над механизм оптимизации 2-й задачи (используя threading)


if __name__ == '__main__':
    main()
