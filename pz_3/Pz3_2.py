
#даны два числа. вывести большее из них
a=input('Введите первое число')
b=input('Введите второе число')
while type(a)!=int() and type(b)!=int():
    try:
        a!=int(a)
        b!=int(b)
        print(max(a,b))
        break
    except ValueError:
        print('неправильно ввели')
        a = input('Введите трехзначное число:')
        b = input('Введите трехзначное число:')
        break