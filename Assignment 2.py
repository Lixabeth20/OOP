class Vehicle:
    def __init__(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def __str__(self):
        return f"This vehicle is {self.color}."
my_vehicle = Vehicle("red")
print(my_vehicle.getColor())  
print(my_vehicle)             



class Car(Vehicle):
    def __init__(self, color, has_winter_tires=False):
        super().__init__(color)  
        self.has_winter_tires = has_winter_tires

    def __str__(self):
        vehicle_str = super().__str__()  
        return f"{vehicle_str}Has winter tires: {self.has_winter_tires}"
my_car = Car("blue", True)
print(my_car)  

    
class Truck(Vehicle):
    def __init__(self, color, has_trailer=False):
        super().__init__(color)  
        self.has_trailer = has_trailer

    def __str__(self):
        vehicle_str = super().__str__()  
        return f"{vehicle_str}Has trailer: {self.has_trailer}"
my_truck = Truck("white", True)
print(my_truck)

    

class Garage:
    def __init__(self):
        self.parked_vehicle = None  

    def setVehicle(self, parked):
        self.parked_vehicle = parked  

    def __str__(self):
        if self.parked_vehicle:
            return f"Description of the parked vehicle:{self.parked_vehicle}"
        else:
            return "The garage is empty."
my_car = Car("red", True)
my_truck = Truck("blue", False)

my_garage = Garage()
print(my_garage)  # Output: The garage is empty.

my_garage.setVehicle(my_car)
print(my_garage)
my_garage.setVehicle(my_truck)
print(my_garage)

        

class GarageTester:
    def getExample():
        my_truck = Truck("black", False)
        my_garage = Garage()
        my_garage.setVehicle(my_truck)
        print(my_garage)
GarageTester.getExample()


class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"Customer Name: {self.name}Address: {self.address}"
customer1 = Customer("John Doe", "Bugujju, Mukono")
print(customer1)





