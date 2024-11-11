# 1

str = "Robin Singh"
str2 = "I love arrays they are my favorite"
arr = str.split(" ")
arr2 = str2.split(" ")
print(arr)
print(arr2)

# 2

array = ["Ivan", "Ivanou"]
city = "Minsk"
country = "Belarus"
print(f"Привет, {array[0]} {array[1]}! Добро пожаловать в {city} {country}")

# 3

arr_to_str = ["I", "love", "arrays", "they", "are", "my", "favorite"]
str_from_arr = " ".join(arr_to_str)
print(str_from_arr)

# 4
numbers = list(range(1, 11))
numbers.insert(2, "new item on 3rd position")
numbers.pop(6)
print(numbers)

# 5
a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}

c = [a.items(), b.items()]
print(c)