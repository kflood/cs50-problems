# Author kflood
# Checks the validity of a supplied vanity license plate

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Checks various parameters for validity
    if is_invalid_length(s):
        return False
    elif doesnt_start_with_two_letters(s):
        return False
    elif has_middle_numbers(s):
        return False
    elif has_punctuation(s):
        return False
    else:
        return True

def is_invalid_length(lplate):
    # Checks if the length of the string is 2-6 characters
    if 2 <= len(lplate) <= 6:
        return False
    else:
        return True

def doesnt_start_with_two_letters(lplate):
    # Checks if either of the first two characters are not letters (illegal)
    if lplate[0].isalpha() and lplate[1].isalpha():
        return False
    else:
        return True

def has_middle_numbers(lplate):
    left_letter = True
    for c in lplate:
        # Check for first number being 0 (illegal)
        if left_letter and c == "0":
            return True
        # Effectively marks where the letters end and numbers start
        elif c.isnumeric():
            left_letter = False
        # Check for a letter after any numbers (illegal)
        elif not left_letter and c.isalpha():
            return True
    return False

def has_punctuation(lplate):
    for c in lplate:
        # Checks if any character is not alpha-numeric (illegal)
        if not c.isalnum():
            return True
    return False

main()