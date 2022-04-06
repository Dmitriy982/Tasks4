from random import randint


def func():
    my_list = [randint(-10, 10) for i in range(10)]
    print(my_list)
    new_list = [j for i, j in zip(my_list, my_list[1:]) if j > i]
    print(new_list)


func()




