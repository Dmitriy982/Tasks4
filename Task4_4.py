from random import randint


def func():
    list1 = [randint(0, 10) for i in range(10)]
    print(list1)
    my_list = [el for el in list1 if list1.count(el) == 1]
    print(my_list)


func()
