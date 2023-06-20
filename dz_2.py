#Задача 1 Напишите программу, которая находит все простые числа в диапазоне от 1 до N. 


n = int(input("Введите число: "))
for i in range(1, n+1):
    if i > 1: 
        for j in range(2, i):
            if i % j == 0: 
                break 
        else: 
            print(f"{i} простое число")


# #Задача 2 Напишите программу, которая находит количество пар элементов в списке, которые в сумме дают заданное значение.

def counting_pairs(n, list_number):
    s = 0
    for i in list_number:
        for j in range(1, i+1):
            if i + j == n:
                s += 1
    return s

print(counting_pairs(5, [1, 2, 3, 4, 5]))  
''' Не понимаю замечание. что тут не верно ? '''

# #Задача 3 Напишите программу, которая находит все подстроки строки, которые являются палиндромами.
text = input()
list_text = text.split()
for i in list_text:
    palindromes = ""
    for j in range(len(i), 0, -1):
        palindromes += str(i[j-1])
    if i == palindromes:
        print(f"{i} палиндромные")
    else:
        print(f"{i} Не палиндромные")
    
# #Задача 4 Напишите программу, которая находит наибольшую общую подстроку двух строк. 

a, b = input(), input()
answer = ""
len1, len2 = len(a), len(b)
for i in range(len1):
    match = ""
    for j in range(len2):
        if (i + j < len1 and a[i + j] == b[j]):
            match += b[j]
        else:
            if (len(match) > len(answer)): answer = match
            match = ""
print(answer)


# #Задача 5 Напишите программу, которая находит наименьшее число, которое делится на все числа от 1 до N.



# #1. Поиск среднего значения элементов в массиве.

list_of_numbers = [2, 5, 3, 1, 21]
sum_numbers = 0

for i in list_of_numbers:
    sum_numbers += i
print(sum_numbers / len(list_of_numbers))


# #2. Проверка, является ли число простым.
def checking_the_number(number):
    for i in range(2, number):
        if number % i == 0:
                return "Число сложное"
    return "Число простое"
    
print(checking_the_number(1))    


# #3. Нахождение самого длинного палиндрома в строке
# '''
# - узнать что такое палиндром 
# - узнать как его находят
# - разбить строку по элементам в списке
# - найти все палиндром в строке 
# - найти из них самый длинный
# '''
palindrome_text = "1221 и 74737 так же как 121 палиндромы"

list_palindrome = []
checked_list = palindrome_text.split()
for i in checked_list:
    if i == i[::-1] and len(i) > 1:
        list_palindrome.append(i)
the_longest_palindrome = ""
for j in list_palindrome:
    if len(the_longest_palindrome) != 0 and len(j) > len(the_longest_palindrome):
        the_longest_palindrome = j
    if len(the_longest_palindrome) == 0:
        the_longest_palindrome = j
print(the_longest_palindrome)


# #4. Проверка, все ли элементы в массиве уникальны (не используя set)

def checking_uniqueness(list_of_numbers):
    unique_numbers = []
    for i in list_of_numbers:
        if i not in unique_numbers:
            unique_numbers.append(i)
        elif i in unique_numbers:
            return False
    if unique_numbers == list_of_numbers:
        return True

print(checking_uniqueness([2, 5, 3, 1, 21]))


# #5. Поиск наибольшего общего делителя (НОД) двух чисел.
# '''
# - узнать что такое нод 
# - узнать как его находят
# - найти нод двух чисел
# '''
import math

def node_search(a, b):
    return math.gcd(a, b)

print(node_search(8, 12))

def node_search(a, b): 
    if a > b: 
        c = b 
    else: 
        c = a 
    for i in range(1, c + 1): 
        if a % i == 0 and b % i == 0: 
            node = i 
    return node 

print(node_search(8, 12))

def node_search(a, b):
    while a != 0 and b != 0:
        if a >= b:
            a %= b
        else:
            b %= a
    return a or b
num = node_search(8, 12)
print(num)



# #6. Поиск наименьшего общего кратного (НОК) двух чисел.

def nok_search(x, y):
    if x > y:
        greater = x
    else:
        greater = y 
    while True: 
        if greater % x == 0 and greater % y == 0:
            nok = greater 
            break
        greater += 1 
    return nok

print(nok_search(180, 72))

# #7. Вычисление факториала числа.

def factorial_search(n):
    factorial = 1
    for i in range(1,n+1):
        factorial *= i
    return factorial

print(factorial_search(8))

# #8. Поиск суммы цифр числа.

def finding_the_sum_of_a_number(n):
    sum_namber = 0
    for i in str(n):    
        sum_namber += int(i)
    return sum_namber

print(finding_the_sum_of_a_number(16567))   


# #9. Вычисление первых N чисел Фибоначи

fib1 = fib2 = 1
 
n = int(input("Номер элемента ряда Фибоначчи: "))
 
print(fib1, fib2, end=' ')
 
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')
