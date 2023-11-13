num = int(input('Type the quantity of number: '))
c = 1
f = 0
p = 1
print('~'*30)
print('{} '.format(f), end='')
while c < num:
    f = f+p
    print('>{}'.format(f), end=' ')
    p = f-p
    c += 1
print('\n','~'*30)