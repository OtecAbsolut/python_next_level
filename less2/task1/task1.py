# 1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
# info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
# Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и
# считывание данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь
# значения параметров «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
# Значения каждого параметра поместить в соответствующий список. Должно получиться четыре списка — например,
# os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции создать главный список
# для хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета в виде списка:
# «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
# Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
# Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
# В этой функции реализовать получение данных через вызов функции get_data(),
# а также сохранение подготовленных данных в соответствующий CSV-файл;
# Проверить работу программы через вызов функции write_to_csv().
import re
import csv
import pprint
from collections import defaultdict
import os

def get_data():
    # шаблоны с регулярками
    patterns = {
        'Изготовитель системы': r'^Изготовитель системы: *',
        'Название ОС': r'^Название ОС: *',
        'Код продукта': r'^Код продукта: *',
        'Тип системы': r'^Тип системы: *'
    }
    # Будущий список словарей будущих данных, который я объединил с main_data, один словарь будет содержать в себе
    # данные из одного файлика, и количество словарей будет равно количеству файлов
    data = []
    i = 0
    while True:
        i += 1
        try:
            # Открываем файлики по очереди, с виндовой кодировкой
            with open(f'{os.getcwd()}/task1/info_{i}.txt', 'r', encoding='windows-1251') as file:
                # объявляем словарь для данных из файла, словарь из модуля коллекций,
                # чтобы не объявляеть заранее структуру ключей и значений.
                data_dict = defaultdict()
                # Перебираем строки по очереди из файлоы
                for string in file:
                    # В каждой строке проверяем если совпадаение с патернами
                    for key, pattern in patterns.items():
                        if re.search(pattern, string):
                            value = re.split(pattern, string)[1][:-1]
                            data_dict[key] = value
                            break
                data.append(data_dict)
        except FileNotFoundError:
            # Если выпадаем с ошибкой значит кончились файды в папки и мы идем дальше
            print(f'Было обработанно {i-1} файлов')
            break
    return data


def write_to_csv(path):
    all_data = get_data()
    with open(path, 'w', newline='') as file:
        for data in all_data:
            keys = list(data.keys())
            writer = csv.DictWriter(file, delimiter=',', fieldnames=keys)
            writer.writerow(data)


if __name__ == '__main__':
    write_to_csv('task1/result.csv')
    print(f'Обработка файлов успешно выполненна')
