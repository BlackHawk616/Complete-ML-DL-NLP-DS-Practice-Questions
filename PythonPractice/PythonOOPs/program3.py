# Create a base class Vehicle and derive classes like Car and Bike with specific attributes and methods.

class Vehicle:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model
    
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, speed):
        super().__init__(brand, model)
        self.speed = speed

    def display_info(self):
        super().display_info()
        print(f"Speed: {self.speed}")

class Bike(Vehicle):
    def __init__(self, brand, model, CC) -> None:
        super().__init__(brand, model)
        self.CC = CC

    def display_info(self):
        super().display_info()
        print(f"CC: {self.CC}")

car = Car("Toyota", "Camry", 120)
bike = Bike("Yamaha", "R15", 150)
car.display_info()
bike.display_info()