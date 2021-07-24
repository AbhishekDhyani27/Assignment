# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 10:32:00 2021

@author: dhyani
"""

#Classes and Objects

#Class
#This List contains data of all the employees
kirk = ["James Kirk", 34, "Captain", 2265]
spock = ["Spock", 35, "Science Officer", 2254]
mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]


#Classes vs Instances

#Dog is a class name and pass is a keyword indicating where code will go
class Dog:
    pass

#We use __init__ to initialise values which that particular class contains
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
#Class attributes defined by assigning  value to a variable name outside of __init__
class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
#This string of no.s is a memory address that indicates where the Dog object is stored
 Dog()
__main__.Dog object at 0x106702d30>

#The new Dog instance is located at a different memory address
 Dog()
__main__.Dog object at 0x0004ccc90>

#a and b are false because of different memory address but they both got same dog class
 a = Dog()
 b = Dog()
 a == b
False


 class Dog:
     species = "Canis familiaris"
     def __init__(self, name, age):
         self.name = name
         self.age = age
#to pass arguments to the name and age parameters, put values into the parentheses after the  buddy = Dog("Buddy", 9)
buddy = Dog("Buddy", 9) 
miles = Dog("Miles", 4)

#After we create the Dog instances,we can access their instance attributes using dot notation
buddy.name
'Buddy'
 buddy.age
9

 miles.name
'Miles'
 miles.age
4

#Instance Methods

#This Dog class contains 2 instance methods
#1.description() returns a string displaying the name and age of the dog.
#2.speak() has one parameter called sound & returns a string containing the dog’s name and sound the dog makes.
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
#When we create a list object,we use print() to display a string that looks like the list
names = ["Fletcher", "David", "Dan"]
>>> print(names)
['Fletcher', 'David', 'Dan']

#we replace str with description to get a valid output
class Dog:
    # Leave other parts of Dog class as-is

    # Replace .description() with __str__()
    def __str__(self):
        return f"{self.name} is {self.age} years old"

class Dog:
    species = "Canis familiaris"

#breed attribute here defines breed of every dog so we can identify particular dog with more ease
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
 
 miles = Dog("Miles", 4, "Jack Russell Terrier")
 buddy = Dog("Buddy", 9, "Dachshund")
 jack = Dog("Jack", 3, "Bulldog")
 jim = Dog("Jim", 5, "Bulldog")

#Parent Classes vs Child Classes

#Extend the Functionality of a Parent Class

#To override a method defined on the parent class, you define a method with the same name on the child class.
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"
    
    miles = JackRussellTerrier("Miles", 4)
 miles.speak()
'Miles says Arf'

#change the string returned by .speak() in the Dog class
#when we create a new Bulldog instance named jim, jim.speak() returns the new string
class Dog:
    # Leave other attributes and methods as they are

    # Change the string returned by .speak()
    def speak(self, sound):
        return f"{self.name} barks: {sound}"
    
jim = Bulldog("Jim", 5)
 jim.speak("Woof")
'Jim barks: Woof'

#we can access the parent class from inside a method of a child class by using super()
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)
    
 miles = JackRussellTerrier("Miles", 4)
 miles.speak()
'Miles barks: Arf'



























































