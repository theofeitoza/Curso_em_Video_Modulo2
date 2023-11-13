higher=0;lower=0;sum=0;qtt=0;num=0;media=0;r='Y'
while r=='Y':
    num=int(input('Type a number: '))
    if qtt==0:
        higher=num
        lower=num
    else:
        if num>higher:
            higher=num
        if num<lower:
            lower=num
    sum+=num
    qtt+=1
    r=str(input('Do you want to continue? [Y/N]')).upper()
media=sum/qtt
print('You typed {} numbers'.format(qtt))
print('The media of them was:{}'.format(media))