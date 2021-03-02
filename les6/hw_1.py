def parse_logs(path):
    with open(path, 'r') as f:
        while True:
            s = f.readline()
            if not s:
                break
            s = s.split('"')[:2]
            yield [s[0].split(' ')[0], s[1].split(' ')[0], s[1].split(' ')[1]]


print(*parse_logs('nginx_logs.txt'))
