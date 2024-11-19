def find_week_day_by_number(day):
    match day:
        case 1:
            return "понедельник"
        case 2:
            return "вторник"
        case 3:
            return "среда"
        case 4:
            return "четверг"
        case 5:
            return "пятница"
        case 6:
            return "суббота"
        case 7:
            return "воскресенье"
        case _:
            return "Некорректный номер дня недели"

print(find_week_day_by_number(2))



def unique_numbers_in_list(arr):
    unique = ""
    for i in range(arr[0], len(arr)):
        if arr.count(arr[i]) == 1:
            unique += str(arr[i]) + " "
    return unique.strip()


list0 = [1, 4, 2, 3, 5, 1, 3, 2, 4, 10]
list1 = [4, 5, 6, 7, -2, 1, -3, 5, -10, 15]
print(unique_numbers_in_list(list))


def sum_of_lists(a,b):
    return a + b

print(sum_of_lists(list0,list1))

def sorted_sum_of_2_arrays(a,b):
    return sorted(sum_of_lists(a,b))

print(sorted_sum_of_2_arrays(list0,list1))