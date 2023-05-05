# Question 1
# Write a program that asks the user for a number of a month and then prints out the corresponding season
# (spring, summer, autumn, winter). Save the seasons as strings into a tuple in your program. We can define each
# season to last three months, December being the first month of winter.

Seasons_tuple = ("Spring", "Summer", "Autumn", "Winter")
Months_list = ([3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 1, 2])
month_n = int(input("Enter a month in number (1-12:) "))
for i in range(len(Months_list)):
    if month_n in Months_list[i]:
        print(Seasons_tuple[i])
        break

# Question  2
# Write a program that asks the user to enter names. After each name is read the program either prints out
# New name or Existing name depending on whether the name was entered for the first time. Finally, the program lists
# out the input names one by one, one below another in any order. Use the set data structure to store the names.

Names = set()
temp_names = []
print("Enter five names.")
i = 1
while i <= 5:
    Entd_name = input(f"Name {i}: ")
    if Entd_name not in Names:
        temp_names.append(Entd_name)
        Names.update(temp_names)
        print("New name")
        i += 1
    else:
        print("Existing name")
for i in Names:
    print(i)

# Question 3 Write a program for fetching and storing airport data. The program asks the user if they want to enter a
# new airport, fetch the information of an existing airport or quit. If the user chooses to enter a new airport,
# the program asks the user to enter the ICAO code and name of the airport. If the user chooses to fetch airport
# information instead,the program asks for the ICAO code of the airport and prints out the corresponding name. If the
# user chooses to quit,the program execution ends. The user can choose a new option as many times they want until
# they choose to quit. (The ICAO code is an identifier that is unique to each airport. For example, the ICAO code of
# Helsinki-Vantaa Airport is EFHK. You can easily find the ICAO codes of different airports online.)

Data = {}
def option_entrd():
    print("Select from the available options:")
    print("press A to enter a new airport")
    print("press I to fetch airport information")
    print("press ENTER to quit program")
    return input()

option_sel = option_entrd()
while option_sel == "A" or option_sel == "I":
    if option_sel == "A":
        ICAO_in = input("enter ICAO code: ")
        Airport_nm = input("enter the name of airport: ")
        Data.update({ICAO_in: Airport_nm})
    else:
        ICAO_entrd = input("enter ICAO code: ")
        if ICAO_entrd in Data:
            print("Airport name is", Data[ICAO_entrd])
        else:
            print(" Requested airport not found")
    option_sel = option_entrd()
print("Bye!")