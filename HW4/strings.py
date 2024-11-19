# strings
# 1

string = "Hola amigo nice to meet you!"
print(string[0])
print(string[-1])
print(string[2])
print(string[-3])
print(len(string))

# 2
string = "15 symbols line"
print(string[:8])
mid = (len(string) // 2)
print(string[mid-2:mid+2:1])
print(string[::3])
print(string[::-1])

# 3
my_name = "Vasili"
introduction = f"my name is {my_name}"
print(introduction)

# 4
test_string = "Hello world!"
position_of_symbol = test_string.index("w")
print("position of symbol w: ", position_of_symbol)
print("number of letter l in test string: ", test_string.count('l'))
print("Whether test string starts with 'Hello': ", test_string.startswith("Hello"))
print("Whether test string ends with 'qwe': ", test_string.endswith("qwe"))