with open('nums.txt', 'r') as file:
    for line in file:
        elements = line.split(" ")
        if len(elements) < 3:
            print("Error: length of first line is lees than 4 elements")
        else:
            print(elements[0], elements[1], elements[-2], elements[-1])
