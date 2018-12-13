from random import randint

while (True):
    Zadanie = input("\nТекстовая помощь: help\nВведите команду или номер задания: ")
    if Zadanie == 'help':
        print("_____________________________________\nhelp - Подсказки.\nexit/0 - Выход из цыкла.\n0-8,10-12 - номера заданий. Вводить только одно число!\n")
    elif Zadanie == 'exit' or "0":
        break

    elif Zadanie == '1':     
        #1 Задание
        print("\n от 0 до 30")

        n=0
        while n <30:
            n+=2
            print(n)


    elif Zadanie == '2':
        #2 Задание
        print("\n")

        n=1
        k=n**2
        print(k)
        k=0
        while n < 15:
            n=n+2
            k=n**2
            print(k)


    elif Zadanie == '3':
        #3 Задание
        print("\n")

        n=900
        print(n)
        while n!=800:
            n = n-1
            print(n)
        n -= 99
        print("\n")
        while n!=600:
            n = n-1
            print(n)
        n -= 99
        print("\n")
        while n!=400:
            n = n-1
            print(n)
        n -= 99
        print("\n")
        while n!=200:
            n = n-1
            print(n)

    elif Zadanie == '4':
        #4 Задание
        print("\n")

        a = int(input("Начальный диапозон: "))
        b = int(input("Конечный диапозон: "))
        n = a
        sum = 0
        while n <= b:
            #print(n ** 2)
            sum += n ** 2
            n+=1
        print("сумму квадратов целых чисел в диапазоне от {} до {}: {}".format(a, b, sum))


    elif Zadanie == '5':
        #5 Задание
        print("\n")

        n = input("Факториал факториала числа ") 
        n = int(n) 
        fac = 1 
        i = 0 
        while i < n: 
            i += 1
            fac = fac * i
            k = fac
        fac = 1
        i = 0
        while i < k: 
            i += 1
            fac = fac * i
        print("равен", fac)


    elif Zadanie == '6':
        #6 Задание
        print("\n")

        a = int(input())
        b = int(input())
        c = int(input())
        d = int(input())
        e = int(input())
        if a<b<c<d<e:
            print("Мои поздравления")
        else:
            print("Ошибка!")


    elif Zadanie == '7':
        #7 Задание
        print("\n")

        number = randint(0,100)
        Shot = 0
        print("Я загадал число! Но у тебя всего 4 попытки отгадать его!\nДиапозон числа от 0 до 100")
        while Shot < 4:
            print("Как ты думаешь, какое?")
            Number_Shot = input()
            Number_Shot = int(Number_Shot)
            Shot = Shot+1
            if Number_Shot < number:
                print("Загаданное число больше твоего ;3\nПомни!")
            if Number_Shot > number:
                print("Загаданное число меньше твоего :3")
            if Number_Shot == number:
                break
        if Number_Shot == number:
            print("Превосходно! Ты угадал число с {} попытки." .format(Shot))
        if Number_Shot != number:
            print("У тебя не осталось попыток. Я загадал число{}.Ты проиграл!" .format(number))

    elif Zadanie == '8':
        #8 Задание
        print("\n")

        x=int(input("Сколько рублей у Васи?: "))
        y=int(input("Сколько стоит мороженое?: "))
        k=x//y
        while x >= y:
            x=x-y
        print("Сколько осталось денег у Васи?:  {}".format(x))
        print("Сколько съест мороженных?: {}" .format(y))


    elif Zadanie == '9':
        #9 Задание
        print("\n")

        n = 56
        i=0
        j=28

        while i*4+j*2 == n:
            print('{} единорогов и {} людей'.format(i, j))
            i+=1
            j=(n-4*i)//2
            if i==15:
                break

    elif Zadanie == '10':
        #10 Задание
        print("\n")

        n = int(input('Введите число: '))
        x = str(n)
        s = int(len(x))
        print(s)


    elif Zadanie == '11':
        #11 Задание
        print("\n")

        n = int(input('Введите число: '))
        summa = 0
        l = str(n)
        s = int(len(l))
        while n > 0:
            i = n % 10
            n = n//10
            summa = summa + i
        print ('Сумма чисел равна = {}'.format(summa))
        x = summa//s
        print("Средне арифметическое этих чисел: {}".format(x))


    elif Zadanie == '12':
        #12 Задание
        print("\n")

        a = randint(2,102)
        print("Рандомное число от 2 до 102: {}".format(a))

    elif Zadanie == '13':
        #12 Задание
        print("\n")

        n = int(input("Integer: "))
        factors = []
        d = 2
        m = n
        while d * d <= n:
                if n % d == 0:
                    factors.append(d)
                    n//=d
                else:
                    d += 1
        factors.append(n)
        print('{} = {}' .format(m, factors))        

    elif Zadanie == '14':
        #12 Задание
        print("\n")

        N = int(input("Введите число:"))
        sum = 0
        while N > 0:
            d = N%10
            N = N // 10
            sum += d
        print("Сумма всех цифр этого числа: {}".format(sum))

    elif Zadanie == '15':
        #12 Задание
        print("\n")

        secret = randint(9824, 9900)
        i, j = 0, 0
        x = 1
        print("1. Задумайте любое двухзначное число.")
        print("2. Вычтите из него составляющие его цифры.")
        print("3. Найдите это число в таблице и символ, которому оно соответствует.")
        print("4. Вообразите мысленно себе этот символ.")
        print("5. Нажмите Enter")
        while i<10:
            while j < 10:
                num = randint(9824, 9900)
                if (i*10+j+1)%9==0:
                    print('{}: {}' .format(x, chr(secret)), end='\t')
                else:
                    print('{}: {}' .format(x, chr(num)), end='\t')
                j += 1
                x += 1

            print()
            i += 1
            j = 0
        x = input('Проверить?')
        print("Ваш символ: {}".format(chr(secret)))

    else: 
        print("\n!!!Я не знаю такую комманду/задание.!!!")


