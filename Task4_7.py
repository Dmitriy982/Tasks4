from functools import reduce


def fact():
    for el in (range(1, (int(input("Введите факториал: "))) + 1)):
        yield el


my_list = []
g = fact()
for i in g:
    my_list.append(i)
print(my_list, end=' = ')
real_fact = reduce(lambda x, y: x * y, my_list)
print(real_fact)
