# Author kflood
# Converts two text patterns into emojis

def main():
    # Prompt user for text input
    user_text = input()

    # Convert and print
    print(convert(user_text))

def convert(text_to_change):
    # Replace smileys
    smile_replaced = text_to_change.replace(":)", "\N{slightly smiling face}")
    
    # Replace frowneys
    return smile_replaced.replace(":(", "\N{slightly frowning face}")

main()