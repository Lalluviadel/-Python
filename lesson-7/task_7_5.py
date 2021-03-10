import os
from json import dump


def get_file_path(user_folder):
    for i in os.walk(user_folder):
        for file in i[2]:
            yield os.path.join(i[0], file)


def get_stat(some_gen):
    for dir_f in some_gen:
        file_size, inx = os.stat(dir_f).st_size, 1
        f_ext = os.path.basename(dir_f).split('.')[1]
        while file_size > 10:
            file_size = file_size // 10
            inx += 1
        yield 10 ** inx, f_ext


my_folder = r'C:\Users\dns\Desktop\Учеба\Четверть 1\Marmaliukova_Marina_dz_5'
gen_paths = get_file_path(my_folder)
gen_info_f = get_stat(gen_paths)

dict_stat = {}
for file_info in gen_info_f:
    key, ext = file_info[0], file_info[1]
    if key in dict_stat:
        dict_stat[key][0] += 1
        if ext not in dict_stat[key][1]:
            dict_stat[key][1].append(ext)
    else:
        dict_stat.setdefault(key, [1, [ext]])
dict_stat = {i: dict_stat[i] for i in sorted(dict_stat)}
folder_name = os.path.basename(my_folder)

with open(f"{my_folder}/{folder_name}_summary.json", 'w', encoding='UTF-8') as f:
    dump(dict_stat, f, ensure_ascii=False)
