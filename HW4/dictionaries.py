# 1
school = {
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
}

# 2
print(school["2B"])

# 3

school["1B"] = 30
school["2A"] = 20
school["5A"] = 26

school["7A"] = 31
school["8A"] = 17

del school["2C"]
# 4

print(school)

# 5
a = { 'a': 1, 'b': 2, 'c': 3}
b = { 'c': 3, 'd': 4,'e': 5}

c = {}
for key in set(a.keys()) | set(b.keys()):
    c[key] = [a.get(key), b.get(key)]
sorted_c = dict(sorted(c.items()))
print(sorted_c)
