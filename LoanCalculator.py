cost = float(input('What is the house cost? R$'))
salary = float(input('What\' is the persos salary? R$'))
year = int(input('How much years to pay?'))
month = year*12
loan = cost/month
max = salary*0.3
if(loan<max):
    print('The loan was approved and the quota will be ${:.2f}'.format(cost*0.3))
else:
    print('The loan was denied because the quote will be on ${:.2f}'.format(loan))