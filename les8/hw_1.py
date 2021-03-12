import re


def email_parse(email):
    re_mail = re.compile(r'\w+@\w+\.\w+')
    if re_mail.search(email):
        re_u = re.search(r'\w+@', email)
        re_d = re.search(r'@\w+\.\w+', email)
        return {'username': re_u[0][:-1], 'domain': re_d[0][1:]}
    else:
        raise ValueError


print(email_parse('someone@geekbrains.ru ds'))

#print(email_parse('someone@geekbrainsru ds'))
