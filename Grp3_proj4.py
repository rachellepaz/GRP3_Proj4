import urllib.parse
import requests
from colorama import Fore, Back, Style
from datetime import datetime, date

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "k2BGKwAMKCqQB7KpRhTiC9fPY7OfCZsM"
now = date.today()

name = input(Fore.BLUE + "Please Enter Traveller's Namee: ")
print("                                              ")
print(Fore.RED + "Class 1 Vehicles: CAR \n, Van \n, Pick-Up \n, Motorcycle \n")
print(Fore.RED + "Class 2 Vehicles: Bus\n, Truck \n")
print(Fore.RED + "Class 3 Vehicles: Large Truck \n, Truck with trailer\n")
print("                                              ")
vehicle = input(Fore.BLUE + "Input what type of class of vehicles (1-3): ")
print("                                              ")
car = input(Fore.BLUE + "What is your car?: ")
print("                                              ")
plate = input(Fore.BLUE + "Please enter your plate number: ")
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
        print(Fore.GREEN + " Welcome to TEAM SECRET COMPANY")
        print(Fore.GREEN + "The Date Today is: ")
        print(now)
        print(Fore.RED + "**********************************************")
        print("                                              ")
        print(Fore.GREEN + "Welcome " + (name))
        print(Fore.GREEN + "Class of your vehicle is " + (vehicle))
        print(Fore.GREEN + "You own a " + (car))
        print(Fore.GREEN + "Your plate number is:  " + (plate))
        print("                                              ")
        print(Fore.GREEN + "Directions from " + (orig) + " to " + (dest))
        print(Fore.GREEN + "Trip Duration:   " +
              (json_data["route"]["formattedTime"]))
        print(Fore.GREEN + "Kilometers:      " +
              str("{:.2f}".format((json_data["route"]["distance"]) * 1.61)))
        print(Fore.GREEN + "Fuel Used (Liter): " +
              str("{:.2f}".format((json_data["route"]["distance"]) * 3.78)))
        print(Fore.GREEN + "Fuel Cost (USD): " +
              str("{:.2f}".format((json_data["route"]["distance"]) * 3.78 *
                                  (1.038))))
        print("                                              ")
        print(Fore.RED + "=============================================")
    elif json_status == 402:
        print(Fore.RED + "**********************************************")

        print(Fore.GREEN + "Status Code: " + str(json_status) +
              "; Invalid user inputs for one or both locations.")

        print(Fore.RED + "**********************************************\n")

    elif json_status == 611:
        print(Fore.RED + "**********************************************")

        print(Fore.GREEN + "Status Code: " + str(json_status) +
              "; Missing an entry for one or both locations.")

        print(Fore.RED + "**********************************************\n")
    else:
        print(
            Fore.RED +
            "************************************************************************"
        )

        print(Fore.GREEN + "For Staus Code: " + str(json_status) +
              "; Refer to:")

        print(
            Fore.GREEN +
            "https://developer.mapquest.com/documentation/directions-api/status-codes"
        )

        print(
            Fore.RED +
            "************************************************************************\n"
        )
