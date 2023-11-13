sum = cont = 0
while True:
    num = int(input('What multiplication table do you want?(negative to stop):'))
    print('-'*30)
    if num < 0:
        break
    while cont<=10:
        sum=num*cont
        print(f'{num}*{cont}={sum}')
        cont+=1
    cont=0
    print('-'*30)
print('Finished Program')