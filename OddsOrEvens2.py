from random import randint
sum = wins = 0
while True:
    print('-'*50)
    type=str(input('Let`s play odds or evens? Type your side:')).upper()
    num2=randint(0,10)
    num1=int(input('Type a number:'))
    sum=num1+num2
    print('-'*50)
    print(f'You played {num1} and the computer {num2}. Total of {sum}.')
    if type == 'Odds':
        if sum%2 == 0:
            print('The player won, lets play again')
            wins+=1
        else:
            print('The player lost and the game finished')
            break
    elif type == 'Evens':
        if sum%2 == 0:
            print('The player lost and the game finished')
            break
        else:
            print('The player won,lets play again')
            wins+=1
    else:
        print('The word typed wasn`t recognized')
print(f'The player lost after {wins} wins.')