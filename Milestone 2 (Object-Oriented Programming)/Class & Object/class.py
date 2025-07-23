
# # Creating class
# class Student:
#     name = "Rasel sarker",
    
# # creating object(intance)
# s1 = Student()
# print(s1.name)  

# s2 = Student()
# print(s2.name)


# Creating class
# class Car:
#     name = "Ferrari"
#     brand = "Lamborghini"  
#     color = "Red"
    
# # Creating objects (instances)
# s1 = Car()

# # Accessing object attributes
# print(s1.name)   
# print(s1.brand)  
# print(s1.color)  

# class Student:
#     def __init__(self, name, age):
#         print(self)
#         self.name = name
#         self.age = age
    
# # Creating objects (instances)
# s1 = Student("Rasel Sarker", 25)
# print(s1.name)


# class Bike:
#     new_bike = "Honda"    # This is a class attribute
#     def __init__(self, name):
#         self.name = name  # This is an object attribute

# # Creating an object (instance)
# s = Bike("Royal Enfield")

# print(s.name)  # Accessing object attribute
# print(Bike.new_bike)  # Accessing class attribute  


# Creating a class
# class Car:
#     def __init__(self, brand):
#         self.brand = brand

#     # define method to display car info
#     def display_info(self):
#         print(f"{self.brand}")

# car1 = Car("Tesla") # Creating an object (instance) of the class
# car1.display_info() # Calling methods using the object 

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def Welcome(self):
        print("Welcome guys!")

s1 = Student("Rasel", 25)
s1.Welcome() 

