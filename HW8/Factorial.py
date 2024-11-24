import time
def recursion_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursion_factorial(n-1)

start_time = time.time()
result = recursion_factorial(10)
end_time = time.time()
elapsed_time = end_time - start_time

def generator_factorial(n):
    result = 1
    for number in range(1, n + 1):
        result *= number
    yield result

start_time1 = time.time()
result1 = generator_factorial(10)
end_time1 = time.time()
elapsed_time1 = end_time1 - start_time1

print("\nresult for recursion:", recursion_factorial(20), "\nelapsed time for recursion", elapsed_time)
print("\nresult for genereator:", next(generator_factorial(20)), "\nelapsed time for genereator", elapsed_time1)

print("\nGenerator works faster than recursion:" ,elapsed_time > elapsed_time1)


# def calculate_time(func, *args):
#     start_time = time.time()
#     result = func(*args)
#     end_time = time.time()
#     elapsed_time = end_time - start_time
#     return result, elapsed_time