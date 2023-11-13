first_term=int(input('Type the first term of AP:'))
ratio=int(input('Type the rate of the AP:'))
calc=first_term
last_term=first_term+(10-1)*ratio
while calc<=last_term:
    print(calc,'-',end=' ')
    calc+=ratio