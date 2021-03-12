from functools import wraps


def type_logger(func):

    @wraps(func)
    def wraper(*args, **kwargs):
        types = {a: type(a) for a in args}

        if kwargs:
            k_type = {k: {v: type(v)} for k, v in kwargs.items()}
            print(f'{func.__name__} args: {types}, kwargs: {k_type}')
        else:
            print(f'{func.__name__ } {types}')
        res = func(*args, **kwargs)
        return res

    return wraper


@type_logger
def calc_cube(x, **kwargs):
    return x ** 3


a = calc_cube(5, y=6)
print(calc_cube)
