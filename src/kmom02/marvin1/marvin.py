#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Colors i found online to make it look nice
RED = "\033[31m"
WHITE = "\033[0m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

marvin_image = r"""
                    ╔═════════════════════════════════╗
                    ║          AI - BOOT v2.0         ║
                    ╚═════════════════════════════════╝
                          ┌─────────────────────┐
                          │  ◉ SYSTEM ONLINE ◉  │
                          └─────────────────────┘
                                ┌───┐   ┌───┐
                                │ ● │   │ ● │
                                └───┘   └───┘
                                 \\       /
                                  \\     /
                                   ┌───┐
                                   │ > │
                                   └───┘
                            ┌─────────────────┐
                            │ MARVIN AI READY │
                            │    [████████]   │
                            │   Loading.....  │
                            └─────────────────┘
                        ╭─────────────────────────╮
                        │ [1] [2] [3] [4] [5] [6] │
                        │      Neural Network     │
                        │     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    │
                        ╰─────────────────────────╯
                          ╭───╮           ╭───╮
                          │ ◈ │           │ ◈ │
                          ╰───╯           ╰───╯
"""

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""


stop = False
while not stop:
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(marvin_image)
    print("Hi, I'm Marvin. I know it all. What can I do you for?")
    print("1) Present yourself to Marvin.")
    print("2) Calcius to farenheit.")
    print("3) Calculate grade.")
    print("4) Is smaller, bigger or equal.")
    print("5) Check SSN.")
    print("6) Match brackets")

    print("q) Quit.")

    choice = input(f" {MAGENTA} --> {WHITE}").upper()
    if choice == "Q":
        print("Bye, bye - and welcome back anytime!")
        stop = True

    elif choice == "1":
        name = input("What is your name? ")
        print("\nMarvin says:\n")
        print(f"Hello {BLUE}{name}{WHITE} - your awesomeness!")
        print("What can I do you for?!")

    elif choice == "2":
        user_input = input("Tell me the real temperature and i shall return the pretend temperature...")
        try:
            Calcius_input = float(user_input)
            Farenheit = round(Calcius_input * 9/5 + 32, 2)
            print (f"The make believe temperature (farenheit) is {GREEN}{Farenheit} degrees{WHITE}")

        except ValueError:
            print(f"That is not a valid number: {RED}{user_input}{WHITE} Plz try again")

    elif choice == "3":
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

    elif choice == "4":
        numbers = []  

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

            if numbers:  
                num2 = numbers[-1] 

                if num > num2:
                    print(f"{GREEN}{num} is larger! than {RED}{num2}{WHITE}")
                elif num < num2:
                    print(f"{RED}{num}{WHITE} is smaller! than {GREEN}{num2}")
                else:
                    print(f"{YELLOW}{num} is the same! as {num2}{WHITE}")
            
            numbers.append(num)

    elif choice == "5":
        user_input = input("Enter ssn to validate: ")
        
        if "-" in user_input:
            user_input = user_input.replace("-", "")
        
        if len(user_input) != 10:
            print(f"{RED}Not valid")
        elif not user_input.isdigit():
            print(f"{RED}Not valid{WHITE}")
        else:
            total_sum = 0
            for i in range(10):
                digit = int(user_input[i])
                if i % 2 == 0:
                    digit = digit * 2
                    if digit > 9:
                        digit = digit - 9
                total_sum = total_sum + digit
            
            if total_sum % 10 == 0:
                print(f"{GREEN}Valid")
            else:
                print(f"{RED}Not valid{WHITE}")

    elif choice == "6":
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

    else:
        print("That is not a valid choice. You can only choose from the menu.")

    if not stop:
        input(f"{YELLOW}\nTHE KNOWLEGE HAS BEEN GRANTED. NOW GO BOTHER SOMEONE ELSE...{WHITE}")
