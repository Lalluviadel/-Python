user_num = int(input('Введите число от 0 до 20: '))
while user_num not in range(0, 21):
    user_num = int(input('Число не соответствует условию. Введите число от 0 до 20: '))

if user_num == 1:
    print(f"{user_num} процент")
elif user_num in range(2, 5):
    print(f"{user_num} процента")
else:
    print(f"{user_num} процентов")

for num in range(0, 21):
    if num == 1:
        print(f"{num} процент")
    elif num in range(2, 5):
        print(f"{num} процента")
    else:
        print(f"{num} процентов")
    num += num
