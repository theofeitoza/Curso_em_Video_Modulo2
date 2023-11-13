total = product = cheaper = cont =  0 #cont=continuar ; produt= produtos acima de mil ; mb=mais barato
most_cheap=' '
print('-'*30)
while True:
    price = int(input('What the product price? R$'))
    nome = str(input('What is the product name?'))
    cont+=1
    total+=price
    if price>1000:
        product+=1
    if cont==1 or price<cheaper:
        cheaper=price
        most_cheap=nome
    keep=' '
    while keep not in 'YN':
        keep = str(input('Wanna continue?(Y or N)')).upper()[0]
    if keep == 'N':
        break
    print('-'*30)
print('-'*50)    
print(f'The total was: {total}')
print(f'There was {product} products over $1,000.00')
print(f'The {most_cheap} was the cheaper product')
print('-'*50)