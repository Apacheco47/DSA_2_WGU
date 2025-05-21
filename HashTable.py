#HASH TABLE CLASS
import csv
from email.utils import UEMPTYSTRING

import Package


class CreateHashTable:
#Initialize table with empty buckets
    def __init__(self,initial_capacity=40):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

#Insert element into hash table
    def insert(self,key,value):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for key_value in bucket_list:
            if key_value[0] == key:
                key_value[1] = value
                return True

        key_value = [key,value]
        bucket_list.append(key_value)
        return True

#Search and return element in hash table if found
    def find(self,key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv_pair in bucket_list:
            if key == kv_pair[0]:
                #print("Item found: ")
                return kv_pair[1]
        else: print("Item not found")
        return UEMPTYSTRING



#Delete element from hash table if found
    def delete(self,key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for i, (k,v) in enumerate(bucket_list):
            if k == key:
                del bucket_list[i]
            print("Item Deleted")
            return

        print("Item not found")

#Method to load packages to hash table from CSV
def load_packages(filename, package_table):
    with open(filename) as package_info:
        package_data = csv.reader(package_info, delimiter = ',')
        #next(package_data)
        for package in package_data:
            p_id = int(package[0])
            delivery_address = package[1]
            deadline = package[2]
            city = package[3]
            zip_code = package[4]
            weight = package[5]
            status = "At Hub"
            deliveryTime = None

            pack = Package.Package(p_id, delivery_address, deadline, city, zip_code, weight)
            package_table.insert(p_id, pack)


