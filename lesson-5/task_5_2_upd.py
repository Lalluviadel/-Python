# 2. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield.
# Полностью истощить генератор.
# Усложнение(*):
# С ключевым словом yield - как в задании 1: генератор нечётных чисел от 1 до n (включительно),
# для чисел, квадрат которых меньше 200.


def gen_odd_num(n):
    for i in range(1, n+1, 2):
        if i**2 < 200:
            yield i


gen_tmp = gen_odd_num(50)
# print(*gen_tmp)
for num in gen_tmp:
    next(gen_tmp)
