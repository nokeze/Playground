#vehicle is the base class
class vehicle:
    def __init__(self):
        #dictionary of options
        self.vehicle_options = {'make': '', 'model': '', 'engineSize': ''}

    def setMake(self, make):
        self.vehicle_options['make'] = make

    def setModel(self, model):
        self.vehicle_options['model'] = model
    
    def setEngineSize(self, engineSize):
        self.vehicle_options['engineSize'] = engineSize

    def displayOptions(self):
        print("")
        print(f"You successfully created a vehicle and here are the options you entered.")
        print(f"The make: {self.vehicle_options['make']}")
        print(f"The model: {self.vehicle_options['model']}")
        print(f"The engineSize: {self.vehicle_options['engineSize']}")
        print("")

#car inherits from vehicle
class car(vehicle):
    def __init__(self):
        super().__init__()

    #add the number of doors to the dictonary
    def setNumDoors(self, numDoors):
        self.vehicle_options['numDoors'] = numDoors

    #override the method in the vehicle class
    def displayOptions(self):
        print("")
        print(f"You successfully created a car and here are the options you entered.")
        print(f"The make: {self.vehicle_options['make']}")
        print(f"The model: {self.vehicle_options['model']}")
        print(f"The engineSize: {self.vehicle_options['engineSize']}")
        print(f"The number of doors: {self.vehicle_options['numDoors']}")
        print("")

#pickup inherits from vehicle
class pickup(vehicle):
    def __init__(self):
        super().__init__()

    #add the bed length to the dictionary
    def setBedLength(self, bedLength):
        self.vehicle_options['bedLength'] = bedLength

     #add the fuel type to the dictionary
    def setCabStyle(self, cabStyle):
        self.vehicle_options['cabStyle'] = cabStyle

    #override the method in the vehicle class
    def displayOptions(self):
        print("")
        print(f"You successfully created a pickup and here are the options you entered.")
        print(f"The make: {self.vehicle_options['make']}")
        print(f"The engineSize: {self.vehicle_options['engineSize']}")
        print(f"The model: {self.vehicle_options['model']}")
        print(f"The bed length: {self.vehicle_options['bedLength']}")
        print(f"The cab style: {self.vehicle_options['cabStyle']}")
        print("")


print("Welcome to the Bellevue University Garage ")
print("")

vehicle_type = "0"

while vehicle_type != "3":

    vehicle_type = input("Enter 1 to create a car and 2 to create a pickup 3 to quit: ")
    print("")
    
    if (vehicle_type == "1"):
        my_vehicle = car()
        selected_make = input("Enter make: ")
        selected_model = input("Enter model: ")
        selected_engineSize = input("Enter engineSize: ")
        selected_doors = input("Enter number of doors: ")
        my_vehicle.setMake(selected_make)
        my_vehicle.setModel(selected_model)
        my_vehicle.setNumDoors(selected_doors)
        my_vehicle.displayOptions()
    elif(vehicle_type == "2"):
        my_vehicle = pickup()
        selected_make = input("Enter make: ")
        selected_engineSize = input("Enter engineSize: ")
        selected_model = input("Enter model: ")
        selected_bedlength = input("Enter bed length: ")
        selected_cabStyle = input("Enter cabStyle: ")
        my_vehicle.setMake(selected_make)
        my_vehicle.setModel(selected_model)
        my_vehicle.setEngineSize(selected_engineSize)
        my_vehicle.setBedLength(selected_bedlength)
        my_vehicle.setCabStyle(selected_cabStyle)
        my_vehicle.displayOptions()
    elif(vehicle_type == "3"):
        print("")
        print("Thank you for shopping")
        print("")
    else:
        print("What did you do?")