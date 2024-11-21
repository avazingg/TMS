# def (check_the)

odds = []
evens = []
def divide_numbers_on_odds_and_evens(inp):
    with open(inp, "r") as file:
        for line in file:
            for number in line.split(" "):
                if int(number) % 2 == 0:
                    evens.append(number)
                elif int(number) % 2 != 0:
                    odds.append(number)
    filling_odds_file()
    filling_evens_file()
    return

def filling_odds_file():
    with open("odds.txt", "w") as odds_file:
            for number in odds:
                if number == odds[len(odds) - 1]:
                    odds_file.write(str(number))
                else:
                    odds_file.write(str(number + " "))
    return

def filling_evens_file():
    with open("evens.txt", "w") as evens_file:
        for number in evens:
            if number == evens[len(evens) - 1]:
                evens_file.write(str(number))
            else:
                evens_file.write(str(number + " "))
    return

(divide_numbers_on_odds_and_evens("input.txt"))

