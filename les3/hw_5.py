from random import shuffle, randint

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count, repeat=False):
    rez = []
    if repeat:
        shuffle(nouns)
        shuffle(adverbs)
        shuffle(adjectives)
        jokes = list(zip(nouns, adverbs, adjectives))
        if count > len(jokes):
            count = len(jokes)
        for i in range(count):
            rez.append(' '.join(jokes[i]))
    else:
        for i in range(count):
            rez.append(f'{nouns[randint(0,len(nouns)-1)]} {adverbs[randint(0,len(adverbs)-1)]} {adjectives[randint(0,len(adjectives)-1)]}')
    return rez


print(get_jokes(1000, repeat=True))
