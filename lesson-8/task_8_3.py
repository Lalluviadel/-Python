# Написать декоратор для логирования типов позиционных аргументов функции.
# Cможете ли вы вывести тип значения функции?
# Сможете ли решить задачу для именованных аргументов?
# Сможете ли вы замаскировать работу декоратора?
# Сможете ли вывести имя функции
from functools import wraps


def type_pos_logger(func):
    @wraps(func)
    def type_pos_get(*args, **kwargs):
        source_res = func(*args, **kwargs)
        dict_pos_args = {str(item): type(item) for item in args}
        result = ', '.join(f'{key}: {value}' for key, value in dict_pos_args.items())
        print(f"Позиционные аргументы функции {func.__name__}: {result}")
        return dict_pos_args, source_res
    return type_pos_get


def type_key_logger(func):
    @wraps(func)
    def type_key_get(*args, **kwargs):
        source_res = func(*args, **kwargs)
        dict_keyword_args = {str(item): type(item) for item in func.__defaults__}
        result = ', '.join(f'{key}: {value}' for key, value in dict_keyword_args.items())
        print(f"Именованныe аргументы функции {func.__name__}: {result}")
        print(f"Тип значения функции {func.__name__}({source_res}: {type(source_res)})")
        return dict_keyword_args, source_res
    return type_key_get


@type_pos_logger
@type_key_logger
def calc_cube(x, y, t=(1, 2), b=2, c='tell', g=True):
    return x ** 3


a = calc_cube(5, 'fdf')
# print(a[1][1])
