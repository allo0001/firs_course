def thesaurus_adv(*args):
    rez = {}
    for name, lastname in map(str.split, args):
        if rez.get(lastname[0]):
            if rez[lastname[0]].get(name[0]):
                rez[lastname[0]][name[0]].append(f'{name} {lastname}')
            else:
                rez[lastname[0]][name[0]] = [f'{name} {lastname}']
        else:
            rez[lastname[0]] = {name[0]: [f'{name} {lastname}']}

    return rez


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
