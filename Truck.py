class Truck:
    def __init__(self,id , location, departureTime, deliveryTime, mileage):
        self.id = id
        self.packages = set()
        self.capacity = 16
        self.location = location
        self.departureTime = departureTime
        self.deliveryTime = deliveryTime
        self.mileage = mileage

    def __str__(self):
        return f"Truck ID = {self.id} , Packages = {self.packages},Capacity = {self.capacity}, Location = {self.location}, Departure Time = {self.departureTime}, Delivery Time = {self.deliveryTime}, Mileaege = {self.mileage}"

