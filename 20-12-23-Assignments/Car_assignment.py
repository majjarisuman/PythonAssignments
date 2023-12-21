class Car:
    def __init__(self, brand, mileage, color, is_automatic, is_manual):
        self.brand = brand
        self.mileage = mileage
        self.color = color
        
        if is_automatic and is_manual:
            raise ValueError("A car cannot be both automatic and manual")
        
        self.is_automatic = is_automatic
        self.is_manual = is_manual

    def display_features(self):
        print(f"Car Brand: {self.brand}")
        print(f"Mileage: {self.mileage}")
        print(f"Color: {self.color}")
        if self.is_automatic:
            print("Transmission: Automatic")
        elif self.is_manual:
            print("Transmission: Manual")
        else:
            print("Transmission: Not specified")

# Creating car objects
car1 = Car("Toyota", 25, "Red", True, False)
car2 = Car("BMW", 30, "Blue", False, True)
car3 = Car("Ford", 20, "Black", False, False)

# Displaying car features
print("Car 1 Features:")
car1.display_features()
print("\nCar 2 Features:")
car2.display_features()
print("\nCar 3 Features:")
car3.display_features()
