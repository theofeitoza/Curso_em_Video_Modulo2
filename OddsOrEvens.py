num=1
odds=evens=0
while num!=0:
    num=int(input('Type a number: ')) 
    if num!=0:
        if num%2==0:
            odds+=1
        else:
            evens+=1
print(f'You typed {odds} odds and {evens} evens')