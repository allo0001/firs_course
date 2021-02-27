tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В'#, '8Б', '10А', '10Б', '9А'
]


def gen():
    for i, name in enumerate(tutors):
        yield name, klasses[i] if i < len(klasses) else None


g = gen()
print(type(g))

for elem in g:
    print(elem)
