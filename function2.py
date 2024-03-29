def add():
    num1, num2, num3 = 10, 20, 50
    sum = num1 + num2
    print(sum)

add()

# creating a dynamic function
def add1(num1,num2):
    sum = num1 + num2
    print(sum)

add1(100,50)
add1(200,45)


def sub1(num,num2):
    sub = num - num2
    print(sub)
sub1(95,60)
def multi1(num1, num2):
    mul = num1 * num2
    print(mul)
multi1(12,10)

def div(num1,num2):
    div = num1 / num2
    print(div)
div(120,12)

def mod(num1,num2):
    modulo = num1 % num2
    print(modulo)
mod(155,10)

def exp(num1,num2):
    exp = num1 ** num2
    print(exp)  

exp(2,3)

def floordiv(num1,num2):
    floordiv = num1 // num2
    print(floordiv)

floordiv(100,3)

def multidata(num1, num2,name,flt):
    print(num1)
    print(num2)
    print(name)
    print(flt)

multidata(100,3,"branie",10.2)


def multidata(gender, age,name,flt,int):
    print(gender)
    print(age)
    print(name)
    print(flt)
    print(int)

multidata("female",12,"branie",10.2,100)