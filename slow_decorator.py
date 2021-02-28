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
        print(time.time() - start_time)
        return res
    return wrapped


def slow_decorator(func):
    def wrapped(*args):
        time.sleep(5)
        res = func(*args)
        return res
    return wrapped


@slow_decorator
@time_decorator
def func(first, second):
    result = bin(int(first, 2) + int(second, 2))
    return result


print(func("111", "0000"))
