# Author kflood
# Takes an answer input and checks if it is '42' in some form

answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ").strip().lower()

if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")