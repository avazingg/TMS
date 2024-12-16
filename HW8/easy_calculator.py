import re
from unittest import removeResult


def calculator(user_input):
    try:
        user_input = user_input.replace(" ","")
        if not re.match(r"^[0-9+-/*]", user_input):
            return "Error: invalid characters in expression. If you want to stop the process, please type 'exit'"
        res = eval(user_input)
        return res
    except ZeroDivisionError:
        return "You are unable to divido on 0"
if __name__ == "__main__":
    print("Welcome to calculator!")
    print("Please write your expression:")
    while True:
        user_input = input()
        if user_input == "exit":
            print ("See you later alligator!")
            break
        result = calculator(user_input)
        print(result)
