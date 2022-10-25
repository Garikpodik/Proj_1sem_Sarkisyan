a=input('Введите число больше 999')
while type(a)!=int:
    try:
        a=int(a)
    except ValueError:
        print('неправильно ввели')
        a = input('Введите число больше 999')

if a > 999:
     print(a//100%10)
else:
        print('Число должно быть больше 999')