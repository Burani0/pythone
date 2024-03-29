#datatypes in python
#numeric
#string
#sequence type
#mapping
#boolean
#set

#Numeric: we have integers (int), float(float), Complex numbers(complex)
#examples:
num1=10
print(num1, "is of a type", type(num1))
num2=100.0
print(num2, "is of a type", type(num2))


num3 = 1+2j
print(num3, "is of a type", type(num3))

num4 = 1+2j
print(num4, "is of a type", type(num4))

#strings (a string is a serie of character)
name = "burani" #or 'burani'
print(name, "is a type", type(name) )
#semantics is the meaning of what you have written
#typecasting
numx = "20"
print(numx, "is of a type", type(numx))
#example of typecasting
numy = str(numx) #conversion of the value of numx into an interger and store it in a varial
print(numy, "is of a type", type(numy))
numx = "20"
print(numx, "is of a type", type(numx))
#example of typecasting
numy = float(numx) #conversion of the value of numx into an interger and store it in a varial
print(numy, "is of a type", type(numy))
numx = "20"
print(numx, "is of a type", type(numx))
#example of typecasting
numy = int(numx) #conversion of the value of numx into an interger and store it in a varial
print(numy, "is of a type", type(numy))



#sequence data type
#under sequence, we have lists, tuples, and range
#list is a variable that ccaan store more than one value
#however we can have more than one list and we can store  values later on

mylist = []
mylist.append("burani")
print(mylist)  
mylist.append(15)
print(mylist)

#append is a specialised command in py used to add valyes to a list
#print is a specialised command in py used to add to output values on a computer screen
#pop is uesd to remove the last value of the list
languages=["python", "javascript", "ruby", "cobol", "julia", "swift"]
print(languages[5])
print(languages[0])
print(languages[1])
print(languages[2])
print(languages[-1])

country=["uganda", "kenya", "tanzania",["egypt","somalia",["sudan",["burundi",["Togo"],["Benin"]]]]]
print(country[-1][-1])
print(country[3][2][0])
print(country[3][2])
print(country[-1][-1][-1])
print(country[-1][-1][-1][-1])
print(country[-1][-1][-1][-2])
print(country[-1][-1][-1][-2][-1])
print(country[3])
country.append(10)
print(country)

fruits = ("apples","mangoes","oranges",["pawpaws","pears"])
print(fruits[0])
print(fruits[-3])
print(fruits[-1][-1])
print(fruits[3][1])

#a list is mutable data type because it can be manipulated after it has been created
#tuples are imutable data types meaning one you create them with elements they can't be changed
#tuples can be type casted thus you can change a list into a tuple but you can't change a tupple to a list

 #mapping
person = {"name": "branie", "age":6, "country":"United States", "height":171}
print (person["name"])
print (person.keys())
print (person.values())


#sets
student_id = {122 ,233,344,455,566,577}
print(student_id)
print(student_id)
print(type(student_id))

 
for keys, value in person.items(): 
    print(keys,value)

lakes = {"name:":"victoria", "width:":9990, "location:":"southeast", "country:":"Uganda"}
for keys, value in lakes.items(): 
    print(keys,value)
    