#################################################################################
# Basics of Class, Objects, inheritance, methods
#################################################################################
import time
class Person:
    def __init__(self, fname, lname, age):
        self.firstname = fname
        self.lastname = lname
        self.age = age

    def __str__(self):
        return f"{self.firstname} {self.lastname}({self.age})"
    
    def myIntroduction(self):
        print("Hello my name is " + self.firstname)

    def printName(self):
        print(self.firstname, self.lastname)

class Sport(Person):
    def __init__(self, fname, lname, sport):
        self.firstname = fname
        self.lastname = lname
        self.sport = sport

class Child(Person):
    def __init__(self, fname, lname, age):
        Person.__init__(self, fname, lname, age)

class Student(Person):
    def __init__(self, fname, lname, age, year):
        super().__init__(fname, lname, age)
        self.graduationYear=year

    def welcome(self):
        print(f"Welcome new student {self.firstname} {self.lastname} to the class of {self.graduationYear}!")

p1 = Person("Shawn","Tester",21)
print(p1.firstname)
print(p1.age)
print(p1)
p1.myIntroduction()
p1.age = 25
print(p1.age)
p1.printName()
x = Sport("Billy","Bob","Lacrosse")
x.printName()
print(f"{x.firstname} {x.lastname}, favorite sport is: {x.sport}")
kid=Child("Jonny","Appleseed",26)
kid.printName()
collegeKid=Student("Mary","Jones",18,2026)
collegeKid.printName()
collegeKid.welcome()
# time.sleep(1)