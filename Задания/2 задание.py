while (True):
    Zadanie = input("\nТекстовая помощь: help\nВведите команду или номер задания: ")
    if Zadanie == 'help':
        print("_____________________________________\nhelp - Подсказки.\nexit/0 - Выход из цыкла.\n0-8,10-12 - номера заданий. Вводить только одно число!\n")
    elif Zadanie == 'exit' or '0':
        break

    elif Zadanie == '1':     
        #1 Задание
        print("\n")

        b = int(input("Введите второе число: "))
        a = int(input("Введите первое число: "))
        c = int(input("Введите Третъе число: "))
        if a > 0 and b > 0 and c > 0:
            print("Сумма трёх положительных чисел: ", a + b + c)
        if a < 0 and b > 0 and c > 0:
            print("Сумма двух положительных чисел: ", b + c)
        if a > 0 and b < 0 and c > 0:
            print("Сумма двух положительных чисел: ", a + c)
        if a > 0 and b > 0 and c < 0:
            print("Сумма двух положительных чисел: ", b + a)

    elif Zadanie == '2':
        #2 Задание
        print("\n")

        a = int(input("Введите первый угол: "))
        b = int(input("Введите второй угол: "))
        c = int(input("Введите третий угол: "))
        if a==90:
            print('У треугольника есть прямой угол.')
        elif b==90:
            print('У треугольника есть прямой угол.')
        elif c==90:
            print('У треугольника есть прямой угол.')
        else:
            print("Прямоугольник не прямоугольный. Логично.")

    elif Zadanie == '3':
        #3 Задание
        print("\n")

        x = int(input("Введите координату x: "))
        y = int(input("Введите координату y: "))
        if x > 0 and y > 0:
            print('1 четверть')
        if x > 0 and y < 0:
            print('4 четверть')
        if x < 0 and y > 0:
            print('2 четверть')
        if x < 0 and y < 0:
            print('3 четверть')

    elif Zadanie == '4':
        #4 Задание
        print("\n")

        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        c = int(input("Введите третье число: "))
        if a < b < c:
            print("Среднее число: ",b)
        elif a < c < b:
            print("Среднее число: ",c)
        elif c < b < a:
            print("Среднее число: ",b)
        elif b < c < a:
            print("Среднее число: ",c)
        elif b < a < c:
            print("Среднее число: ",a)
        elif c < a < b:
            print("Среднее число: ",a)

    elif Zadanie == '5':
        #5 Задание
        print("\n")

        m = int(input("Введите число: "))
        k = m % 10
        if (m > 9)and(m < 20)or(m > 110) and (m < 120) or(k > 4)or(k == 0):
            print(m, "лет")
        else:
            if k == 1:
                print(m, "год")
            else:
                print(m, "года")

    elif Zadanie == '6':
        #6 Задание
        print("\n")

        m = int(input("Введите число: "))
        k = int(len(str(m)))
        if (m > 0):
            print("Число положительное")
        elif (k == 1):
            print("Число однозначное")
        elif (k == 2):
            print("Число двузначное")
        elif (k == 3):
            print("Число трёхзначное")
        elif (k > 3):
            print("Число многозначное")
        if (m < 0):
            print("Число отрицательное")
        elif (k == 1):
            print("Число однозначное")
        elif (k == 2):
            print("Число двузначное")
        elif (k == 3):
            print("Число трёхзначное")
        elif (k > 3):
            print("Число многозначное")
        if (m == 0):
            print("Ноль")

    elif Zadanie == '7':
        #7 Задание
        print("\n")

        m = int(input("Введите возраст: "))
        if (m>0) and (m < 18) or(m > 59):
            print("Вы находитесь в непризывном возрасте")
        if (m >= 18) and (m <= 27 ):
            print("Вы подлежите призыву на срочную службу или можете служить по контракту")
        if (m >= 28) and (m <=59):
            print("Вы можете служить по контракту")
        if (m>100) or (m<=0):
            print("ОШИБКА!")

    elif Zadanie == '8':
        #8 Задание
        print("\n")

        a = int(input("Число a: "))
        b = int(input("Число b: "))
        n = int
        if (a%2 == 1):
            n = a+b
            print(n)
        else:
            n = a*b
            print(n)

    elif Zadanie == '9':
        print("Данное задание делается в отдельном файле!")

    elif Zadanie == '10':
        #10 Задание
        print("\n")

        n = int(input("Введите 3х-значное число"))
        print("Верно ли, что все цифры в этом числе различные?")
        a = n%10
        b = n//100
        c = (n//10)%10
        if a!=b and a!=c and b!=c:
            print("Да")
        else:
            print("Нет")

    elif Zadanie == '11':
        #11 Задание
        print("\n")

        n = int(input("Введите число"))
        m = 0
        l= n
        while m==0:
            if(n%10)>m:
                m = n%10
                n = n //10
            if n==0:
                break
        print("В числе {} самая большая цифра: {}" .format(l,m))

    elif Zadanie == '12':
        #12 Задание
        print("\n")

        m = int(input("Введите число секунд: "))
        k = m // 3600
        f = k%10
        if (k > 9)and(k < 20) or (k > 110) and (k < 120) or (f > 4) or (f == 0):
            print(k, "часов")
        elif f == 1:
            print(k, "час")
        else:
            print(k, "часа")

    else: 
        print("\n!!!Я не знаю такую комманду/задание.!!!")