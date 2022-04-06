from sys import argv


def func():

    name, arg1, arg2, arg3 = argv

    res = (int(arg1) * int(arg2)) + int(arg3)
    print(res)


func()