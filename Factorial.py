from time import sleep
num1 = int(input('Type a number to find the factorial: '))
calc=num1
result=1
print('Calculating...')
sleep(1)
while calc>0:
    print('{}'.format(calc),end='')
    print(' x ' if calc>1 else ' = ', end='')
    result*=calc
    calc-=1
print('{}'.format(result)) 