p=int(input('Type the first term of AP:'))
r=int(input('Type the rate of AP:'))
c=p
d=p+(10-1)*r
q=1
while q!=0:
    while c<=d:
        print(c, end=' ')
        c+=r
    q=int(input('\nHow much terms do you want to add?'))
    d=d+q*r
print('Finished program')