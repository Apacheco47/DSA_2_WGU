# Package class
import datetime

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
        self.delivery_truck = None

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s,%s ,%s" % (self.p_id, self.delivery_address, self.deadline, self.city, self.zip_code, self.weight, self.status, self.deliveryTime, self.delivery_truck)

    def set_status(self,status):
        self.status = status
        #print("Status Updated")
        return

    def set_delivery_time(self, time_input):
        self.deliveryTime = time_input

    def update_packages(self, time_input):
        time = self.deliveryTime
        if time > time_input:
            self.set_status("In Transit")
        elif time <= time_input:
            self.set_status("Delivered")
        else:
            self.set_status("At Hub")



