#how to make fuctions communicate
def vat(rate,price):
    frate = ((rate/100) * price)
    return frate

def net_price():
    actvat = vat(18,20000)
    print(actvat)
    actprice = 20000 + actvat
    print(actprice)

net_price()

# 18,20000 are arguments
#price and rate are parameters of the function vat.
#return is the last statement to be exected in a function

# assignmment
# using paramentalized functions create three fuctions that share the same function name but take different number of arguments:
#two of them should be dynamic
#last one should be receiving values from the first two.

#from then and now what are your learning take aways with examples in code

#python is extreamly moduler and object oriented


