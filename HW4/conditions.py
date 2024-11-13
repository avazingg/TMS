# 1

number = 13
if number > 0:
    number += 1
print (number)

# 2

a = 1
b = -1
c = 0
count = 0
if a > 0:
    count += 1
if b > 0:
    count += 1
if c > 0:
    count += 1
print(count)

#3

year = 1300
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(366)
else:
    print(365)

# 4

day = 2
match day:
    case 1:
        print("понедельник")
    case 2:
        print("вторник")
    case 3:
        print("среда")
    case 4:
        print("четверг")
    case 5:
        print("пятница")
    case 6:
        print("суббота")
    case 7:
        print("воскресенье")
    case _:
        print("Некорректный номер дня недели")

# 5

weight = 2
measure = 2
match measure:
    case 1:
        print(weight,"kg")
    case 2:
        print(weight * 0.000001, "kg")
    case 3:
        print(weight * 0.001, "kg")
    case 4:
        print(weight * 1000, "kg")
    case 5:
        print(weight * 100, "kg")
    case _:
        print("Неизвестная мера измерения")