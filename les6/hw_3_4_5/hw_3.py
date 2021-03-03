from itertools import zip_longest


def read_file_gen(path):
    with open(path, 'r', encoding='utf-8') as f:
        while True:
            s = f.readline()
            if s:
                yield s.replace(',', ' ').replace('\n', '')
            else:
                break


def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        res = []
        while True:
            s = f.readline()
            if s:
                res.append(s.replace(',', ' ').replace('\n', ''))
            else:
                break
        return res


result = {user: hobby for user, hobby
          in zip_longest(read_file_gen('users.csv'), read_file_gen('hobby.csv'))}

print(result)
