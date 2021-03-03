from itertools import zip_longest

def read_file_gen(path):
    with open(path, 'r', encoding='utf-8') as f:
        while True:
            s = f.readline()
            if s:
                yield s.replace('\n', '')
            else:
                break


def create_users_hobby(users, hobby, result):
    with open(result, 'w', encoding='utf-8') as f:
        f.writelines([f'{user}: {hobby}\n' for user, hobby
              in zip_longest(read_file_gen(users), read_file_gen(hobby))])
