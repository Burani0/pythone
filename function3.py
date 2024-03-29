#functions are self contained block of code
#values inside the fuction parathesis is called parameters
def add(a,b):
    ans = a + b
    print(ans)

age = 16

def add1(a,b):
    ans = a + b + age
    age1 = 100
    print(ans)
    print(age1)
#print(ans) 
#this will give an error as 'ans' is not defined in the global scope. It is only defined inside the functions.return ans
#fuctions are self contained because variables inside cannot be acessed from outside of the function
#

add1(20,10)
