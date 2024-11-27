NUMBER_NAMES = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

def lexical_increase(dictionary):
    arr = dictionary.split(" ")
    arr_with_lexical_meanings = []
    result = []
    for num in arr:
        num = int(num)
        if num in NUMBER_NAMES:
            arr_with_lexical_meanings.append(NUMBER_NAMES[num])

    arr_with_lexical_meanings = sorted(arr_with_lexical_meanings)

    for word in arr_with_lexical_meanings:
        for key, value in NUMBER_NAMES.items():
            if word == value:
                result.append(key)

    return result

print(lexical_increase("1 2 3 4"))
print(lexical_increase("1 2 3 4 12 13 19 25"))