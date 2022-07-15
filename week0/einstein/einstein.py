
# Author kflood
# Determines the value of 'E' in joules for a user-provided value of 'm' in grams, per the equation E=mc^2

def main():
    m = input("m: ")

    print("E: ", energize(m))


# Multiplies mass by c^2, returns value
def energize(mass):
    return int(mass) * 300000000 * 300000000

main()