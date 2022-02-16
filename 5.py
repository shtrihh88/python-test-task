import os


def task1():
    # в папке test найти все файлы filenames вывести колличество
    count = 0
    os.chdir('test')
    for root, dirs, files in os.walk('.'):
        for name in files:
            if 'filenames' == name.split('.')[0]:
                count += 1
    print(count)


def task2():
    # в папке test найти все email адреса записанные в файлы
    pass


def main():
    task1()
    task2()
    # дополнительно: придумать над механизм оптимизации 2-й задачи (используя threading)


if __name__ == '__main__':
    main()
