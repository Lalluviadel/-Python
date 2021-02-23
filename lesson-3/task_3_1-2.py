def num_translate(num_en):
    dict_num = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
                'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь',
                'nine': 'девять', 'ten': 'десять'}
    if num_en == num_en.capitalize() and not dict_num.get(num_en.lower()) is None:
        print(dict_num.get(num_en.lower()).capitalize())
    else:
        print(dict_num.get(num_en))


num_translate(input("Enter a number from one to ten: "))
