def make_dict (element, some_dict, x):
    if element[x][0] not in some_dict:
        some_dict[element[x][0]] = list()
        some_dict.setdefault(element[x][0], some_dict[element[x][0]].append(element))
    else:
        some_dict[element[x][0]].append(element)


def dict_sort(some_dict):
    some_dict = {k: some_dict[k] for k in sorted(some_dict)}
    return some_dict


def thesaurus_adv(*args):
    dict_real = {}
    for item in args:
        item = tuple(item.split(' '))
        make_dict(item, dict_real, 1)
    for key in dict_real:
        dict_real[key] = level_below(dict_real[key])
    dict_real = dict_sort(dict_real)
    return dict_real


def level_below(dict_part):
    dict_tmp = {}
    for person in dict_part:
        make_dict(person, dict_tmp, 0)
    dict_tmp = dict_sort(dict_tmp)
    return dict_tmp


name_1 = "Игорь Альметьев"
name_2 = "Иван Сергеев"
name_3 = "Алла Сидорова"
name_4 = "Инна Серова"
name_5 = "Петр Алексеев"
name_6 = "Илья Иванов"
name_7 = "Анна Савельева"
name_8 = "Василий Суриков"
name_9 = "Богдан Иночкин"

result = thesaurus_adv(name_5, name_4, name_2, name_3, name_1, name_9, name_8, name_7, name_6)
print(result)
