# TODO Напишите функцию find_common_participants
def find_common_participants(firstg, secondg, r = ','):
    f = set(firstg.split(r))
    s = secondg.split(r)
    return list(f.intersection(s))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
temp = find_common_participants(participants_first_group, participants_second_group, '|')
print(temp)