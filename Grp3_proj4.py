import urllib.parse
import requests
from colorama import Fore, Back, Style
from datetime import datetime, date

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "k2BGKwAMKCqQB7KpRhTiC9fPY7OfCZsM"
now = date.today()

name = input(Fore.BLUE + "Enter your name: ")
print("                                              ")
print(Fore.RED + "Class A: Car \n, Sedan \n, Mini-Van \n, Motorbike \n")
print(Fore.RED + "Class B: Bus\n, Mini-Bus \n")
print(Fore.RED + "Class C: Container Truck \n, Private Limousine\n")
print("                                              ")
vehicle = input(Fore.BLUE + "Input what type of class of vehicles (A-C): ")
print("                                              ")
car = input(Fore.BLUE + "Enter brand: ")
print("                                              ")
plate = input(Fore.BLUE + "Plate Number: ")
print("                                              ")

while True:

    orig = input(Fore.BLUE + "Source Location: ")
    print("                                              ")

    if orig == "quit" or orig == "q":

        break

    dest = input(Fore.BLUE + "End Location: ")
    print("                                              ")

    if dest == "quit" or dest == "q":

        break
    url = main_api + urllib.parse.urlencode({
        "key": key,
        "from": orig,
        "to": dest
    })

    print(Fore.GREEN + "URL: " + (url))

    json_data = requests.get(url).json()

    json_status = json_data["info"]["statuscode"]

    if json_status == 0:

        print(Fore.GREEN + "API Status: " + str(json_status) +
              " = A successful route call.\n")
        print(Fore.RED + "=============================================")
        print(Fore.GREEN + " GROUP 3 of 4ITH - VEHICLE AND TRIP CALC")
        print(Fore.GREEN + "Date: ")
        print(now)
        print(Fore.RED + "-------------------------------------------------*")
        print("                                              ")
        print(Fore.GREEN + "Hello there, " + (name))
        print(Fore.GREEN + "Vehicle Class: " + (vehicle))
        print(Fore.GREEN + "Vehicle: " + (car))
        print(Fore.GREEN + "Plate Number:  " + (plate))
        print("                                              ")
        print(Fore.GREEN + "Directions from " + (orig) + " to " + (dest))
        print(Fore.GREEN + "Duration of Trip:   " +
              (json_data["route"]["formattedTime"]))

        print(Fore.GREEN + "Kilometers:      " +
              str("{:.2f}".format((json_data["route"]["distance"]) * 1.61)))
        print(Fore.GREEN + "Fuel Used (Liter): " +
              str("{:.2f}".format((json_data["route"]["distance"]) * 3.78)))
        print(Fore.GREEN + "Fuel Cost ($): " +
              str("{:.2f}".format((json_data["route"]["distance"]) * 3.78 *
                                  (1.038))))
        print("                                              ")
        print(Fore.RED + "=============================================")
    elif json_status == 402:

        print(Fore.GREEN + "Status Code: " + str(json_status) +
              "; Error! Invalid user inputs for one or both locations.")

        print(
            Fore.RED +
            "-------------------------------------------------------------------------\n"
        )

    elif json_status == 611:
        print(
            Fore.RED +
            "----------------------------------------------------------------")

        print(Fore.GREEN + "Status Code: " + str(json_status) +
              "; Error! Missing an entry for one or both locations.")

        print(Fore.RED +
              "-----------------------------------------------------------\n")
    else:
        print(
            Fore.RED +
            "-------------------------------------------------------------------------"
        )

        print(Fore.GREEN + "For Staus Codes: " + str(json_status) +
              "; Refer to:")

        print(
            Fore.GREEN +
            "https://developer.mapquest.com/documentation/directions-api/status-codes"
        )

        print(
            Fore.RED +
            "-------------------------------------------------------------------------\n"
        )
