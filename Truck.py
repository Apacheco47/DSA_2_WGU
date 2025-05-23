class Truck:
    def __init__(self, truck_id, packages, location, departure_time, deliveryTime, mileage):
        self.truck_id = truck_id
        self.packages = packages
        self.capacity = 16
        self.location = location
        self.departureTime = departure_time
        self.deliveryTime = deliveryTime
        self.mileage = mileage

    def __str__(self):
        return "%s,%s,%s,%s,%s,%s,%s" % (self.truck_id ,self.packages,self.capacity, self.location, self.departureTime, self.deliveryTime, self.mileage)


