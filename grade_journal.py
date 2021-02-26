"""
    Пользователь вводит количество студентов N.
    После чего вводит N строк, в которых записана фамилия и балл через пробел.
    Программа выводит список фамилий, отсортированный по их баллам по убыванию.
    Пример:
    [out] Введите количество студентов:
    [in]  3
    [out] Введите фамилию и балл:
    [in]  Иванов 87
    [out] Введите фамилию и балл:
    [in]  Смирнов 90
    [out] Введите фамилию и балл:
    [in]  Фролов 89
    [out]
        1. Смирнов
        2. Фролов
        3. Иванов
"""


def main():
    students = {}
    n = int(input("Количество студентов: "))
    s = 0
    for i in range(n):
        s_name, s_point = map(str, input('Введите фамилию и балл через пробел: ').split())
        students[s_name] = int(s_point)
        s += int(s_point)
    sort_to_tuple = sorted(students.items(), key=lambda item: item[1], reverse=True)
    sort_to_dict = {k: v for k, v in sort_to_tuple}
    for i, key in enumerate(sort_to_dict):
        print(str(i + 1)+'.', key)


if __name__ == "__main__":
    main()
