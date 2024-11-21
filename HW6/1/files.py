with open('nums.txt', 'r') as file:
    for line in file:
        if len(line.split(" ")) < 4:
            print("Error: length of first line is lees than 4 elements")
        else:
            for number in line.split(" "):
                print(number)


