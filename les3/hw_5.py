# вариант без удаления из списка = варианту с удалением, переписать вариант без удаления
# процедура возврашает список кортежей, а должна список строк. join ++++++
from random import shuffle

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count, repeat=False):
    shuffle(nouns)
    shuffle(adverbs)
    shuffle(adjectives)
    jokes = list(zip(nouns, adverbs, adjectives))
    rez = []
    if count > len(jokes):
        count = len(jokes)
    for i in range(count):
        if repeat:
            rez.append(' '.join(jokes[i]))
        else:
            rez.append(' '.join(jokes.pop()))
    return rez


print(get_jokes(10, repeat=True))
