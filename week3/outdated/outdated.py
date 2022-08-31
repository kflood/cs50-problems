# Author kflood
# Converts dates from anno Domini to ISO 8601

def main():
    while True:
        try:
            date = input("Date: ")
            if date[0].isalpha():
                # Month dd, yyyy
                monthAndDay, year = date.split(",")
                year = year.strip()
                month, day = monthAndDay.split(" ")
                month = validMonths[month]
            elif date[0].isnumeric():
                # mm/dd/yyyy
                month, day, year = date.split("/")
        except (ValueError, KeyError):
            pass
        else:
            if 1 <= int(month) <= 12 and 1 <= int(day) <= 31 and 0 <= int(year) <= 9999:
                convertedDate = convertDate(month, day, year)
                break
    
    print(convertedDate)

def convertDate(m, d, y):
    # Compiles m, d, y into yyyy-mm-dd format, adding leading zeros where necessary
    if len(y) == 1:
        y = "000" + y
    elif len(y) == 2:
        y = "00" + y
    elif len(y) == 3:
        y = "0" + y
    if len(m) == 1:
        m = "0" + m
    if len(d) == 1:
        d = "0" + d
    isoDate = y + "-" + m + "-" + d
    return isoDate

validMonths = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}

main()