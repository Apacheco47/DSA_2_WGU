# Package class
class Package:
    def __init__(self, p_id, delivery_address, deadline, city, zip_code, weight):
        self.p_id = p_id
        self.delivery_address = delivery_address
        self.deadline = deadline
        self.city = city
        self.zip_code = zip_code
        self.weight = weight
        self.status = "At Hub"
        self.deliveryTime = None

    def __str__(self):
        return f"Package ID: {self.p_id}, {self.delivery_address}, {self.deadline}, {self.city}, {self.zip_code}, {self.weight}, {self.status}"

    def set_status(self,status):
        self.status = status
        print("Status Updated")
        return

