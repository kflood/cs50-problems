# Author kflood
# Take text input and remove all vowels

def main():
    full_text = input("Input: ")

    for char in full_text:
        if char.lower() not in 'aeiou':
            print(char, end="")
    
    # Add one new line for formatting   
    print()
    
main()