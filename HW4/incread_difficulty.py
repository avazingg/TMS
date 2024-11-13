import re


# 1

arr = [1, 4, 2, 3, 5, 1, 3, 2, 4]
unique = ""
for i in range(arr[0], len(arr)):
    if (arr.count(arr[i]) == 1):
        unique += str(arr[i]) + " "
print(unique.strip())


# 2
string = "a" * 9000 + "b" * 1000

def the_most_common_symbol(str):
    dic = {}
    str = re.sub('[^A-Za-z]', '', str).lower()
    for char in str:
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1
    max_frequency = max(dic.values())
    result = {}
    for key in  dic:
        if dic[key] == max_frequency:
            result[key] = (dic[key])
    result = list(sorted(result))
    return result[0]

print(the_most_common_symbol(string))
