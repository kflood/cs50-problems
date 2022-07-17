# Author kflood
# Takes greeting text from user and pays out $100 if it contains 'hello', $20 if it starts with another 'h' word, or $0 otherwise

greeting = input("Greeting: ").strip().lower()

if "hello" in greeting:
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")

