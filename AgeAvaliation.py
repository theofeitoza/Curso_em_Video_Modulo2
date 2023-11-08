average = 0
older = 0
young_woman = 0
for c in range(0, 4):
    name = str(input('Qual seu nome:'))
    age = int(input('Qual sua idade:'))
    sex = str(input('Qual seu sexo?(M ou F)'))
    if (sex == 'M' and age > older):
        older = age
        nmv = name
    elif sex == 'F' and age < 20:
        young_woman = young_woman+1
    average = average+age
average = average/4
print('The average age is: {}'.format(average))
print('The name of the older man is: {}'.format(nmv))
print('{} womens younger than 20 years'.format(young_woman))