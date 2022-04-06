def fact():
    for el in (range(0, (int(input())))):
       yield el


for i in fact:
    my_list.append(i)
print(my_list)
