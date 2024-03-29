#defining an object in python
#if we to define a class we use a keyword class followed with a capital letter of the name of class and then a full colon

#class MyClass(object):
"""This is a class that represents something"""

class Animal:
    color = ""
    size = ""
    gender = ""
    name = ""
    sound = ""
    species = ""
    age = 0
    def feed(self):  #this is a method
        return "by chewing"

#creating an object of a class animal
cat = Animal()
cat.color = "brightgreen"
cat.size = "small"
cat.gender = "female"
cat.name = "fluffy"
cat.sound = "meow"
cat.species = "feline"
cat.age = 4

#Accesing objects 
print(f"{cat.name} is {cat.age} years old")
print(cat.name + " is " +  cat.size)
print(cat.name + " does " + cat.sound)
print(cat.name + " is " + cat.size)
print(cat.name + " is " + cat.gender)
print(f"{cat.name} is {cat.color}")
print(cat.name + " is of " + cat.species)
print(f"{cat.name} feeds {cat.feed()}")


#the below code fragment can be found in: 
#https://docs.python-guide.org/writing/structure/#docstring-summary
"""A docstring should always start on the line immediately after the definition (with one leading blank line"""

class Human:
    age = ""
    name = ""
    gender = ""
    location = ""
    color = ""
    height = ""
    weight = ""

bobo = Human()
bobo.age = 20
bobo.name = 'Bob'
bobo.gender = 'Female'
bobo.location = 'groundbreakers'

#add another take away from where we stopped and with examples in code