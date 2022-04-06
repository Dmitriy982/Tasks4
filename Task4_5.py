from functools import reduce


def func():
    my_list = [el for el in range(100, 1001)]
    print(reduce(lambda x, y: x + y, my_list))


func()
