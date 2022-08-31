# Author kflood
# takes fraction input of a fuel tank and converts to percent

def main():
    while True:
        # get user input, split the numerator and denominator, checks for int and converts to percentage
        fraction = input("Fraction: ")
        X, Y = fraction.split('/')
        try:
            X = int(X)
            Y = int(Y)
            percent = int(( X / Y ) * 100)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            # makes sure fraction is valid
            if X <= Y:
                break

    if percent >= 99:
        print("F")
    elif percent <= 1:
        print("E")
    else:
        print(f"{percent}%")


main()