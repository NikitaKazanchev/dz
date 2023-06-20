#Создайте класс "Сотрудник" (Employee) с атрибутами "имя" (name), "возраст" (age) и "зарплата" (salary). Добавьте метод "получить_информацию" (get_info), который будет выводить 
#информацию о сотруднике (имя, возраст и зарплата).

# class Employee:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary

#     def get_info(self):
#         print(f'сотрудник - {self.name}, возраст - {self.age}, зарплата - {self.salary}')

# employee = Employee('Никита', 34, 50000)
# employee.get_info()

#Создайте класс "Прямоугольник" (Rectangle) с атрибутами "длина" (length) и "ширина" (width). Добавьте метод "площадь" (area), который будет возвращать площадь прямоугольника, и метод 
#"периметр" (perimeter), который будет возвращать периметр прямоугольника.

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return f'Площадь прямоугольника  = {self.length * self.width}'
    
#     def perimeter(self):
#         return f'Периметр прямоугольника  = {2 * (self.length + self.width)}'
    
# rectangle = Rectangle(7, 4)
# print(rectangle.area())
# print(rectangle.perimeter())

#Создайте класс "Круг" (Circle) с атрибутом "радиус" (radius). Добавьте метод "площадь" (area), который будет возвращать площадь круга, и метод "длина_окружности" (circumference), 
#который будет возвращать длину окружности.
#import math

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return f'Площадь курга  = {math.pi * (self.radius**2)}'
    
#     def circumference(self):
#         return f'Длина окружности = {2 * math.pi * self.radius}'
    
# circle = Circle(5)
# print(circle.area())
# print(circle.circumference())

#Создайте класс "Автомобиль" (Car) с атрибутами "марка" (brand), "модель" (model) и "год_выпуска" (year). Добавьте метод "описание" (description), который будет выводить 
#полное описание автомобиля (марка, модель и год выпуска).

# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def description(self):
#         return f'Автомобиль марки - {self.brand}, модель - {self.model}, год выпуска - {self.year}'
    
# car = Car('hyundai', 'ix35', 2013)
# car2 = Car('hyundai', 'sonata', 2015)
# print(car.description())
# print(car2.description())


#Создайте класс "Банковский счет" (BankAccount) с атрибутами "владелец" (owner) и "баланс" (balance). Добавьте методы "пополнить" (deposit), который будет увеличивать баланс 
#на определенную сумму, и "снять" (withdraw), который будет уменьшать баланс на определенную сумму. 
#Также добавьте метод "получить_баланс" (get_balance), который будет возвращать текущий баланс.

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self,entrance):
#         self.balance = self.balance + entrance
#         return self.balance

    
#     def withdraw(self, minus_amount):
#         self.balance = self.balance - minus_amount
#         return self.balance
    
#     def get_balance(self):
#         return self.balance
    
# bank_account = BankAccount('Nikita', 120000)

# print(bank_account.deposit(1000))
# print(bank_account.withdraw(1))
# print(bank_account.get_balance())


#Создайте базовый класс "Фигура" (Shape) с методом "вычислить_площадь" (calculate_area). Создайте подклассы "Прямоугольник" (Rectangle) и "Круг" (Circle), которые наследуются от класса "Фигура".
#Добавьте методы для вычисления площади прямоугольника и круга соответственно. Создайте несколько объектов этих классов и выведите их площади.

import math

class Shape:
    def calculate_area(self):
        print("Вычисление площади")

class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def rectangle_area(self):
        return self.a * self.b


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area_circle(self):
        return math.pi * (self.radius**2)
    
circle = Circle(5)
circle.calculate_area()
print(circle.area_circle())


#Создайте базовый класс "Фигура" (Shape) с атрибутами "цвет" (color) и "заполнение" (fill). Создайте подклассы "Прямоугольник" (Rectangle) и "Круг" (Circle), 
#которые наследуются от класса "Фигура". Добавьте методы для установки цвета и заполнения фигуры. Создайте несколько объектов этих классов и установите им разные цвета и заполнение.


class Shape:
    def __init__(self, color, fill):
        self.color = color
        self.fill = fill

