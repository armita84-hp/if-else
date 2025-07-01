the_price=int(input('p='))
if the_price>300:
    d=10/100*the_price
    discount=the_price-d
    print(discount)
else:
    no_discount=the_price
    print(no_discount)
print("the actual price:",the_price,'\n','the amount of discount:',d,'\n','the price with discounr:',discount)
