#a named block of code is called a function.
#<s>A function can be thought of as a box that contains
# a set of statements to be executed together, with an optional name by which the box
# can be referred to from outside the function.
#def my_function():  # this line defines a new function called "my_function
#print("Hello World!")   # this statement is inside the function and will be printed when 
#it runs
# indentation matters in Python - it shows where the group of statements belongs to
#print("Hello World!")
#end of definition
#calling a function:
#def my_function()    # you don't need to call your own functions, but if you do
#                      # you must put parentheses after the function name
#my_function()       # this calls the function (i.e., executes its code)

def myfunction():
    num1, num2 = 20, 40
    print(num1 + num2)
myfunction()

#we have 2 types of functions namely static and dynamic functions
#static functions are known as simple functions or regular
#functions in python. They don’t take any special action before executing their code.

def condition():
    number = 10
    if number > 0:
        print("number is positive")
    print("if statement is easy") # from ln 26 to ln 29 its a function definition

condition()

# below code has been executed from the above fuction
number = 10
if number > 0:
    print("number is positive")
  
number = 40
if number > 0:
    print("number is your age")
print("not really")



# calling of a fuction is called invoke just like in ln 46
#condition()

"""
fuction condition(){
    this how they write in js 
}"""

def mycondition():
    number = 10
    if number > 0:
        print("positive is number")
    else:
        print("negative is number")
    print("this statement is not related to if or else but in the same function")

mycondition()