class Rectangle(Shape):
    def colors_and_fillings(self):
        print(f"Пряммоугольник {self.color} и {self.fill}")
        
class Circle(Shape):
    def colors_and_fillings(self):
        print(f"Круг {self.color} и {self.fill}")

circle = Circle("Красный", "Заштрихованный")
rectangle = Rectangle("Синий", "Прозрачный")
circle.colors_and_fillings()
rectangle.colors_and_fillings()


#Создайте базовый класс "Транспортное средство" (Vehicle) с атрибутами "марка" (brand) и "скорость" (speed). Создайте подклассы "Автомобиль" (Car) и "Мотоцикл" (Motorcycle), 
#которые наследуются от класса "Транспортное средство". Добавьте методы для установки скорости и вывода информации о транспортном средстве. 
#Создайте несколько объектов этих классов и проверьте их методы.


class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

class Car(Vehicle):
    def automabile_brand(self):
        return self.brand
    
    def automabile_speed(self):
        return self.speed
    
    def result(self):
        print(f"Автомобиль {self.automabile_brand()} максимальная скорость {self.automabile_speed()}")


class Motorcycle(Vehicle):
    def motorcycle_brand(self):
        return self.brand
    
    def motorcycle_speed(self):
        return self.speed
        
    def result(self):
        print(f"Мотоцикл {self.motorcycle_brand()} максимальная скорость {self.motorcycle_speed()}")


car = Car("BMW", 220)
car.result()
motorcyle = Motorcycle("Honda", 260)
motorcyle.result()        

#Создайте базовый класс "Животное" (Animal) с атрибутами "имя" (name) и "возраст" (age). Создайте подклассы "Кошка" (Cat) и "Собака" (Dog), которые наследуются от класса "Животное".
#Добавьте методы для вывода звука, который издает животное, и проверьте их работу создав несколько объектов этих классов.


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Cat(Animal):
    def sound(self):
        return f"{self.name} возростом {self.age} года, это кошка и поизносит звук - meow"

class Dog(Animal):
    def sound(self):
        return "woof"
    
cat = Cat("Муся", 2)
print(cat.sound())

#Создайте базовый класс "Человек" (Person) с атрибутами "имя" (name) и "возраст" (age). Создайте подклассы "Студент" (Student) и "Преподаватель" (Teacher), 
#которые наследуются от класса "Человек". Добавьте методы для вывода информации о студенте и преподавателе, включая их специализацию (например, предмет, который преподает преподаватель).
#Создайте несколько объектов этих классов и проверьте

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def student_information(self, course, specialty):
        print(f"Студент. Имя: {self.name}, возраст: {self.age}, курс: {course}, специальность {specialty}")

class Teacher(Person):
    def information_teacher(self, object, course_number):
        print(f"Преподаватель. Имя: {self.name}, возраст: {self.age}, предмет: {object}, перподает студентам {course_number} курса")


student = Student("Григорий", 19)
student.student_information(3,"Data Engineer")
teacher = Teacher("Никита Валерьевич", 34)
teacher.information_teacher("Физическая культура", 2)


# Задача по картинке

class A(object):
    pass

class B(A):
    pass

class C(A):
    pass

class D(A):
    pass

class E(B):
    pass

class F(B):
    pass

class G(B):
    pass

class H(E):
    pass

class I(F, G):
    pass

class J(C):
    pass

class K(D):
    pass

class L(H, I, J, K):
    pass

print(L.__mro__)


# Создайте классы A, B, C, D и E. Класс A имеет метод foo(), класс B наследуется от A и имеет метод bar(), класс C наследуется от A и имеет метод foo(), класс D наследуется одновременно от B и C
# ,а класс E наследуется от D. Создайте объект класса E и вызовите его методы. Наблюдайте порядок вызова методов при использовании MRO.

class A():
    def foo(self):
        return "A"

class B(A):
    def bar(self):
        return "B"

class C(A):
    def foo(self):
        return "C"

class D(B, C):
    pass
    
class E(D):
    pass

e = E()
print(E.__mro__)
print(e.foo())
print(e.bar())

# Создайте цепочку наследования классов, которая сломает mro при инициализации класса

class A():
    pass

class B(A, C):
    pass

class C(A):
    pass