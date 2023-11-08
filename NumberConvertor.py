num1=int(input('Type an integer number:'))
print('Wha the conversion do you want? ')
print('[1] binary')
print('[2] octal')
print('[3] hexadecimal')
base=int(input('What base do you want?:'))
if(base==1):
    print('{} converterd on binary is: {}'.format(num1,bin(num1)[2:]))
elif(base==2):
    print('{} converterd on octal is: {}'.format(num1,oct(num1)[2:]))
elif(base==3):
    print('{} converted on hexadecimal is: {}'.format(num1,hex(num1)[2:]))
else:
    print('The number isn\' in the data base')