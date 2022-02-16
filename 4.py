import json
import sys


def some_func(dicts: dict, param: str, list_dict=[]):
    if isinstance(dicts, dict):
        for key, value in dicts.items():
            if not isinstance(value, dict):
                if key == param:
                    list_dict.append((key, value))
            some_func(value, param, list_dict)
    elif isinstance(dicts, list):
        for elem in dicts:
            some_func(elem, param, list_dict)

    return list_dict


def count_questions(data: dict):
    # вывести количество вопросов (questions)
    result = some_func(data, 'questions', [])
    count = 0
    for elem in result:
        count += len(elem[1])
    print(count)


def print_right_answers(data: dict):
    # вывести все правильные ответы (correct_answer)
    result = some_func(data, 'correct_answer', [])
    for elem in result:
        print(elem[1])


def print_max_answer_time(data: dict):
    # вывести максимальное время ответа (time_to_answer)
    max_time = 0
    result = some_func(data, 'time_to_answer', [])
    for elem in result:
        if elem[1] > max_time:
            max_time = elem[1]
    print(max_time)


def main(args):
    with open(args, 'r') as file:
        data = json.load(file)  # загрузить данные из test.json файла
    count_questions(data)
    print_right_answers(data)
    print_max_answer_time(data)


if __name__ == '__main__':
    # передать имя файла из аргументов командной строки
    main(sys.argv[1])
