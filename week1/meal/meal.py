# Author kflood
# Takes a given time and supplies the corresponding mealtime

def main():
    currentTime = input("What time is it? ")
    convertedTime = convert(currentTime)

    if 7 <= convertedTime <= 8:
        print("breakfast time")
    elif 12 <= convertedTime <= 13:
        print("lunch time")
    elif 18 <= convertedTime <= 19:
        print("dinner time")

# Converts time, a string in ##:## format to a float representing hours
def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + (float(minutes) / 60)


if __name__ == "__main__":
    main()