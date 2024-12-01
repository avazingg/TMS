import time

def decorator(func):
    def wrapper(n):
        start_time = time.time()
        result = func(n)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time:.6f} seconds")
        return result
    return wrapper

def recursion_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursion_factorial(n-1)

def generator_factorial(n):
    result = 1
    for number in range(1, n + 1):
        result *= number
    yield result

@decorator
def compute_recursion_factorial(n):
    return recursion_factorial(n)

@decorator
def compute_generator_factorial(n):
    return  next(generator_factorial(n))

print(compute_recursion_factorial(100))
print(compute_generator_factorial(100))