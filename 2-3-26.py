# Question = 1
# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")

# a = Animal()
# b = Dog()
# c = Cat()

# a.sound()
# b.sound()
# c.sound()

# Question = 2
# class Vehicle:
#     def move(self):
#         print("Vehicle is moving")

# class Car(Vehicle):
#     def move(self):
#         print("Car is moving")

# class Bike(Vehicle):
#     def move(self):
#         print("Bike is moving")

# class Bus(Vehicle):
#     def move(self):
#         print("Bus is moving")

# v1 = Car()
# v2 = Bike()
# v3 = Bus()

# Vehicles = [v1, v2, v3]

# for Vehicle in Vehicles:
#     Vehicle.move()

# Question = 3
# import math
# class Shape:
#     def area(self):
#         print("Area method not defined")

# class Rectangle(Shape):
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width
    
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         return math.pi*self.radius**2
    
# class Triangle(Shape):
#     def __init__(self,base,height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return (1/2)*self.base*self.height
    
# r = Rectangle(4, 7)
# c = Circle(12)
# t = Triangle(6, 8)

# Shapes = [r, c, t]
# for Shape in Shapes:
#     print("Area =",Shape.area())
    
# Question = 4
# class Employee:
#     def get_role(self):
#         print("I am a employee")

# class Manager(Employee):
#     def get_role(self):
#         print("I am Manager")

# class Developer(Employee):
#     def get_role(self):
#         print("I am Developer")

# class Designer(Employee):
#     def get_role(self):
#         print("I am Designer")

# a = Manager()
# b = Developer()
# c = Designer()

# a.get_role()
# b.get_role()
# c.get_role()

# Question = 5
# class Payment:
#     def pay_amount(self,amount):
#         print("Amount is paid")

# class CreditCardPayment(Payment):
#     def pay_amount(self,amount):
#         print(amount,"was paid through credit card")

# class JazzCashPayment(Payment):
#     def pay_amount(self,amount):
#         print(amount,"was paid through Jazzcash")

# class BankTransferPayment(Payment):
#     def pay_amount(self,amount):
#         print(amount,"was paid through bank account")

# Payments = [CreditCardPayment(),
# JazzCashPayment(),
# BankTransferPayment()]

# for p in Payments:
#     p.pay_amount(5000)

# Question = 6
# class Employee:
#     def calc_salary(self):
#         print("Salary not defined")

# class FullTimeEmployee(Employee):
#     def __init__(self,F_Salary):
#         self.F_Salary = F_Salary

#     def calc_salary(self):
#         return self.F_Salary
    
# class PartTimeEmployee(Employee):
#     def __init__(self,h_rate,hours):
#         self.h_rate = h_rate
#         self.hours = hours

#     def calc_salary(self):
#         return self.h_rate*self.hours
    
# class Intern(Employee):
#     def __init__(self,stipend):
#         self.stipend = stipend

#     def calc_salary(self):
#         return self.stipend

# f = FullTimeEmployee(50000)
# p = PartTimeEmployee(1500, 10)
# i = Intern(25000)

# Employees = [f, p, i]

# for Employee in Employees:
#     print("Salary =",Employee.calc_salary())