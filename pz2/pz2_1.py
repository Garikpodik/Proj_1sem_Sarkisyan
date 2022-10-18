a=input('Введите число больше 999')
while type(a)!=int():
    try:
        a=int(a)
        if a > 999:
            print(a//100%10)
            break
        else:
            print('Число должно быть больше 999')
            continue
        break
    except ValueError:
        print('неправильно ввели')
        a = input('Введите число больше 999')
