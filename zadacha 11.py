"""  11. Знайти значення функції y=3x6+6x2+7 при даному значенні x. """


def func(x):
    y = 3 * pow(int(x), 6) + 6 * pow(int(x), 2) + 7
    return int(y)


b = input()

print(func(b))
