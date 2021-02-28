"""
    Реализовать декораторы:
    1. @time_decorator - считает и выводит время работы функции,
        если функция выполняется дольше 5 секунд, тогда дополнительно
        выводить сообщение print(f'{func.__name__} - very slow function')
    * в func.__name__ лежит название функции
    2. @slow_decorator - замедляет выполнение функции на 5 секунд
    Используйте библиотеку time, а именно функции time и sleep
"""
import time


def time_decorator(func):
    def wrapped(*args):
        start_time = time.time()
        res = func(*args)
        how_long = time.time() - start_time
        print(f'Время выполнения функции: {how_long}')
        if how_long > 5:
            print(f'{func.__name__} - very slow function')
        return res
    return wrapped


def slow_decorator(func):
    def wrapped(*args):
        time.sleep(5)
        res = func(*args)
        return res
    return wrapped


@time_decorator
@slow_decorator
def func(first, second):
    result = int(first) + int(second)
    return result


print(func("57545585644457", "1754545445480"))
