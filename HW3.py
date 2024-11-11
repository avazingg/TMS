# 1. Привести к целому типу -1.6, 2.99
print ("\n Task 1 \n ---------------------------")
first_number = -1.6
second_number = 2.99
print (int(first_number))
print (int(second_number))


# 2. Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
print ("\n Task 2 \n ---------------------------")
string = 'www.my_site.com#about'
print (string.replace("#", "/"))


# 3. Напишите программу, которая добавляет ‘ing’ к слову ‘stroka’
print ("\n Task 3 \n ---------------------------")
str_origin = "stroka"
str_addition = "ing"
print (str_origin + str_addition)


# 4. В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
print ("\n Task 4 \n ---------------------------")
str_to_be_order_reversed = "Ivanou Ivan"
str_to_be_order_reversed = str_to_be_order_reversed.split()[::-1]
print(" ".join(str_to_be_order_reversed))


# 5. Напишите программу которая удаляет пробел в начале, в конце
print ("\n Task 5 \n ---------------------------")
string_with_spaces = "  Hello World!  "
print (string_with_spaces.strip())


# 6. Создайте словарь, связав его с переменной school, и наполните его
# данными которые бы отражали количество учащихся в десяти разных
# классах (например, 1а, 1б, 2б, 6а, 7в и т.д.).
print ("\n Task 6 \n ---------------------------")
primary_school = {
    "1A": 25,
    "1B": 28,
    "2A": 30,
    "2B": 27,
    "2C": 26,
    "3A": 32,
    "4A": 29,
    "5A": 25,
    "6A": 31,
    "6B": 24,
    "7A": 30
}
high_school = {
    "8A": 29,
    "9A": 25,
    "9B": 31,
    "10A": 24,
    "11A": 30
}
whole_school = {**primary_school, **high_school}
print(whole_school)


# 7. Создайте список и извлеките из него списка второй элемент.
print ("\n Task 7 \n ---------------------------")
import random
size = 10
array = [random.randint(1, 100) for i in range(size)]
print("Randomly generated array: ",array)
print("2nd element off array: ",array[1])


# 8. Вывести входит ли строка1 в строку2 (пример: employ и employment )
print ("\n Task 8 \n ---------------------------")
full_string = "employment"
substring = "employ"
print (substring in full_string)


# 9. Вывести нужные символы
# x = "My name is Agent Smith"
# print(x[?]) #y
# print(x[?:?:?]) #nesgt
print ("\n Task 9 \n ---------------------------")
x = "My name is Agent Smith"
print(x[1]) #y
print(x[3:20:3])  # 'nesgt'

# 10*. Есть массив чисел. Известно, что каждое число в этом массиве имеет
# пару, кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
# Напишите программу, которая будет выводить уникальное число

print ("\n Task 10 \n ---------------------------")
array_with_numbers = [1, 5, 2, 9, 2, 9, 1]
result = []
for i in range(0, len(array_with_numbers)):
     unique = array_with_numbers.count(array_with_numbers[i])
     if unique == 1:
         result.append(array_with_numbers[i])
print(result)

# counter = 0
# for num in array_with_numbers:
#       if count[num] ==
#