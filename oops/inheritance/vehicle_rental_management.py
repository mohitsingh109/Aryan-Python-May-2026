class Vehicle:
    def __init__(self, vehicle_id ,brand ,model , rent_per_day, availability):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.rent_per_day = rent_per_day
        self.availability = availability

    def display(self):
        print("===========================================")
        print(f"Vehicle Id = {self.vehicle_id}")
        print(f"Brand = {self.brand}")
        print(f"Model = {self.model}")
        print(f"Rent/Day = {self.rent_per_day}")
        # if self.availability:
        #     print(f"Availability = Available")
        # else:
        #     print(f"Availability = Rented")
        print(f"Availability = { "Available" if self.availability else "Rented" }")
        print("==========================================")

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

    def display(self):
        print("=============Car===============")
        super().display()
        print(f"Number of Doors = {self.number_of_doors}")


class Bike(Vehicle):
    def __init__(self, vehicle_id,brand,model,rent_per_day,availability,helmet_included):
        super().__init__(vehicle_id,brand,model,rent_per_day,availability)
        self.helmet_included = helmet_included

    def wheelie_mode(self):
        print("Wheelie started")

    def display(self):
        print("=========Bike=================")
        super().display()
        print(f"Helmet = {self.helmet_included}")


class Truck(Vehicle):
    def __init__(self, vehicle_id,brand,model,rent_per_day,availability,load_capacity):
        super().__init__(vehicle_id,brand,model,rent_per_day,availability)
        self.load_capacity = load_capacity

    def load_cargo(self):
        print("Cargo loaded")

    def display(self):
        print("============Truck===============")
        super().display()
        print(f"Load Capacity = {self.load_capacity}")










