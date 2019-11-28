from functools import wraps
from inspect import stack
from datetime import datetime

def check_who_call(func):
    return stack()[2][3]


def log(func):
    def wrapper(request, *args, **kwargs):
        print('*'*50)
        print(f'{datetime.now()} => Функция <{func.__name__}> вызвана из : <{check_who_call(func)}> ')
        print(f'В нее переданы параметры: {request}')
        print('*'*50)
        return func(request, *args, **kwargs)
    return wrapper


