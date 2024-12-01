greetings = lambda name : "Hello, " + name
print((greetings("Name")))

greeting_with_list = lambda names: [f"Hello, {name}" for name in names]
print(greeting_with_list(["The", "List", "of", "the", "names"]))
