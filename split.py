#!/usr/bin/env python3
"""
Split bill program for kmom01 - splits a bill between multiple people.
"""

def main():
    """Main function to handle bill splitting."""
    total_amount = float(input())
    number_of_people = int(input())
    amount_per_person = total_amount / number_of_people
    # Format to remove unnecessary decimals
    if amount_per_person == int(amount_per_person):
        print(f"{amount_per_person:.1f} kr")
    else:
        # Round to 2 decimals and remove trailing zeros
        formatted_amount = f"{amount_per_person:.2f}".rstrip('0').rstrip('.')
        print(f"{formatted_amount} kr")

if __name__ == "__main__":
    main()
