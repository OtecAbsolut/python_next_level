'''

Есть функция, возвращающая первый элемент последовательности, удовлетворяющий заданному условию. Ее код:

def get_first_matching_object(predicate, objects=[]):
  matching_objects = (obj for obj in objects if predicate(object))
  if matching_objects:
    object = matching_objects[0]
    return object
  else:
    return None


Сначала укажите все проблемы этого кода (как критичные, так и не критичные), а затем сделайте свою реализацию такой функции.
1. Не кретическая ошибка (т.е. код будет работать, но может привести к нежелательным результатам)
objects=[] - так объявлять аргумент по умолчанию, считается анти-паттерном, на это даже ругается IDE.
если таким объявляением несколько раз вызвать функцию , то можно добится такого эффетка:

def append(number, number_list=[]):
    number_list.append(number)
    print(number_list)
    return number_list

append(5) # expecting: [5], actual: [5]
append(7) # expecting: [7], actual: [5, 7]
append(2) # expecting: [2], actual: [5, 7, 2]

лучше объявить аргумент например так:
number_list=None

2. в строке matching_objects = (obj for obj in objects if predicate(object))
Тут критическая ошибка object - не объявленная переменная, должно быть predicate(obj), но при этом не будет будет
ошибки, т.к. кроме всего прочего, object является базовым суперклассом и следовательно выражение if predicate(object):
не даст верного результата, т.к. в функцию predicate передастся <class object>, вместо элеменнта списка objects и
скорее всего мы получим False для всех итераций выражения if predicate(object) и как следствие пустой объект generator.

3. if matching_objects: - тоже не имеет смылса, т.к. даже если предыдущее выражение верент нам пустой генератор,
то данное выражение будет вседа True


4. object = matching_objects[0] - вызовет критическую ошибку. т.к. к генератору нельзя обращаться таким способом по индекcу.
Будет ошибка: TypeError

Если бы стояла задача исправить ошибки функции, то я бы написал так...
def get_first_matching_object(predicate, objects=None):
    matching_objects = (obj for obj in objects if predicate(obj))
    try:
        return next(matching_objects)
    except StopIteration:
        return None

А если бы стояла задача написать более логичную (на мой взгляд) функцию, которая делает тоже самое, то я бы написал так:
def get_first_matching_object(predicate, objects=None):
    for obj in objects:
        if predicate(obj):
            return obj
'''

'''
На входе таблица с одной колонкой «Имя». С помощью SQL-запроса посчитайте, сколько раз каждое имя встречается в этой таблице.

SELECT name, COUNT(name) FROM Table GROUP BY name;

выдаст таблицу вида:
name, count(name)
apple  2 
и.т.д. 

'''

'''
У вас есть таблица с колонками «Товар», «Дата» и «Цена». Цена для конкретного продукта указана только за тот день, 
когда она фактически менялась. Далее она действует до следующего изменения. В таблице много разных продуктов. 
Напишите SQL-запрос, который выгрузит цену для каждого продукта на 1 января 2019 года.

Пример такой таблицы (для понимания):

Товар, Дата, Цена
Яблоко, 10 октября 2018, 100 руб.
Груша, 15 ноября 2018, 200 руб.
Яблоко, 25 ноября 2018, 150 руб.
Яблоко, 5 февраля 2019, 200 руб.
Груша, 1 января 2019, 230 руб.

На выходе хотим увидеть:

Товар, Цена
Яблоко, 150 руб.
Груша, 230 руб.

SELECT товар,  цена FROM Table WHERE (товар, дата) in 
(SELECT  товар, max (дата) FROM Table where дата <= '2019-01-02' group by товар);

'''

import os


# for string in os.environ['PYTHONPATH'].split(os.pathsep):
#     print(string)

import sys

a = open('/dev/tty').readline()[:-1]
print(a)

















