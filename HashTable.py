#HASH TABLE CLASS
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

#Search and print element in hash table if found
    def find(self,key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv_pair in bucket_list:
            if key == kv_pair[0]:
                print("Item Located at index: " + str(bucket) + " with value: " + str(kv_pair[1]))
                return kv_pair[1]
        else: print("Item not found")
        return None


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


