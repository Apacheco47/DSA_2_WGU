# Albert Pacheco
#Student ID:011151730
# DSA_2_WGUPS Routing Program

import csv
import datetime
import HashTable
import Truck
from HashTable import CreateHashTable

#READ CSV DATA
with open ('CSV/Distances.csv') as file_1:
    distances_csv = csv.reader(file_1, delimiter = ',')
    distances_csv = list(distances_csv)
with open ('CSV/Addresses.csv') as file_2:
    addresses_csv = csv.reader(file_2, delimiter = ',')
    addresses_csv = list(addresses_csv)

#2D LIST FOR ADDRESSES
addresses = [[]]
for row in addresses_csv:
    addresses.append(row)

#DISTANCE BETWEEN TWO LOCATIONS
def distance_between(x_coordinate, y_coordinate):
    miles = distances_csv[x_coordinate][y_coordinate]
    if miles == '':
        miles = distances_csv[y_coordinate][x_coordinate]
    return float(miles)

#ADDRESS EXTRACTION
def get_address_id(address):
    for i in range(len(addresses_csv)):
        while addresses_csv[i][2] != str(address):
            i += 1
        if addresses_csv[i][2] == str(address):
            address_id = addresses_csv[i][0]
            return int(address_id)
        else:
            return "Address ID not found"
    return None


#Hash Table Instance
package_hash = CreateHashTable()
#Load Packages
HashTable.load_packages("CSV/Packages.csv", package_hash)

#CREATE 3 TRUCKS ID, PACKAGES, LOCATION, DEPARTURE TIME, RETURN TIME, MILEAGE
#9:00 AM DEADLINE
Truck1 = Truck.Truck(1,[],"4001 South 700 East", datetime.timedelta(hours = 8, minutes =00), datetime.timedelta(hours = 23, minutes = 00),0)
#10:30 AM DEADLINE
Truck2 = Truck.Truck(2, [], "4001 South 700 East", datetime.timedelta(hours = 9, minutes = 5),datetime.timedelta(hours = 23, minutes = 00), 0)
#EOD DEADLINE
Truck3 =Truck.Truck(3,[] ,"4001 South 700 East", datetime.timedelta(hours = 10, minutes = 20),datetime.timedelta(hours = 23, minutes =00), 0)
#Method to add packages to each truck
def add_packages(truck, p_id, package_table):
    if package_table.find(p_id):
        truck.packages.append(p_id)
#Load packages to Truck 1
add_packages(Truck1, 1, package_hash)
add_packages(Truck1, 13, package_hash)
add_packages(Truck1, 14, package_hash)
add_packages(Truck1, 15, package_hash)
add_packages(Truck1, 16, package_hash)
add_packages(Truck2, 19, package_hash)
add_packages(Truck1, 20, package_hash)
add_packages(Truck1, 29, package_hash)
add_packages(Truck1, 30, package_hash)
add_packages(Truck1, 31, package_hash)
add_packages(Truck1, 34, package_hash)
add_packages(Truck1, 37, package_hash)
add_packages(Truck1, 40, package_hash)
#Load packages to Truck 2
add_packages(Truck2, 3, package_hash)
add_packages(Truck2, 6, package_hash)
add_packages(Truck2, 12, package_hash)
add_packages(Truck2, 17, package_hash)
add_packages(Truck2, 18, package_hash)
add_packages(Truck2, 21, package_hash)
add_packages(Truck2, 22, package_hash)
add_packages(Truck2, 23, package_hash)
add_packages(Truck2, 24, package_hash)
add_packages(Truck2, 26, package_hash)
add_packages(Truck2, 27, package_hash)
add_packages(Truck2, 35, package_hash)
add_packages(Truck2, 36, package_hash)
add_packages(Truck2, 38, package_hash)
add_packages(Truck2, 39, package_hash)
#Load packages to Truck 3
add_packages(Truck3, 2, package_hash)
add_packages(Truck3, 4, package_hash)
add_packages(Truck3, 5, package_hash)
add_packages(Truck3, 7, package_hash)
add_packages(Truck3, 8, package_hash)
add_packages(Truck3, 9, package_hash)
add_packages(Truck3, 10, package_hash)
add_packages(Truck3, 11, package_hash)
add_packages(Truck3, 25, package_hash)
add_packages(Truck3, 28, package_hash)
add_packages(Truck3, 32, package_hash)
add_packages(Truck3, 33, package_hash)

#NEAREST NEIGHBOR DELIVERY ALGORITHM RETURNS ROUTE
def nearest_neighbor_route(truck):
    #GET CURRENT LOCATION ID AND ADDRESS
    undelivered_packages = truck.packages.copy()
    route = []
    current_location = truck.location
    current_location_id = get_address_id(current_location)
    #ORDER PACKAGES BY DISTANCE FROM CURRENT LOCATION
    while undelivered_packages:
        closest_package = None
        closest_package_address_id = None
        min_distance = float('inf')
        for p_id in undelivered_packages :
            package = package_hash.find(p_id)
            package_address_id = get_address_id(package.delivery_address)
            dist = distance_between(int(current_location_id), int(package_address_id))
            if dist < min_distance:
                min_distance = dist
                closest_package = p_id
                closest_package_address_id = package_address_id

        route.append(closest_package)
        undelivered_packages.remove(closest_package)
        current_location_id = closest_package_address_id
    #print(route)
    return route

