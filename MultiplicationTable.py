number=int(input('Which number do you want to know the multiplication table of?'))
for c in range(1,11): #a segunda virgula faz ele saltar de 5 em 5
    print('{} x {:2} = {}'.format(number,c,number*c))