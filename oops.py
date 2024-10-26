# Object Oriented Programming(OOPS)
# CLASS & OBJECT
# ENCAPSULATION
# INHERITANCE
# POLYMORPHISM
# ABSTRACTION

# CLASS & OBJECTS

# class car:
#     def __init__(self, brand, color, year):
#         self.brand = brand
#         self.color = color
#         self.year = year

#     def display(self):
#         print(f"Car : {self.brand}, color : {self.color}, year : {self.year}")

# car1 =  car("tata", "red", 2023)
# car2 =  car("toyato", "blue", 2024)
# car3 =  car("honda", "green", 2022) 

# car1.display()
# car2.display()
# car3.display()
  
# ENCAPSULATION
# class car:
#     def __init__(self, brand, color, year, mileage):
#         self.brand = brand
#         self.color = color
#         self.year = year
#         self.mileage = mileage

#     def display(self):
#         print(f"Car : {self.brand}, color : {self.color}, year : {self.year}")

#     def car_mileage(self):
#             return self.mileage
    
#     def set_mileage(self, mileage):
#          if mileage >= 0:
#               self.mileage = mileage
#          else:
#               print("milage cannot be negative") 


# car1 =  car("tata", "red", 2023, 5000)
# car2 =  car("toyato", "blue", 2024, 4000)
# car3 =  car("honda", "green", 2022, 3000)

# # print("Mileage :", car1.car_mileage())

# car1.set_mileage(100)
# print("Mileage :", car1.car_mileage())

# car1.display()
# car2.display()
# car3.display()

# INHERITANCE
# class car:
#     def __init__(self, brand, color, year):
#         self.brand = brand
#         self.color = color
#         self.year = year

#     def display(self):
#         print(f"Car : {self.brand}, color : {self.color}, year : {self.year}")

# class electriccar(car):
#     def __init__(self, brand, color, year, battery):
#         super().__init__(brand, color, year)
#         self.battery = battery
    
#     def display_electric(self):
#          print(f"Car : {self.battery} power")
       
# car4 = electriccar("tesla", "royal blue", 2023,1000)
# car1 =  car("tata", "red", 2023)
# car2 =  car("toyato", "blue", 2024)
# car3 =  car("honda", "green", 2022) 

# car4.display()
# car4.display_electric()
# car1.display()
# car2.display()
# car3.display()

# POLYMORPHISM

# class car:
#     def __init__(self, brand, color, year):
#         self.brand = brand
#         self.color = color
#         self.year = year

#     def display(self):
#         print(f"Car : {self.brand}, color : {self.color}, year : {self.year}")

# class electriccar(car):
#     def battery(self):
#         print(f"{self.brand} is charging")

# class gascar(car):
#     def fuel(self):
#         print(f"{self.brand} is refueling")

# def start(car):
#     car.display()            
       
# car4 = electriccar("tesla", "royal blue", 2023)
# car1 =  gascar("tata", "red", 2023)

# start(car4)
# start(car1)

# car1.fuel()
# car4.battery()

# car4.display()
# car4.display_electric()
# car1.display()
# car2.display()
# car3.display()

# ABSTRACTION
from abc import ABC, abstractmethod

class coffee(ABC):
    def make_coffee(self):
        pass

class strongcoffee(coffee):
    def make_coffee(self):
        print("coffee making start.......")

machine = strongcoffee()
machine.make_coffee()        
     