#METHOD TO DELIVER PACKAGES AND UPDATE TRUCK INFO
def delivery(truck, route):
#GET CURRENT PACKAGE ID AND ADDRESS
    current_location_id = get_address_id(truck.location)
    current_time = truck.departureTime

    for p_id in route:
        current_package = package_hash.find(p_id)
        delivery_address = current_package.delivery_address
        current_package_address_id = get_address_id(delivery_address)
#GET DISTANCE BETWEEN CURRENT LOCATION AND PACKAGE ADDRESS
        distance = distance_between(int(current_location_id), int(current_package_address_id))
        truck.mileage += distance
 # UPDATE PACKAGE DELIVERY TIME
        travel_time = datetime.timedelta(hours = distance/18)
        current_time += travel_time
#UPDATE TRUCK INFO
        truck.location = delivery_address
        truck.deliveryTime = current_time
        current_package.deliveryTime = current_time
        current_package.delivery_truck = ("Truck " + str(truck.truck_id))

        current_location_id = current_package_address_id
        truck.remove_package(p_id)
    #RETURN TO HUB
    hub_id = get_address_id("4001 South 700 East")
    return_trip = distance_between(int(current_location_id), int(hub_id))
    truck.mileage += return_trip
    truck.location = "AT HUB EOD"


    #print(truck.packages)
    print("Truck " + str(truck.truck_id) + " has delivered all packages!")

#DELIVER PACKAGES
delivery(Truck1, nearest_neighbor_route(Truck1))
delivery(Truck2, nearest_neighbor_route(Truck2))
if Truck1.location == "AT HUB EOD":
    delivery(Truck3, nearest_neighbor_route(Truck3))



#MAIN USER GUI
# Provide an intuitive interface for the user to view the delivery status of all packages at any time
# the total mileage traveled by all trucks
class Main:
    while True:
        print("*************************************** WGU - Postal Service ***************************************")
        print("                                      Package Tracking System")
        print("Options: ")
        print("1. View Individual Package Status")
        print("2. View Total Miles Traveled")
        print("3. View Status of All Packages")
        print("Input 0 to Exit")
        print("*****************************************************************************************************")
        usr_input = input("Enter Selection: ")

        if usr_input == "0":
            print("Thank you for using the Package Tracking System, Goodbye!")
            break
        elif usr_input == "1":
            while usr_input != "0":
                print("*************************************** WGU - Postal Service ***************************************")
                print("                                      Package Tracking System")
                print()
                print()
                print("                                 >>Input package ID to view status<<")
                print()
                print()
                print()
                print("Input 0 to Return to the Main Menu")
                print("*****************************************************************************************************")
                id_input = input("Enter Package ID: ")
                if id_input == "0":
                    print("Returning to Return to the Main Menu.")
                    break
                elif id_input.isnumeric():
                    print("PLease Enter a time to view the status of a package at that time.")
                    usr_time = input("Enter Time in HH:MM format: ")
                    (H, M) = usr_time.split(":")
                    time_check = datetime.timedelta(hours=int(H), minutes=int(M))
                    print("Status of Package: " + str(id_input))
                    print("ID | Delivery Address | City | Zip Code | Delivery Deadline | weight | Status | Delivery Time | Delivery Truck")
                    lookup = package_hash.find(int(id_input))
                    if lookup.p_id == 9 and (time_check < datetime.timedelta(hours=10, minutes=20)):
                        package_hash.find(9).set_status("Delayed")
                        package_hash.find(9).delivery_address = "300 State St"

                    else:
                        package_hash.find(9).delivery_address = "410 S. State St."
                        lookup.update_packages(time_check)

                    print(lookup)
                    pause = input("Press Enter to Continue.")
                    continue
                else:
                    print("Invalid Selection, please try again.")
                    continue


        elif usr_input == "2":
            print("Total Miles Traveled: " + str(Truck1.mileage + Truck2.mileage + Truck3.mileage))
            menu = input("Press Enter to Return to the Main Menu.")
        elif usr_input == "3":
            print("PLease Enter a time to view the status of all packages at that time.")
            usr_time = input("Enter Time in HH:MM format: ")
            (H,M) = usr_time.split(":")
            time_check = datetime.timedelta(hours = int(H), minutes = int(M))
            print("Status of All Packages: ")
            print("ID | Delivery Address | City | Zip Code | Delivery Deadline | weight | Status | Delivery Time | Delivery Truck")
            for i in range(1,41):
                lookup = package_hash.find(i)
                if lookup.p_id == 9 and time_check < datetime.timedelta(hours = 10, minutes = 20):
                    package_hash.find(9).set_status("Delayed")
                    package_hash.find(9).delivery_address = "300 State St"
                    print(lookup)
                else:
                    lookup.update_packages(time_check)
                    package_hash.find(9).delivery_address = "410 S. State St."
                    print(lookup)
            menu = input("Press Enter to Continue.")
        else:
            print("Invalid Selection, please try again.")
            continue



