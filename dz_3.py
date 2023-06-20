import time

'''Задача 1
Создать декоратор, который вычисляет и выводит (через print) время работы декорируемой функции
При каждом вызове декорируемой функции печатать имя функции и сколько она выполнялась.'''

# def calculating_the_working_time(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         res = func(*args, **kwargs)
#         end = time.time()
#         print(f'время выполнения функции {func.__name__} составляет {end-start}')
#         return res
#     return wrapper    

# @calculating_the_working_time
# def sum(x, y):
#      return x + y

# @calculating_the_working_time
# def hello_world():
#     print('Hello world')

# sum(6, 4)
# hello_world()

'''Задача 2
Изучить функцию wraps (from functools import wraps) и применить её к декоратору из прошлой задачи'''

from functools import wraps

# def calculating_the_working_time(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         res = func(*args, **kwargs)
#         end = time.time()
#         print(f'время выполнения функции {func.__name__} составляет {end-start}')
#         return res
#     return wrapper    

# @calculating_the_working_time
# def sum(x, y):
#     '''we make the addition of numbers'''
#     return x + y

# print(sum(6, 4))
# print(sum.__name__)
# print(sum.__doc__)


'''Задача 3
Создать декоратор, оптимизирующий работу декорируемой функции (без аргументов).
Декоратор должен сохранять результат работы функции на ближайшие 5 запусков и вместо выполнения функции возвращать сохранённый результат.
После 5 запусков функция должна вызываться вновь, а результат работы функции — вновь кешироваться.

Подсказка:
Создайте в декораторе переменную-кеш, сохраните в ней результат выполнения декорируемой функции.
Создайте в декораторе переменную, хранящую счётчик запросов.
Пока счётчика ниже предельного — отдавайте результат, сохранённый в кеше.
Когда число запросов к функции превысит предел и пора будет снова высчитывать результат выполнения функции — сбросьте счётчик,
выполните декорируемую функцию и заново сохраните результат её выполнения в переменную-кеш.'''

def cached(func):
    cache = {}
    counter = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal counter
        counter += 1
        cache_key = str(args) + str(kwargs)
        if counter <= 5:
            if cache_key not in cache:
                res = func(*args, **kwargs)
                cache[cache_key] = res
                return res
        else:
            counter = 0
            cache.clear()
    return wrapper
    
  
@cached
def sum(x, y=3):
    '''we make the addition of numbers'''
    return x + y

print(sum(2, 2))
print(sum(1, 8))
print(sum(2, 2))
print(sum(2, 5))
print(sum(7, 2))
print(sum(2, 5))
print(sum(3, 2))
print(sum(2, 5))
print(sum(6, 2))


'''Задача 4
Улучшить декоратор из предыдущей задачи (кеширование результата).
Добавить возможность передавать кол-во запусков, которые будут закэшированы, как аргумент декоратора'''

def number_of_cached_runs(arg):   
    def cached(func):
        cache = {}
        counter = 0
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal counter
            counter += 1
            cache_key = str(args) + str(kwargs)
            if counter <= arg:
                if cache_key not in cache:
                    res = func(*args, **kwargs)
                    cache[cache_key] = res
                    return res
            else:
                counter = 0
                cache.clear()
        return wrapper
    return cached
    
  
@number_of_cached_runs(3)
def sum(x, y=3):
    '''we make the addition of numbers'''
    return x + y

print(sum(2, 2))
print(sum(1, 8))
print(sum(2, 2))
print(sum(2, 5))
print(sum(7, 2))
print(sum(2, 5))
print(sum(3, 2))
print(sum(2, 5))
print(sum(6, 2))

'''Задача 5
Улучшить декоратор из Задачи 4
Добавить возможность кэшировать результат функции с аргументами.'''
