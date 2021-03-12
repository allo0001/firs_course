from functools import wraps


def val_checker(f):
    def _val_checker(func):
        @wraps(func)
        def wraper(*args):
            if f(*args):
                return func(*args)
            else: raise ValueError(f'wrong val: {args[0]}')
        return wraper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


print(calc_cube)
a = calc_cube(5)
print(a)
a = calc_cube(-5)
