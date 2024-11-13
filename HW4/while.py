#while

num = 3
res = 1
i = 0
while i < num:
    i += 1
    res *= i
print(res)


# S1 = int(input("Введите начальную площадь первого сорта: "))
# S2 = int(input("Введите начальную площадь второго сорта: "))
# years = 0
# while S1 >= 0.1 * S2:
#     S1 *= 2
#     S2 *= 3
#     years += 1
# print(f"Через {years} года/лет")

n = int(input("Введите число N, больше 0: "))
sum_of_digits = 0
number_of_digits = 0
while n > 0:
    digit = n % 10
    sum_of_digits += digit
    number_of_digits += 1
    n //= 10
print("сумма чисел:", sum_of_digits)
print("число символов:", number_of_digits)

granddad_age = int(input("Введите возраст деда: "))
grandson_age = int(input("Введите возраст внука: "))
years = 0

if(granddad_age < grandson_age * 2):
    print("Слишком поздно, момент уже прошёл.")
while granddad_age != grandson_age * 2:
    granddad_age += 1
    grandson_age += 1
    years += 1
print("Возраст деда:", granddad_age, "\nВозраст внука:", grandson_age,  "\nПрошло лет:", years)