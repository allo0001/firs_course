def thesaurus(*args):
    rez = {}
    for name in args:
        if rez.get(name[0]):
            rez[name[0]].append(name) 
        else:
            rez[name[0]] = [name]
    return rez
    
    
print(thesaurus("Иван", "Мария", "Петр", "Илья", "Иван", "Мария", "Петр", "Илья"))
