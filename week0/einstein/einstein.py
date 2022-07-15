def main():
    m = input("m: ")

    print("E: ", energize(m))

def energize(mass):
    return int(mass) * 300000000 * 300000000

main()