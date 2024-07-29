#################################################################################
# Basics of Class, Objects, inheritance, methods
#################################################################################
import time

#################################################################################
# Basics of Polymorphism with Car, Boat and Plane all child classes
#################################################################################
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

print("Basic class call:")
vehicle1=Vehicle("NuCamp","Trailer")
print(f"The basic class is a {vehicle1.brand} {vehicle1.model}.")
print("Mode of movement:")
vehicle1.move()

for x in (car1, boat1, plane1):
  print(f"The transportation is a {x.brand} {x.model}.")
  print("The mode of transportation is the ability to:")
  x.move() #executing the same method for all three classes

time.sleep(1)
#################################################################################
# Basics of Polymorphism
#################################################################################
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  print(f"The transportation is a {x.brand} {x.model}.")
  print("The mode of transportation is the ability to:")
  x.move() #executing the same method for all three classes

time.sleep(1)
#################################################################################
# Basics of Polymorphism - all have a "move" method
#################################################################################
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  print(f"The transportation is a {x.brand} {x.model}.")
  print("The mode of transportation is the ability to:")
  x.move() #executing the same method for all three classes

time.sleep(1)
#################################################################################
# Basics of Class, Objects, inheritance, methods
#################################################################################
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

#Child class - Inheritance
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