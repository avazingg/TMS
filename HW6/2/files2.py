def (check_the)

def divide_numbers_on_odds_and_evens():
    with open("input.txt", "r") as file, open("odds.txt", "w") as odds, open("evens.txt", "w") as evens:
        for line in file:
            for number in line.split(" "):
                if int(number) % 2 == 0:
                    evens.write(number + " ")
                elif int(number) % 2 != 0:
                    odds.write(number + " ")
    return "process finished, please check the files"

print(divide_numbers_on_odds_and_evens())

