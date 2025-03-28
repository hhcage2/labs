# TODO Напишите функцию find_common_participants
def find_common_participants(a:str, b:str, sep_=','):
    a = a.split(sep_)
    b = b.split(sep_)
    list_ = []
    for i in a:
        if i in b:
            list_ += [i]
    return list_



participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


print(find_common_participants(participants_first_group, participants_second_group))
# выглядит криво поэтому буду ждать комментариев :)

# TODO Проверьте работу функции с разделителем отличным от запятой
