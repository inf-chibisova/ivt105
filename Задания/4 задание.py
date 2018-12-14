while (True):
    Zadanie = input("\nТекстовая помощь: help\nВведите команду или номер задания: ")
    if Zadanie == 'help':
        print("_____________________________________\nhelp - Подсказки.\nexit/0 - Выход из цыкла.\n0-10 - номера заданий. Вводить только одно число!\n")
    elif Zadanie == 'exit' or Zadanie == "0":
        break

    elif Zadanie == '1':     
        #1 Задание
        print("\n")

        a = input("Введите фамилию: ")
        b = input("Введите имя: ")
        c = input("Введите отчество: ")
        print(a, b[0]+".", c[0]+".")


    elif Zadanie == '2':
        #2 Задание
        print("\n")

        print ( "Введите имя, отчество и фамилию: " ) 
        s = input() 
        n = s.find ( " " ) 
        name = s[:n] 
        s = s[n+1:]
        n = s.find ( " " ) 
        name2 = s[:n] 
        s = s[n+1:]
        s = name + " " + name2[0] + "." + s[0] + "." 
        print ( s ) 


    elif Zadanie == '3':
        #3 Задание
        print("\n")

        s = input()
        count = 0
        flag = 0
        for i in range(len(s)):
            if s[i] != ' ' and flag == 0:
                count += 1
                flag = 1
            else:
                if s[i] == ' ':
                    flag = 0
        print(count)

    elif Zadanie == '4':
        #4 Задание
        print("\n")
                
        s = str(input("Введите сообщение(Ограничение в 10 символов):"))
        a=int(len(s))
        if a > 10:
            x=a-10
            print('Вы написали на {} символов больше'.format(x))



    elif Zadanie == '5':
        #5 Задание
        print("\n")

        a = input("Сколько звёзд на небе?")
        b = input("Сколько листьев на дереве?")
        c = input("Почему в трамвайных поручнях не живут тараканы?")
        print(a.isdigit())
        print(b.isdigit())
        print(c.isalpha())

    elif Zadanie == '6':
        #6 Задание
        print("\n")

        s = input("Введите пример с использованием скобок: ")
        x = s.count("(")
        y = s.count(")")
        if x==y:
            print('Отлично! Ты не забыл не одну скобку! \nА ты думал что я его считать буду? Ха. Наивный.')
        else:
            print('Ошибка... Ты где-то потерял скобку... И как мне считать?')


    elif Zadanie == '7':
        #7 Задание
        print("\n")

        s = str(input("Введите слово в котором надо посчитать кол-ов букв: "))
        x = int(s.count(""))-1
        print("В слове {} букв" .format(x))


    elif Zadanie == '8':
        #8 Задание
        print("\n")

        Text = input("Введите сообщение: ")

        print("Столько слов начинаются с большой буквы: ", sum(1 for c in Text if c.isupper()))

    elif Zadanie == '9':
        #9 Задание
        print("\n")

        s = (list(input("Введите предложение: ")))
        l = len(s)
        Word_hight = 0
        Word_id = 0
        count = 0
        i = 0
        while i < l:
            if s[i] != ' ':
                count += 1
            else:
                if count > Word_hight:
                    Word_hight = count
                    Word_id = i - count
                count = 0
            i += 1
        
        if count > Word_hight:
            Word_hight = count
            Word_id = i - count
        
        Word_id_end = Word_id + Word_hight
        while Word_id < Word_id_end:
            if s[Word_id] == 'а':
                s[Word_id] = 'б'
            Word_id += 1
        
        s1 = ''
        for i in s:
            s1 += i	
        print(s1)

    elif Zadanie == '10':
        #10 Задание
        print("\n")

        s = input("Введите текст: ")

        n = len(s.split())-1
        s = s.replace('\n', ' ')
        s = s.replace('\r', ' ')
        n1 = len(s)
        s = s.replace(' ', '')
        n2 = len(s)

        print('-'*50)
        print(s)
        print('-'*50)

        print('Количество символов с пробелами: '+str(n1))
        print('Количество символов без пробелов: '+str(n2))
        print('Количество слов: '+str(n))

    else: 
        print("\n!!!Я не знаю такую комманду/задание.!!!")