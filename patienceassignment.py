def tests(test1, test2):
    #.a dynamic function test has two parameters
    if test1 == test2:
        #a conditional statement that checks whether the value of the variable test1 is equal to the value of the variable test2
        return test1
    else:
        #the function will exit and return the value of test1.
        return test2
#the function will exit and return the value of test2 if the condition in the if statement is not met

test2 = int(input('Please enter Marks for test two: '))

'''
converts the user input into an integer and assigns it to the variable "test2 so if the user enters a non-integer it will convert to an integer

'''
test1 = int(input('Please enter Marks for test one: '))

def courseWrk(cswork):

    #a dynamic fuction "courseWrk has been defined and given i parameter"
    testsMark = tests(test1,test2) 
    #the tests function is assigned to the variable testsMark. So, testsMark will hold the higher of the two test scores (test1 and test2).
    avgtestsCswork = (cswork + testsMark)/2
    # this line of code computes the average of the scores obtained in the coursework (cswork) and the tests (testsMark). The result is then assigned to the variable avgtestsCswork.
    fnltestsCswork = avgtestsCswork * (40/100)
    #this line of code calculates the final coursework marks by taking 40% of the avgtestsCswork . The result is then assigned to the variable fnltestsCswork.
    print('..............................')
    #it will output a line of dots 
    print('your final coursework marks is: ', fnltestsCswork)
    print('..............................')
#these lines of code display the final coursework marks to the user and a line of dots 
cswork = int(input('Please enter your course work Marks: '))
#requires the user to input their coursework marks, converts the input into an integer, and stores the integer value in the variable cswork.
courseWrk(cswork)


