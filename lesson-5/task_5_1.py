# 1. Написать генератор нечётных чисел от 1 до n (включительно), без использования ключевого слова yield,
# полностью истощить генератор. Например:
# gen1 = iterator_without_yield(11)
# next(gen1)
# 1
# next(gen1)
# 3
# next(gen1)
# 5
# next(gen1)
# 7
# next(gen1)
# 9
# next(gen1)
# 11
# next(gen1)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# StopIteration

n = 11
gen_odd_num = (i for i in range(1, n+1, 2))
for i in gen_odd_num:
    next(gen_odd_num)
# можно ли мне через print(*gen_t) истощить генератор или по условиям задачи это недопустимо?
# print(*gen_t)
