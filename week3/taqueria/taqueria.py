# Author kflood
# Takes user input to order items from the menu

def main():
    
    cost = 0.00
    while True:
        try:
            item = input("Item: ")
            # add item to total cost, format with 2 decimals, add $ and prints
            cost += menu[item.title()]
            print("${:.2f}".format(cost))
        except KeyError:
            pass
        except EOFError:
            # this handles if the user ends input via ctrl-d
            print()
            break

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

main()