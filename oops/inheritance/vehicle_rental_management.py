class Vehicle:
    def __init__(self, vehicle_id ,brand ,model , rent_per_day, availability):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.rent_per_day = rent_per_day
        self.availability = availability

    def display(self):
        print(self.vehicle_id)
        print(self.brand)
        print(self.model)
        print(self.rent_per_day)
        print(self.availability)

    def rent_vehicle(self):
        if self.availability:
            self.availability = False
            print("Vehicle rented successfully")
        else:
            print("Vehicle already rented")


    def return_vehicle(self):
        if self.availability:
            print("Vehicle already available")
        else:
            print("Vehicle return successfully")
            self.availability = True


class Car(Vehicle):
    def __init__(self, vehicle_id,brand,model,rent_per_day,availability,number_of_doors):
        super().__init__(vehicle_id,brand,model,rent_per_day,availability)
        self.number_of_doors = number_of_doors

    def start_ac(self):
        print("AC started")

class Bike(Vehicle):
    def __init__(self, vehicle_id,brand,model,rent_per_day,availability,helmet_included):
        super().__init__(vehicle_id,brand,model,rent_per_day,availability)
        self.helmet_included = helmet_included

    def wheelie_method(self):
        print("Wheelie started")

class Truck(Vehicle):
    def __init__(self, vehicle_id,brand,model,rent_per_day,availability,load_capacity):
        super().__init__(vehicle_id,brand,model,rent_per_day,availability)
        self.load_capacity = load_capacity

    def load_cargo(self):
        print("Cargo loaded")










