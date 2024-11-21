list_floated = []

pow = lambda a : a ** 2

def reading_input_file(inp):
    with open(inp, "r") as file:
        for line in file:
            for number in line.split(" "):
                list_floated.append(float(number))

    def rewriting_input_file_with_new_numbers():
        with open(inp, "w") as file:
            for number in list_floated:
                if number != list_floated[len(list_floated) - 1]:
                    number = pow(number)
                    file.write(str(number) + " ")
                else:
                    number = pow(number)
                    file.write(str(number))

    rewriting_input_file_with_new_numbers()

    res = list((map(pow, list_floated)))
    print("changed values:", res)
    print("inputed values:", list_floated)
    return list_floated

print(reading_input_file("input.txt"))
