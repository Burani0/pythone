class Animal:
    name = ""
    def eat(self):
        print('I can eat')


#dog is a sub class of animal 
#animal iis the parent class of dog

class Dog(Animal):
    def display(self) :
        print("My name is" , self.name)
        print(f'My name is {self.name}')

gshepherd = Dog()
gshepherd.name = 'police'
print(gshepherd.name)
print(gshepherd.display())
print(gshepherd.eat())


#assignment
# create 3 super classes with corresponding atlest 2 sub classes from each and create 3 objects from each of them them

   
