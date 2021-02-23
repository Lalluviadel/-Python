from random import choice


def get_jokes(n):
    """Returns n jokes that are made up of random words from three internal lists"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    list_jokes = []
    for inx in range(n):
        list_jokes.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
    return list_jokes


print(get_jokes(5))
