def net_pay(salary, nssf_rate, paye_rate):
    nssf = (nssf_rate / 100) * salary
    paye = (paye_rate / 100) * salary
    netpay = salary - nssf - paye
    print("Your Net Pay is", netpay)

salary = float(input("Please enter your salary: "))
nssf_rate = float(input("Please enter your NSSF rate in percentage: "))
paye_rate = float(input("Please enter your PAYE rate in percentage: "))

net_pay(salary, nssf_rate, paye_rate)
