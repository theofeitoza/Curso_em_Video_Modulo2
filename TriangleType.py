line1 = float(input('Enter the size of the first straight line:'))
lin2 = float(input('Enter the size of the second straight line:'))
line3 = float(input('Enter the size of the third straight line:'))
if line1+lin2 > line3 and line1+line3 > lin2 and lin2+line3 > line1:
    if line1 == lin2 == line3:
        print('The straight lines can form an equilateral triangle')
    elif line1 == lin2 != 3 or line1 == line3 != lin2 or lin2 == line3 != line1:
        print('Lines can form an isosceles triangle')
    else:
        print('The lines can form a scalene triangle')
else:
    print('This lines cannot form a triangle')
