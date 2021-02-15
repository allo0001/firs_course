def num_translate(word):
    translation = {'один': 'one', 'два': 'two', 'три': 'three',
                   'четыре': 'four', 'пять': 'five', 'шесть': 'six',
                   'семь': 'seven', 'восемь': 'eight', 'девять': 'nine',
                   'десять': 'ten'}
    return translation.get(word.lower())


def num_translate_adv(word):
    translate = num_translate(word)
    if word[0].isupper() and translate != None:
        return translate.capitalize()
    else:
        return translate
    
    
print(num_translate_adv('Ldf'))
