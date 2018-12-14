while (True):
    Zadanie = input("\nТекстовая помощь: help\nВведите команду или номер задания: ")
    if Zadanie == 'help':
        print("_____________________________________\nhelp - Подсказки.\nexit/0 - Выход из цыкла.\n0-10 - номера заданий. Вводить только одно число!\n")
    elif Zadanie == 'exit' or Zadanie == "0":
        break

    elif Zadanie == '1':     
        #1 Задание

        Name = input("Your name: ")
        print("Hello, {}".format(Name))

    elif Zadanie =='2':
        #2 Задание
        print("\n")

        print('''Ага!
Я могу управлять этим компьютером!
Вот только зачем? :'C
Пойду поищу смысл жизни "__"''')

    elif Zadanie == '3':
        #3 Задание
        print("\n")

        print("Задайте последовательно 3 числа: ")
        a = int(input("Первое число: "))
        b = int(input("Второе число: "))
        c = int(input("Третье число: "))
        print("Сумма чисел: {}" .format(a + b + c))

    elif Zadanie == '4':
        #4 Задание
        print("\n")

        radius = int(input("Радиус: "))
        x = 3.14
        pi = x 
        area = pi * radius **2
        print(area)

    elif Zadanie == '5':
        #5 Задание
        print("\n")

        Radius5 = float(input("Введите радиус: "))
        print(Radius5)

    elif Zadanie == '6':
        #6 Задание
        print("\n")

        All_Apple = int(input("Всего яблок: "))
        All_People = int(input("Всего школьникво: "))
        Ostat = All_Apple % All_People
        Seil = int(All_Apple / All_People)
        print("{} осталось в корзине, и по {} яблока съели школьники" .format(Ostat, Seil))

    elif Zadanie == '7':
        #7 Задание
        print("\n")

        n = int(input('Введите количество минут: '))
        print('Прошло суток: ', n//1440)
        print('Прошло часов: ', n//1440//60)
        print('Прошло минут: ', n%60)

    elif Zadanie == '8':
        #8 Задание
        print("\n")

        first = input("Первая переменная: ")
        second = input("Вторая переменная: ")
        first, second = second, first
        print("Первая переменная: {} \nВторая переменная: {}".format(first,second))

    elif Zadanie == '9':
        #9 Задание
        print("\n")

        lenght = int(input("Введите длину одной из стороны квадрата: "))
        print("Периметр: {}см,\nПлощадь: {}см,\nДиагональ: {}см".format(lenght*4, lenght**2, lenght*2**(1/2)))

    elif Zadanie == '10':
        #10 Задание
        print("\n")

        num = input("Введите число: ")
        num *= 15
        num = int(num)
        print(num**2)

        #Или

        print(int(input("Введите число: ") * 15) ** 2)

    else: 
        print("\n!!!Я не знаю такую комманду/задание.!!!")