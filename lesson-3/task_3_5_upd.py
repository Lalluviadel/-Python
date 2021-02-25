from random import choice


def get_jokes(n=2, repeat_words=True):
    """Returns n jokes that are made up of random words from three internal lists"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    list_jokes = []
    if repeat_words == True:
        for inx in range(n):
            list_jokes.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
        return list_jokes
    else:
        for inx in range(n):
            list_jokes.append(f"{del_word(nouns)} {del_word(adverbs)} {del_word(adjectives)}")
        return list_jokes


def del_word(some_list):
    tmp_item = choice(some_list)
    some_list.remove(tmp_item)
    return tmp_item


print(get_jokes(5, False))
