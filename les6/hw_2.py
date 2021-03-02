def getSpammer(logs: list):
    res = {}
    for i in logs:
        res.setdefault(i[0], 0)
        res[i[0]] += 1
    m = max(res.values())
    return {i:v for i,v in res.items() if v == m}


logs =[]

with open('nginx_logs.txt', 'r') as f:
    while True:
        s = f.readline()
        if not s:
            break
        s = s.split('"')[:2]
        logs.append((s[0].split(' ')[0], s[1].split(' ')[0], s[1].split(' ')[1]))
    
print(getSpammer(logs))


