from oops.inheritance.vehicle_rental_management import Vehicle, Car,Bike,Truck

car = Car("V101","TOYOTA","Fortuner",3500,True,4)
bike = Bike("V201","TOYOTA","Classic 350",900,False, "Yes")
truck = Truck ("V301","TOYOTA","SIGNA",6500, True, 5)

vehicles = [car,bike,truck]

car.rent_vehicle()
bike.rent_vehicle()
truck.rent_vehicle()


for vehicle in vehicles:
    vehicle.display()

bike.return_vehicle()
truck.return_vehicle()

car.start_ac()
