#!/usr/bin/env python3

def main():
    print("Hello and welcome to the convert program")
    # get the number from user
    user_input = input("Please enter a value to convert:")
    try:
        num = float(user_input)
    except ValueError:
        print("Invalid value please enter a number.")
        exit()

    print("Choose what to convert:")
    print("P: Price, before --> after tax")
    print("S: Speed, km/h --> mph")
    what_to_convert = input().upper()

    if what_to_convert == 'S':
        result = num * 0.621371
        print(f"{num} km/h motsvarar {result:.2f} mph")

    elif what_to_convert == 'P':
        new_price = num * 1.08
        if num == 0.0:
            rabatt = -12.0
            print(f"{num} kr innan moms blir {new_price:.1f} kr efter moms")
            print(f"Rabatt: {rabatt} kr")
        else:
            print(f"{num} kr innan moms blir {new_price:.1f} kr efter moms")
    else:
        print("Invalid choice. Please enter 'S' or 'P'.")
        exit()

main()
