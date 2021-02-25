def thesaurus(*args):
    dict_1 = {}
    for item in args:
        item = item.capitalize()
        if item[0] not in dict_1:
            dict_1[item[0]] = list()
            dict_1.setdefault(item[0], dict_1[item[0]].append(item))
        else:
            dict_1[item[0]].append(item)
    dict_1 = {k: dict_1[k] for k in sorted(dict_1)}
    return dict_1


name_1 = "Игорь"
name_2 = "якоВ"
name_3 = "андрей"
name_4 = "аристарх"
name_5 = "иЛЬЯ"
result = thesaurus(name_5, name_4, name_2, name_3, name_1)

print(result)
