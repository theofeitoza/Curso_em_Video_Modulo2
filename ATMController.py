value = fifty = twenty = ten = one = 0
print('='*30)
print('{:^30}'.format('ATM BANK'))
print('='*30)
withdraw=int(input('What the withdraw amount? $'))
value=withdraw
while value>0:
    fifty=value//50
    value=value-(fifty*50)
    twenty=value//20
    value=value-(twenty*20)
    ten=value//10
    value=value-(ten*10)
    one=value//1
    value=value-one
print('-'*30)
print('You will receive:')
if fifty!=0:
    print(f'{fifty} bank notes of $50,00.')
if twenty!=0:
    print(f'{twenty} bank notes of $20,00')
if ten!=0:
    print(f'{ten} bank notes of $10,00')
if one!=0:
    print(f'{one} bank notes of $1,00')
print(f'Totalizing ${withdraw:.2f} to withdraw')
print('-'*30)