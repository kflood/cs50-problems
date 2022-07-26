# Author kflood
# Accept 25, 10, and 5 cent coin input towards a 50 cent coke, returning amount due or change owed if fully paid

def main():

    amount_due = 50

    while amount_due > 0:
        print("Amount Due:", amount_due)
        coin = int(input("Insert Coin: "))
        
        # Check for valid coin input, then apply towards amount due
        if coin == 25 or coin == 10 or coin == 5:
            amount_due = amount_due - coin
    
    print("Change owerd:", (0 - amount_due))

main()