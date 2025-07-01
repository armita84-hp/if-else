a=input('a=')
b='@'
if b in a:
    if len(a)>6:
        print('password is good')
    else:
        print('password is not too long')
else:
    print('password is incorect')