import os


def get_file_path(user_folder):
    for i in os.walk(user_folder):
        for file in i[2]:
            yield os.path.join(i[0], file)


def get_size(some_gen):
    for dir_f in some_gen:
        file_size, inx = os.stat(dir_f).st_size, 1
        while file_size > 10:
            file_size = file_size // 10
            inx += 1
        yield 10 ** inx


my_folder = r'C:\Users\dns\Desktop\Учеба\Четверть 1\Marmaliukova_Marina_dz_7\Новая папка'
gen_paths = get_file_path(my_folder)
gen_keys = get_size(gen_paths)

dict_stat = {}
for new_key in gen_keys:
    if new_key in dict_stat:
        dict_stat[new_key] += 1
    else:
        dict_stat.setdefault(new_key, 1)
dict_stat = {i:dict_stat[i] for i in sorted(dict_stat)}
print(dict_stat)


