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

#2 Задание
print("\n")

a = int(input())
b = int(input())
c = int(input())
if a==90:
    print('a')
elif b==90:
    print('b')
elif c==90:
    print('c')

#3 Задание
print("\n")

x = int(input())
y = int(input())
if x > 0 and y > 0:
    print('1')
if x > 0 and y < 0:
    print('4')
if x < 0 and y > 0:
    print('2')
if x < 0 and y < 0:
    print('3')

#4 Задание
print("\n")

a = int(input())
b = int(input())
c = int(input())
if a < b < c:
    print(b)
elif a < c < b:
    print(c)
elif c < b < a:
    print(b)
elif b < c < a:
    print(c)
elif b < a < c:
    print(a)
elif c < a < b:
    print(a)

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
print("В числе", l, "самая большая цифра –", m, ".")

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
