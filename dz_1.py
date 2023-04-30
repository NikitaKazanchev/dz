# 1) Напишите программу, которая получает на вход список чисел и выводит на экран сумму их квадратов.
list_of_numbers = input().split()
sum = 0
for i in list_of_numbers:
    sum += int(i)**2
print(sum)


# 2) Напишите программу, которая получает на вход строку и выводит на экран все слова, начинающиеся на букву "a".
a = input("Введите текст: ").lower().split()
b = []
for i in a:
    if i[0] == 'а':
        b.append(i)
print(b)


# 3) Напишите программу, которая получает на вход два списка чисел и выводит на экран их общие элементы.
a, b = input().split(), input().split()
c = []
for i in a:
    if i in b:
        c.append(i)
print(c)


# 4) Напишите программу, которая получает на вход словарь с именами и возрастами людей, и выводит на экран имена всех людей, возраст которых больше 18 лет.
people = [
    {'name': "Анна", 'age': 23},
    {'name': "Григорий", 'age': 2},
    {'name': "Виктория", 'age': 36},
    {'name': "Игорь", 'age': 15},
    {'name': "Жора", 'age': 44},
    {'name': "Инна", 'age': 12},
]

name = []
for human in people:
    if human['age'] > 18:
        name.append(human['name'])
print(name)


# 5) Напишите программу, которая получает на вход список строк и выводит на экран самую длинную строку в списке.
a = input("Введите текст: ").split()
b = ""
for i in a:
    if len(i) > len(b):
        b = i
print(b)


# 6) Напишите программу, которая получает на вход список чисел и возвращает список из тех же чисел, но без повторений.
a = input("Введите число: ").split()
b = list(map(int, a))
c = []
for i in b:
    if i not in c:
        c.append(i)
print(c)


# 7) Напишите программу, которая получает на вход два списка чисел и возвращает список из всех элементов, которые есть только в одном из списков.
a, b = input().split(), input().split()
a, b = list(map(int, a)), list(map(int, b))
print(a)  # тут не понял задания


# 8) Напишите программу, которая получает на вход список слов и выводит на экран количество различных слов в списке.
a = input("Введите текст: ").split()
c = []
for i in a:
    if i not in c:
        c.append(i)
print(len(c))


# 9) Напишите программу, которая получает на вход строку и выводит на экран все символы, которые встречаются в ней более одного раза.
a = input()
set_a = set(a)
for i in set_a:
    if a.count(i) > 1:
        print(i)


# 10) Напишите программу, которая получает на вход список чисел и возвращает новый список, в котором все числа умножены на 2.
a = input().split()
a = list(map(int, a))
b = []
for i in a:
    i *= 2
    b.append(i)
print(b)


# 11) Напишите программу, которая получает на вход два списка чисел и возвращает список из всех элементов, которые есть в обоих списках.
a, b = input().split(), input().split()
a, b = list(map(int, a)), list(map(int, b))
c = a + b
print(c)        


# 12) Напишите программу, которая получает на вход список чисел и возвращает новый список, в котором все отрицательные числа заменены на нули.
a = input().split()
a = list(map(int, a))
b = []
for i in a:
    if i < 0:
        b.append(0)
    else:
        b.append(i)
print(b)


# 13) Напишите программу, которая получает на вход два списка строк и возвращает список из всех пар строк, одна из которых из первого списка, а другая - из второго списка.
a, b = input().split(), input().split()
c = []
for i in zip(a, b):
    c.append(list(i))
print(c)


# 14) Напишите программу, которая получает на вход словарь и возвращает новый словарь, в котором ключи и значения поменяны местами.
a = {
    'name': "Анна",
    'age': 23,
    'height': 172,
}

b = {}
for k, v in a.items():
    b[v] = k
print(b)


# 15) Напишите программу, которая получает на вход список чисел и выводит на экран наибольшее из них.
a = input().split()
a = list(map(int, a))
print(max(a))
