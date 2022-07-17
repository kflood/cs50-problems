# Author kflood
# Takes a simple math expression as string input (int operator int) and outputs a floating point answer of the evaluated expression

x, y, z = input("Expression: ").split()

if y == "+":
    print(float(x) + float(z))
elif y == "-":
    print(float(x) - float(z))
elif y == "*":
    print(float(x) * float(z))
else:
    print(float(x) / float(z))

