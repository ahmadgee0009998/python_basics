# Class & Object
# class Student:
#     def __init__(self, fullname):
#         self.name= fullname
#         print("Adding new student in database.")

# s1=Student("Ahmad")
# print(s1.name)

# Practice Question
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi", self.name, "your avg score is:",sum/3)
# s1 = Student("Ahmad", [98,87,90])
# s1.get_avg()

# Practice Question
class Accounts:
    def __init__(self,bal,acc):
        self.balance= bal
        self.account_no=acc

    # Debit method
    def debit(self, amount):
        self.balance-=amount
        print("Rs", amount ,"was debitted from your account")
        print("Total balance =", self.get_balance())

    # Credit method
    def credit(self, amount):
        self.balance+=amount
        print("Rs", amount ,"was creditted to your account")
        print("Total balance =", self.get_balance())

    # Final balance
    def get_balance(self):
        return self.balance

acc1 = Accounts(10000, 12345)
acc1.debit(1000)
acc1.credit(500)

# class Student:
    
#     # Constructor
#     def __init__(self, name, marks):
#         self.name = name        # Public variable
#         self.__marks = marks    # Private variable

#     # Public method
#     def display_info(self):
#         print("Name:", self.name)
#         print("Marks:", self.__marks)
#         self.__calculate_grade()   # Calling private method inside class

#     # Private method
#     def __calculate_grade(self):
#         if self.__marks >= 90:
#             print("Grade: A")
#         elif self.__marks >= 75:
#             print("Grade: B")
#         else:
#             print("Grade: C")


# # Creating object
# s1 = Student("Ahmad", 85)

# # Calling public method
# s1.display_info()

# Polymorphism
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