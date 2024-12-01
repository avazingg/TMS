def typed(type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            converted_args = [type(arg) for arg in args]
            result = func(*converted_args, **kwargs)
            return  result
        return wrapper
    return decorator

def add_three_symbols(a, b, c):
    return a + b + c

@typed(type=str)
def add_two_symbols(a, b):
    return a + b

print(add_two_symbols(1, 2))

@typed(type=int)
def add_three_symbols(a, b, c):
    return a + b + c

print(add_three_symbols(1, 2, 3))

@typed(type=str)
def add_three_symbols(a, b, c):
    return a + b + c

print(add_three_symbols(1, 2, 3))
