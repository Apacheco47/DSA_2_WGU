# Albert Pacheco
#Student id:011151730
# DSA_2_WGUPS Routing Program

import csv
import Truck
import Package
from HashTable import CreateHashTable

#READ CSV DATA


#CREATE 3 TRUCKS





#-------------------------Testing-----------------------------------------------
print("Testing")
sample = CreateHashTable()
sample.insert(1,45)
sample.insert(4,4)
sample.insert(76,4)
sample.insert(32,5)
print(sample.table)

sample.find(1)
sample.find(32)
sample.delete(1)
sample.delete(32)
t1 = Truck.Truck(1, "1301 pens", 5, 6, 64)


#print(t1)
print(sample.table)

#-------------------------Testing-----------------------------------------------