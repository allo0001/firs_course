from itertools import zip_longest


def read_file_gen(path):
    with open(path, 'r', encoding='utf-8') as f:
        while True:
            s = f.readline()
            if s:
                yield s.replace('\n', '')
            else:
                break


with open('users_hobby.txt', 'w', encoding='utf-8') as f:
    f.writelines([f'{user}: {hobby}\n' for user, hobby
          in zip_longest(read_file_gen('users.csv'), read_file_gen('hobby.csv'))])


result = [[user, hobby] for user, hobby
          in zip_longest(read_file_gen('users.csv'), read_file_gen('hobby.csv'))]

print(result)
