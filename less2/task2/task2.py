# -*- coding: utf-8 -*-

# 2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
# Написать скрипт, автоматизирующий его заполнение данными. Для этого:
# Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
# цена (price), покупатель (buyer), дата (date). Функция должна предусматривать
# запись данных в виде словаря в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
# Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.

import json
import datetime
import os

# with open('orders.json', 'r') as file:
#     data = json.load(file)
#
# print(data)


def write_order_to_json(item, quantity, price, buyer, date):

    order = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    }

    with open('orders.json', 'r') as file:
        data = json.load(file)
        key = list(data.keys())[0]
        data[key].append(order)

    with open('orders.json', 'w') as file:
        json.dump(data, file, indent=2)


if __name__ == '__main__':
    write_order_to_json(
        item='apple',
        quantity=3,
        price=150,
        buyer='Vasia',
        date=f'{datetime.datetime.now()}'
    )
