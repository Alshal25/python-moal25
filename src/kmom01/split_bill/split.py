#!/usr/bin/env python3

def main():
    print("Hello! This program splits bills between people")
    print()
    
    print("Please enter the total bill amount:")
    total_amount = float(input())
    
    print("How many people will split the bill?")
    number_of_people = int(input())
    
    amount_per_person = total_amount / number_of_people
    
    print()
    print("Here is the result:")
    
    if amount_per_person == int(amount_per_person):
        print(f"{amount_per_person:.1f} kr")
    else:
        result = f"{amount_per_person:.2f}"
        if result.endswith('0'):
            result = result[:-1]
        print(f"{result} kr")
    
    print("Each person should pay this amount.")

main()
