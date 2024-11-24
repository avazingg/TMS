def positive_generator(numbers):
    for number in numbers:
        yield abs(number)

example = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
print(list(positive_generator(example)))

def length_of_words (str):
    result = []
    for word in str.split(" "):
        try:
            if word == "the":
                raise Exception
            result.append(len(word))
        except:
            print("'theword' has been found")
    return result

string = "thequick brown box jumps over the lazy dog"
print(length_of_words(string))