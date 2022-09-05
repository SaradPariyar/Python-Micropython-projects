zander = float(input("Enter the length in CM "))
if (zander < 42):
    print("release the fish back into the lake, caught fish was caught below 42 cm")

#part 4
year = int(input("Please input a year:"))
if year % 4 == 0:

    if year %100 == 0 and year % 400 != 0:
        print("This year is not leap year")
    else:
        print("This year is leap year")

