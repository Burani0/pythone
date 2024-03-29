def user_info(name,age,email,gender):
    name = input("Please enter your name: ")
    age = input("Please enter your age: ")
    email = input("Please enter your email: ")
    gender = input("Please enter your gender: ")
    
    
    print(name)
    print(age)
    print(email)
    print(gender)
user_info("name","age","email","gender")

def net_pay(salary, nssf_rate, paye_rate):
    nssf = (nssf_rate / 100) * salary
    paye = (paye_rate / 100) * salary
    netpay = salary - nssf - paye
    print("Your Net Pay is", netpay)

salary = float(input("Please enter your salary: "))
nssf_rate = float(input("Please enter your NSSF rate in percentage: "))
paye_rate = float(input("Please enter your PAYE rate in percentage: "))

net_pay(salary, nssf_rate, paye_rate)








