calc = 0
num1 = int(input('Type the first number: '))
num2 = int(input('Type the first number: ')) 
while calc != 5:
    print('-'*20)
    print('[1] sum\n[2] multiply\n[3] higher\n[4] new numbers\n[5] Exit')
    print('-'*20) 
    calc = int(input('What option do you want? '))
    if calc == 1:
        print('The su  is: {}'.format(num1+num2))
    elif calc == 2:
        print('The multiplication is: {}'.format(num1*num2))
    elif calc == 3:
        if num1 > num2:
            print('The higher number is: {}'.format(num1))
        else:
            print('The higher number is: {}'.format(num2))
    elif calc == 4:
        print('Type the numbers again')
        num1 = int(input('Type the first number: '))
        num2 = int(input('Type the second number: ')) 
print('Finished program')