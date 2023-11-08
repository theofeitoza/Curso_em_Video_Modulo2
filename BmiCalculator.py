weight=float(input('What is your weight in kg?'))
height=float(input('How tall are you in meters??'))
bmi=weight/(height**2) #poderia adicionar a biblioteca math porém não quis
if(bmi<18.5):
    print('You are underweight')
elif(bmi>=18.5 and bmi<25):
    print('You are at your ideal weight')
elif(bmi>25 and bmi<30):
    print('You are overweight')
elif(bmi>30 and bmi<40):
    print('You are obese')
else:
    print('You are morbidly obese')