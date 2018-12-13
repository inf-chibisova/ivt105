# a = input()
# s = [a] # Зачем делать так, когда можно упороться и сделать так \/ :D

a = [int(s) for s in input("Введите числа разделяя их пробелами: ").split()] 
n = 1

while n < len(a):
     for i in range(len(a)-n):
          if a[i] > a[i+1]:
               a[i], a[i+1] = a[i+1], a[i]
          # print("For: ", a ,"While: ", n) #отладка
     n +=1

print(*a)

# a = input()
# a = a.split()
# a.sort()
# print(*a)
# Ммм. Я тут увидел что знак * преобразует список в строку но так и не нашел почему :D
# a = [int(s) for s in input("Number: ").split()]
# a.sort()
# print(*a)