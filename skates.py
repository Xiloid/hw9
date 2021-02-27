"""
    В прокате коньков есть разные размеры. Известно, что желающий покататься
    может надеть коньки любого размера, которые не меньше размера его ноги.
    Напишите функцию, которая принимает список доступных размеров коньков и
    список размеров ног желающих.
    И возвращает наибольшее количество людей,
    которые смогут покататься одновременно.
    Например:
    [in]
    [39, 38, 41, 37] (доступные размеры)
    [40, 39, 41] (размеры ног желающих)
    [out]
    2
    [37, 38, 39, 40] , [37, 37, 40, 40] -> 3
    [37, 38, 39, 40] , [42] -> 0
    [37, 38, 39] , [37, 37, 37, 37] -> 3
    Напишите несколько тестов
"""
available_sizes = [39, 38, 41, 37]
foot_sizes = [40, 39, 41]


def main():
    # для ввода вручную:
    # available_sizes = sorted(list(map(int, input('Введите доступные размеры коньков через проблел: ').split())))
    # foot_sizes = sorted(list(map(int, input('Введите размеры ног посетителей через проблел: ').split())))
    result = skates(available_sizes, foot_sizes)
    print(f'{result} одновременно катающихся')
    error_test()


def skates(available_sizes, foot_sizes):
    result = 0
    while True:
        try:
            available_sizes = list(filter(lambda x: x >= min(foot_sizes), available_sizes))
            available_sizes.pop(0)
            foot_sizes.pop(0)
            result += 1
        except:
            break
    return result


def error_test():
    available_sizes2 = [37, 38, 39, 40]
    foot_sizes2 = [37, 37, 40, 40]
    available_sizes3 = [37, 38, 39, 40]
    foot_sizes3 = [42]
    available_sizes4 = [37, 38, 39]
    foot_sizes4 = [37, 37, 37, 37]
    assert skates(available_sizes2, foot_sizes2) == 3
    assert skates(available_sizes3, foot_sizes3) == 0
    assert skates(available_sizes4, foot_sizes4) == 3
    print('No assertion errors')


if __name__ == "__main__":
    main()
