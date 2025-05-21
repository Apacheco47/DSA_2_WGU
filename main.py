# Albert Pacheco
#Student id:011151730
# DSA_2_WGUPS Routing Program

import csv
import datetime
import HashTable
import Truck
import Package
from HashTable import CreateHashTable

"""""
#READ CSV DATA
with open ('CSV/Packages.csv') as file_1:
    packages_csv = csv.reader(file_1, delimiter = ',')

with open ('CSV/Distances.csv') as file_2:
    distances_csv = csv.reader(file_2, delimiter = ',')

with open ('CSV/Addresses.csv') as file_3:
    addresses_csv = csv.reader(file_3, delimiter = ',')

"""

#Hash Table Instance
package_hash = CreateHashTable()
#Load Packages
HashTable.load_packages("CSV/Packages.csv", package_hash)

#CREATE 3 TRUCKS ID, PACKAGES, LOCATION, DEPARTURE TIME, RETURN TIME, MILEAGE
#9:00 AM DEADLINE
Truck1 = Truck.Truck(1,[],"4001 South 700 East", datetime.time(hour=8, minute=00), datetime.time(hour=00, minute=00),0)
#10:30 AM DEADLINE
Truck2 = Truck.Truck(2, [], "4001 South 700 East", datetime.time(hour=9, minute=5),datetime.time(hour=00, minute=00), 0)
#EOD DEADLINE
Truck3 =Truck.Truck(3,[] ,"4001 South 700 East", datetime.time(hour=10, minute=20),datetime.time(hour=00, minute=00), 0)

def add_packages(truck, p_id, package_table):
    if package_table.find(p_id):
        truck.packages.append(p_id)

add_packages(Truck1, 1, package_hash)
add_packages(Truck1, 13, package_hash)
add_packages(Truck1, 14, package_hash)
add_packages(Truck1, 15, package_hash)
add_packages(Truck1, 16, package_hash)
add_packages(Truck1, 20, package_hash)
add_packages(Truck1, 29, package_hash)
add_packages(Truck1, 30, package_hash)
add_packages(Truck1, 31, package_hash)
add_packages(Truck1, 34, package_hash)
add_packages(Truck1, 37, package_hash)
add_packages(Truck1, 40, package_hash)

add_packages(Truck2, 3, package_hash)
add_packages(Truck2, 6, package_hash)
add_packages(Truck2, 12, package_hash)
add_packages(Truck2, 17, package_hash)
add_packages(Truck2, 18, package_hash)
add_packages(Truck2, 19, package_hash)
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

print(Truck1)
print(Truck2)
print(Truck3)

#NEAREST NEIGHBOR DELIVERY ALGORITHM




#MAIN USER GUI










#-------------------------Testing-----------------------------------------------
print("Testing")
'''
sample = CreateHashTable()
pack1 = Package.Package(1, "1301 pens", 5, 6, 64554, 5)
sample.insert(1,45)
sample.insert(4,4)
sample.insert(76,4)
sample.insert(32,5)
sample.insert(pack1.p_id, pack1)
print(sample.table)
pack1.set_status("Delivered")
sample.find(1)
sample.find(32)
sample.delete(5)
sample.delete(32)
t1 = Truck.Truck(1, "1301 pens", 5, 6, 64)

print_line(pack1)
print_line(t1)
print_line(sample.table)
'''
#-------------------------Testing-----------------------------------------------