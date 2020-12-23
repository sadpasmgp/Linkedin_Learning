from functools import wraps

def munch(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        new_string = ''
        result = func(*args, **kwargs)
        for index, char in enumerate(result):
            c = 'x' if start <= index < end else char
            new_string += c





@munch(1, 4)
def fib():
    return 'Fibonacci'

print(fib())