# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, v= ","):
    a = []
    first = first.split(v)
    second = second.split(v)
    for i in first:
        for j in second:
            if i == j:
                a.append(i)
    a.sort()
    return a

group_1 = "Иванов|Петров|Сидоров"
group_2 = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(group_1, group_2, "|"))


