# 1

a = -3
b = 5

sum = 0
for i in range(a,b+1):
    sum+=i
print(sum)

# 2
natural_number_sum = 0
for i in range(a,b+1):
    if i > 0:
        natural_number_sum += i
print(natural_number_sum)

arr = [4, 5, 6, 7, -2, 1, -3, 5, -10, 15]
multiplication_of_positive = 1
sum_of_negative = 0
amount_of_negative = 0
for i in range(arr[0], len(arr)):
    if(arr[i] > 0):
        multiplication_of_positive *= arr[i]
    elif(arr[i] < 0):
        sum_of_negative += arr[i]
        amount_of_negative += 1

print("multiplication_of_positive: ",  multiplication_of_positive)
print("sum_of_negative ", sum_of_negative)
print("amount_of_negative ", amount_of_negative)

# 4
swimmers = {
    "Бекиш Александр": 21.07,
    "Будник Алексей": 20.34,
    "Гребень Анастасия": 22.12,
    "Давидович Татьяна": 30,
    "Дешук Дмитрий": 24.01,
    "Казак Анна": 28.17
}
min = list(swimmers.values())[0]
name = ""
for key in swimmers.keys():
   if swimmers[key] < min:
       min = swimmers[key]
       name = key
print(name, min)

arr = [1, 4, 2, 3, 5, 1, 3, 2, 4]
unique = ""
for i in range(arr[0], len(arr)):
    if (arr.count(arr[i]) == 1):
        unique += str(arr[i]) + " "
print(unique.strip())
