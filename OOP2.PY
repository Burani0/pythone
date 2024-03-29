class Lake:
    def __init__(self,name,location,depth,width,ltype):
        self.name = name
        self.location = location
        self.depth = depth
        self.width = width
        self.ltype = ltype

#shish method(__init__) is a special methode used to identify properties of a class
#the first property or parementr in he shish refers to an individual class and not an attribute

#creating objects of class lake
#instatiation is the creation of an object of a class
lake1=Lake("Superior", "North America","500 feet"," 500 feet","salty")
print(lake1.name)

#the shish method is called a constructer
#it is used to give objects of a created object of a class
#so the shish fuction is a constructor

class River:
    def __init__(ozzy,a,b,c):
        ozzy.name = a
        ozzy.length = b
        ozzy.location = c

river=River("R.Nile","600km","central")