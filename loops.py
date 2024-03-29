def loop():
    list = [10,20,30,40,50,]
    for item in list:
        print(item)

#loop is a mechanism or a way or a means of writing instructions to a computer to repeatedly do an action
# below is an iteration of values in a list of numbers
  
       

def loop2():
    for i in range (10):
        print(i)
        item = 1

def loop3():
    for item in range (1,10):   # 1 represents the start and 10 represents the end of the list 
         print(item)
# range is a keyword in python
# loops are very costly in terms of memory consumption
#Two types of loops, that is for loop and while loops are expensive in terms of memory consumption
# In Python, there are two kinds of loops

def loop4():
    for i in range(1,20):
        if i % 2 == 0 :
           print(i)

def loop5():
    for i in range(1,20):
        if i % 2 != 0 :
           print(i)

#a block of code is a collection of related statements 
# a block of code is identation

def loop6():
    digits = [66, 88,99,11]      
    for i in digits:
        print(i)
    else:
        print("No items left")

loop()

loop2()

loop3()     

loop4()    

loop5()         

loop6()                            
    


    