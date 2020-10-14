class decorator_with_arg:

    def __init__(self, some_arg=None):
        print(f'АРГУМЕНТ ДЕКОР {some_arg}')
        self.some_arg = some_arg
        self.func = None

    def __call__(self, *args, **kwargs):
        # инициализация декоратора
        if self.func is None:
            print(f'Первый вызов, получили на вход: {args}')
            func = args[0]
            self.func = func
            return self.func
        print(f'Вызов функциии {self.func}')
        return self.func(*args, **kwargs)


@decorator_with_arg(some_arg='argument')
def test_func(x, y):
    return x + y

print(test_func(3, 8))


