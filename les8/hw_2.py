import re

FILE_PATH = 'nginx_logs.txt'

re_ip = re.compile(r"(\d{1,3}[.]){3}\d{1,3}|([0-9a-g]*:){5,7}[0-9a-g]*")
re_date = re.compile(r'\d{2}/\w{3}/\d{4}(:\d{2}){3}')
re_type = re.compile(r'[A-Z]{3,4}\s')
re_resource = re.compile(r'\s(/\w+){2}')
re_code_size = re.compile(r'\s\d{3}\s\d+\s')


def log_parse(log):
    ip = re_ip.search(log).group(0)
    date = re_date.search(log).group(0)
    typ = re_type.search(log).group(0).strip()
    resource = re_resource.search(log).group(0).strip()
    code, size = re_code_size.search(log).group(0).strip().split(' ')
    return (ip, date, typ, resource, code, size)

with open(FILE_PATH, 'r', encoding=('utf-8')) as f:
    for s in f.readlines():
        print(log_parse(s), end='\n')
