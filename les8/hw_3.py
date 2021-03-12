from functools import wraps


def type_logger(func):

    @wraps(func)
    def wraper(*args, **kvargs):
        types = {a: type(a) for a in args}

        if kvargs:
            k_type = {k: {v: type(v)} for k, v in kvargs.items()}
            print(f'{func.__name__} args: {types}, kvargs: {k_type}')
        else:
            print(f'{func.__name__ } {types}')
        res = func(*args, **kvargs)
        return res

    return wraper


@type_logger
def calc_cube(x, **kvargs):
   return x ** 3


a = calc_cube(5, y=6)
print(calc_cube)
