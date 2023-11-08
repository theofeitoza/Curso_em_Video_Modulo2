from datetime import date
born=int(input('When you were born?'))
typed_year=date.today().year
typed_date=typed_year-born
if typed_date==18:
    print('You need to enlistment')
elif typed_date<18:
    print('You will need to enlistment soon')
elif typed_date>18:
    print('Passed {} years of the enlistment'.format(typed_date))
