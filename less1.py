import sys
from telnetlib import Telnet

def show_size(x, level=0):
    print('\t' * level, f'type = {type(x)}, size = {sys.getsizeof(x)}, obj = {x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                show_size(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)


# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
# соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
# и также проверить тип и содержимое переменных.
print('---------------------Задача №1------------------------------------')
string1 = 'разработка'
string2 = 'сокет'
string3 = 'декоратор'

print(type(string1))  # <class 'str'>
print(type(string2))  # <class 'str'>
print(type(string3))  # <class 'str'>

string1_utf8 = b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'
string2_utf8 = b'\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82'
string3_utf8 = b'\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80'
# string3_utf8 = 'Ð´ÐµÐºÐ¾ÑÐ°ÑÐ¾Ñ'

print(type(string1_utf8))
print(type(string2_utf8))
print(type(string3_utf8))

print(string1_utf8.decode())
print(string2_utf8.decode())
print(string3_utf8.decode())

show_size(string1)
show_size(string1_utf8)

# 2. Каждое) из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность
# кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
print('------------------Задача №2------------------------------')

data = [b'class', b'function', b'method']

for i in data:
    print(f'\n{i}\n '
          f'Длинна {len(i)}'
    )
    print('Размер')
    show_size(i)

# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
print('------------------Задача №3------------------------------')

data = ['attribute', 'класс', 'класс']

for i in data:
    try:
        print(i.encode(encoding='ascii'))
    except Exception as e:
        print(f'ОШИБКА: {e}')
        print(i.encode('utf8'))

# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в
# байтовое и выполнить обратное преобразование (используя методы encode и decode).
print('------------------Задача №4------------------------------')

data = ['разработка', 'администрирование', 'protocol', 'standard']

for i in data:
    print(f'Переменная => {i}\n'
          f'В байтовом виде => {i.encode("utf8")}\n'
          f'Раскодированная обратно в строку  => {i.encode("utf8").decode()}\n')


# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип
# на кириллице.

print('------------------Задача №5------------------------------')
print('Не совсем понял что требуется в условиях задачи')
#
# with Telnet('yandex.ru', 80) as tn:
#
#     tn.set_debuglevel(1)
#     tn.interact()

import os



# 6. Создать текстовый # файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет»,
# «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и
# вывести его содержимое.

test_string = [
    'сетевое программирование',
    'сокет',
    'декоратор'
]

encoding = [
'cp500',
'utf-16',
'GBK',
'windows-1251',
'ASCII',
'US-ASCII',
'Big5',
'utf-8'
]
true_encod = ''
for enc in encoding:
    try:
        if enc == 'utf-8':
            print('\nМИНУТОЧКУ ВНИМАНИЯ - принудительное открытие файла в UTF-8')
            file = open('test_file.txt', encoding=enc)
            for i, string in enumerate(file):
                print(f'{i}. Ожидаемая строка => {test_string[i]}, полученая строка => {string}')
                if test_string[i] == string:
                    true_encod = enc
        else:
            file = open('test_file.txt', encoding=enc)
            print(f'\nКодировка {enc}')
            for i, string in enumerate(file):
                print(f'{i}. Ожидаемая строка => {test_string[i]}, полученая строка => {string}')
                if test_string[i] == string:
                    true_encod = enc
    except UnicodeError:
        print(f'С кодировкой {enc} не открывается!!')

print(f'\n<<<<<<<<Кодировка по умолчанию => {true_encod}>>>>>>>>>>>>>>>>>>\n')
# file = open('test_file.txt', 'r')
# for i in file:
#     pass
#
# file.close()