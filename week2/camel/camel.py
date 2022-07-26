# Author kflood
# Takes camelCase input and converts to snake_case, then prints

def main():
    camel_variable = input("camelCase: ")
    print("snake_case:", snakify2(camel_variable))

# Converts camelCase to snake_case, inserting '_' between words and lower-casing
def snakify2(var):
    snaked = ""

    # Adds each character to 'snaked' string, first adding a '_' if the character is upper-cased
    for char in var:
        if char.isupper():
            snaked = snaked + "_"
        snaked = snaked + char.lower()

    return snaked

main()