from abc import ABC, abstractmethod   # to apply all methods in all vehicle types 

 #Create abstract Vehicle class that serves as a template
    # When it creates a new vehicle it should:
    #  Set private vehicle ID 
    #  Set private license plate 
    #  Set private driver name
    #  Set availability status to True

class Vehicle(ABC):
    def __init__(self, vehicle_id, license_plate, driver_name):
        self._vehicle_id = vehicle_id
        self._license_plate = license_plate
        self._driver_name = driver_name
        self._is_available = True

# For controlled access to private data, 
    # Create property method for vehicle_id
    # When someone asks for vehicle_id:
    # Return the private _vehicle_id value
    # Vehicle data (ID, license plate, driver name) should remains unchanged after creation
    @property
    def vehicle_id(self):
        return self._vehicle_id
    
    @property
    def license_plate(self):
        return self._license_plate
    
    @property
    def driver_name(self):
        return self._driver_name
    
    @property
    def is_available(self):
        return self._is_available
    
    @is_available.setter
    def is_available(self, value):
        self._is_available = value
    
    # Define abstract method get_cost_per_mile that returns hm the vehicle cost per mile
    # Define abstract method get_capacity that returns the passenger capacity
    # Define abstract method get_vehicle_type that return the type name (as string)

    @abstractmethod
    def get_base_fare(self):
        pass
    
    @abstractmethod
    def get_cost_per_mile(self):
        pass
    
    @abstractmethod
    def get_capacity(self):
        pass
    
    @abstractmethod
    def get_vehicle_type(self):
        pass

    # DEFINE calculate_fare method (should work in all types based on their respective rates)
    # Input distance in miles
    # Calcu distance * cost_per_mile
    # Return the total amount

    def calculate_fare(self, distance):
        return self.get_base_fare() + (distance * self.get_cost_per_mile())

# Vehicle types 
    # Vehicle types class should inherit from Vehicle and have these methods using getter:
    #  (Added) Base fare - reference to MoveIt fare pricing
    #  Cost per mile of the vehicle
    #  Capacity of the vehicle
    #  Return the vehicle type

class Motorcycle(Vehicle):
    def get_base_fare(self):
        return 39
    
    def get_cost_per_mile(self):
        return 19.31
    
    def get_capacity(self):
        return 2
    
    def get_vehicle_type(self):
        return "Motorcycle"

class FourSeaterCar(Vehicle):
    def get_base_fare(self):
        return 50
    
    def get_cost_per_mile(self):
        return 30.14
    
    def get_capacity(self):
        return 4
    
    def get_vehicle_type(self):
        return "4-Seater Car"

class SixSeaterCar(Vehicle):
    def get_base_fare(self):
        return 65
    
    def get_cost_per_mile(self):
        return 38.97
    
    def get_capacity(self):
        return 6
    
    def get_vehicle_type(self):
        return "6-Seater Car"
    


    # Need to add:
    # Add formatted vehicle info for users to see
    # Store the info in a dictionary to prepare for save the information (and be saved to json file)



# Test (Added June 22)
if __name__ == "__main__":
    motorcycle = Motorcycle("M001", "ABC-123", "Princess Marian")
    car4 = FourSeaterCar("C001", "XYZ-456", "Baruruth")
    car6 = SixSeaterCar("C002", "DEF-789", "Maryjoy")
    
    # Test functionality
    print(f"Motorcycle fare for 5 miles: ${motorcycle.calculate_fare(5):.2f}")
    print(f"4-Seater Car fare for 5 miles: ${car4.calculate_fare(5):.2f}")
    print(f"6-Seater Car fare for 5 miles: ${car6.calculate_fare(5):.2f}")
    
    print(f"\nMotorcycle capacity: {motorcycle.get_capacity()}")
    print(f"Motorcycle available: {motorcycle.is_available}")
    
    # Test availability setter (after booking it wouldnt be available)
    motorcycle.is_available = False
    print(f"Motorcycle available after booking: {motorcycle.is_available}")