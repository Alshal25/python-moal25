#!/usr/bin/env python3

import marvin1
import marvin2

# Colors i found online to make it look nice
RED = "\033[31m"
WHITE = "\033[0m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"

marvin_image = r"""
                    ╔══════════════════════════════════╗
                    ║          AI - BOOT v2.0          ║
                    ╚══════════════════════════════════╝
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
                             │  [████████████] │
                             │     Loading..   │
                             └─────────────────┘
                        ╭───────────────────────────╮
                        │  [1] [2] [3] [4] [5] [6]  │
                        │        [7] [8] [9]        │
                        │       Neural Network      │
                        │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     │
                        ╰───────────────────────────╯
                            ╭───╮           ╭───╮
                            │ ◈ │           │ ◈ │
                            ╰───╯           ╰───╯
"""

def main():
    """
    Main function with menu loop
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
        print("6) Translate to rövarspråket.")
        print("7) Create SSN.")
        print("8) Randomize string.")
        print("9) Find all indexes.")

        print("q) Quit.")

        choice = input(f" {MAGENTA} --> {WHITE}").upper()

        if choice == "Q":
            print("Bye, bye - and welcome back anytime!")
            stop = True

        elif choice == "1":
            marvin1.greet()

        elif choice == "2":
            marvin1.celsius_to_fahrenheit()

        elif choice == "3":
            marvin1.points_to_grade()

        elif choice == "4":
            marvin1.compare_numbers()

        elif choice == "5":
            marvin1.validate_ssn()

        elif choice == "6":
            marvin1.robber_language()

        elif choice == "7":
            birth_date = input("Enter birth date (YYMMDD): ")
            result = marvin2.create_ssn(birth_date)
            print(f"Generated SSN: {result}")

        elif choice == "8":
            string = input("Enter a string to randomize: ")
            result = marvin2.randomize_string(string)
            print(f"{string} --> {result}")

        elif choice == "9":
            text = input("Enter main string: ")
            substring = input("Enter substring to find: ")
            result = marvin2.find_all_indexes(text, substring)
            if result:
                print(f"Found at indexes: {result}")
            else:
                print("Substring not found")

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        if not stop:
            input(f"{YELLOW}\nTHE KNOWLEGE HAS BEEN GRANTED. NOW GO BOTHER SOMEONE ELSE...{WHITE}")

if __name__ == "__main__":
    main()
