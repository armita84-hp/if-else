age=int(input("age="))
if age>=18:
    print('you can vote!')
else:
    years=18-age
    print(f'you have to wait for {years} years/year so that you can vote!')