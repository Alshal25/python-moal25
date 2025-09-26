#!/usr/bin/env python3

# Colors i found online to make it look nice
RED = "\033[31m"
WHITE = "\033[0m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"

def greet():
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print(f"Hello {BLUE}{name}{WHITE} - your awesomeness!")
    print("What can I do you for?!")

def celsius_to_fahrenheit():
    user_input = input("Tell me the real temperature and i shall return the pretend temperature...")
    try:
        Calcius_input = float(user_input)
        Farenheit = round(Calcius_input * 9/5 + 32, 2)
        print(f"The make believe temperature (farenheit) is {GREEN}{Farenheit} degrees{WHITE}")
    except ValueError:
        print(f"That is not a valid number: {RED}{user_input}{WHITE} Plz try again")

def points_to_grade():
    try:
        max_point = float(input("Enter the max points: "))
        user_points = float(input("Enter your points: "))
        grade = (user_points / max_point) * 100

        if grade >= 90:
            print(f"You will recieve the score: {GREEN}A")
        elif grade >= 80:
            print(f"You will recieve the score: {GREEN}B{WHITE}")
        elif grade >= 70:
            print(f"You will recieve the score: {YELLOW}C")
        elif grade >= 60:
            print(f"You will recieve the score: {YELLOW}D{WHITE}")
        elif grade >= 50:
            print(f"You will recieve the score: {YELLOW}E")
        else:
            print(f"You will recieve the score: {RED}F{WHITE}")
    except ValueError:
        print(f"{RED}Invalid input. Please enter numbers only.{WHITE}")

def compare_numbers():
    previous_number = None
    first_time = True

    while True:
        first_input = input("Feed me a number or write 'done': ")

        if first_input.lower() == "done":
            print("")
            break

        try:
            num = int(first_input)
        except ValueError:
            print(f"That is not a valid number: {RED}{first_input}{WHITE} Please try again")
            continue

        if not first_time:
            if num > previous_number:
                print(f"{GREEN}{num} is larger! than {RED}{previous_number}{WHITE}")
            elif num < previous_number:
                print(f"{RED}{num}{WHITE} is smaller! than {GREEN}{previous_number}")
            else:
                print(f"{YELLOW}{num} is the same! as {previous_number}{WHITE}")

        previous_number = num
        first_time = False

def calculate_luhna_sum(ssn_without_dash):
    total_sum = 0
    for i in range(len(ssn_without_dash)):
        digit = int(ssn_without_dash[i])
        if i % 2 == 0:
            digit = digit * 2
            if digit > 9:
                digit = digit - 9
        total_sum = total_sum + digit
    return total_sum

def validate_ssn():
    user_input = input("Enter ssn to validate: ")

    if "-" in user_input:
        user_input = user_input.replace("-", "")

    if len(user_input) != 10:
        print(f"{RED}Not valid")
    elif not user_input.isdigit():
        print(f"{RED}Not valid{WHITE}")
    else:
        total_sum = calculate_luhna_sum(user_input)

        if total_sum % 10 == 0:
            print(f"{GREEN}Valid")
        else:
            print(f"{RED}Not valid{WHITE}")

def robber_language():
    word = input("Skriv in ett ord >")
    vowel_letters = "AEIOUYÅÄÖ"
    new_word = ""

    for i in range(len(word)):
        letter = word[i]
        new_word = new_word + letter

        if letter.upper() not in vowel_letters:
            if letter.isalpha():
                new_word = new_word + "o" + letter.lower()

    print(f"{YELLOW}{word} --> {GREEN}{new_word}{WHITE}")

