# Author kflood
# User creates a grocery list on the fly, program outputs formatted list, alphabetized and with quantities

def main():
    list = {}

    while True:
        try:
            item = input("").upper()
            if item in list:
                list[item] = int(list[item]) + 1
            else:
                list[item] = 1
        except EOFError:
            print()
            break
        
    for key in sorted(list):
        print(list[key], key)

main()