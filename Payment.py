preço=float(input('What is the product price?'))
print('Choose one of our payment methods:')
print('1 - Cash or check=10 percent discount')
print('2 - Cash on card=5 percent discount')
print('3 - Up to twice on the normal price card')
print('4 - 3x or more on card=20 percent interest')
pag=int(input('What is the payment terms?'))
if(pag==1):
    valor=preço-preço*0.1
    print('The final value of the product will be:{:.2f}'.format(valor))
elif(pag==2):
    valor=preço-preço*0.05
    print('The final value of the product will be:{:.2f}'.format(valor))
elif(pag==3):
    valor=preço
    print('The final value of the product will be:{:.2f}'.format(valor))
elif(pag==4):
    valor=preço+preço*0.2
    print('The final value of the product will be:{:.2f}'.format(valor))
else:
    ('The value entered was not recognized')