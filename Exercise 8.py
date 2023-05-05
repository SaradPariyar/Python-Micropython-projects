# Run the program step wise from the line 2.
import mysql.connector
from tabulate import tabulate
db_connect = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight',
    user='root',
    password='Ratgai#1!',
    autocommit= True
)

# Question 1
# Write a program that asks the user to enter the ICAO code of an airport. The program fetches and prints out
# the corresponding airport name and location (town) from the airport database used on this course.

ICAO_entrd = input("Enter ICAO code: ")
Cursor_obj = db_connect.cursor()
Cursor_obj.execute(f"select name as 'airport name', municipality as 'location' from airport where ident = '{ICAO_entrd}';")
result = Cursor_obj.fetchall()
print(tabulate(result, tablefmt="fancy_grid"))
print(Cursor_obj.rowcount, 'rows in set')

# Question 2
# Write a program that asks the user to enter the area code (for example FI) and prints out the airports located
# in that country ordered by airport type. For example, Finland has 65 small airports, 15 helicopter airports and so on.

areaCode = input("Enter the area code (eg. FI): ")
Cursor_obj = db_connect.cursor()
Cursor_obj.execute(f"select country.name as 'country name', airport.name as 'airport name', airport.type as 'airport type' from country, airport where country.iso_country = airport.iso_country and airport.iso_country = '{areaCode}' order by airport.type;")
result = Cursor_obj.fetchall()
print(tabulate(result, tablefmt="fancy_grid"))
print(Cursor_obj.rowcount, 'rows in set')

# Question 3 Write a program that asks the user to enter the ICAO codes of two airports. The program prints out the
# distance between the two airports in kilometers. The calculation is based on the airport coordinates fetched from
# the database. Calculate the distance using the geopy library: https://geopy.readthedocs.io/en/stable/. Install the
# library by selecting View / Tool Windows / Python Packages in your PyCharm IDE, write geopy into the search field
# and finish the installation.

from geopy import distance
Cursor_obj = db_connect.cursor()
ICAO_f = input("Enter the first ICAO code: ")
Cursor_obj.execute(f"select name from airport where ident = '{ICAO_f}';")
result = Cursor_obj.fetchall()
print(tabulate(result, tablefmt="fancy_grid"))
ICAO_s = input("Enter the second ICAO code: ")
Cursor_obj.execute(f"select name from airport where ident = '{ICAO_s}';")
result = Cursor_obj.fetchall()
print(tabulate(result, tablefmt="fancy_grid"))
Cursor_obj.execute(f"select latitude_deg, longitude_deg from airport where ident = '{ICAO_f}' or ident = '{ICAO_s}';")
Geo_lst = []
for x in Cursor_obj:
    Geo_lst.append(x)
print(f"The distance between the selected airports is", f"{distance.distance(Geo_lst[0], Geo_lst[1]).km:.2f} km")