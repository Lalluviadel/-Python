# 2. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield.
# Полностью истощить генератор. Например:
# gen1 = iterator_with_yield(11)
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


def gen_odd_num(n):
    for i in range(1, n+1, 2):
        yield i


gen_tmp = gen_odd_num(11)
# print(*gen_tmp)
for num in gen_tmp:
    next(gen_tmp)
