# Albert Pacheco
#Student id:011151730
# DSA_2_WGUPS Routing Program

import csv
import Truck
import Package
from HashTable import CreateHashTable

#READ CSV DATA
with open ('CSV/Packages.csv') as file_1:
    packages_csv = csv.reader(file_1, delimiter = ',')

with open ('CSV/Distances.csv') as file_2:
    distances_csv = csv.reader(file_2, delimiter = ',')

with open ('CSV/Addresses.csv') as file_3:
    addresses_csv = csv.reader(file_3, delimiter = ',')

#CREATE 40 PACKAGES WITH DATA FROM CSV



#CREATE 3 TRUCKS





#-------------------------Testing-----------------------------------------------
print("Testing")
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


#print(t1)
print(sample.table)

#-------------------------Testing-----------------------------------------------