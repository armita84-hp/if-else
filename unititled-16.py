price=int(input('price='))
if price>70:
    c=price-price*20/100
    print(f'you have 20 percent off \n the price will be {c}')
elif price>50:
    d=price-price*10/100
    print(f'you have 10 percent off \n the price will be {d}')
else:
    print(f'the price is {price}')