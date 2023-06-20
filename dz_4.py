#Задача чтения файла:
#Напишите программу, которая открывает текстовый файл с именем "example.txt" и выводит его содержимое на экран.

with open('example.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)


#Задача записи в файл:
#Напишите программу, которая запрашивает у пользователя несколько строк текста и записывает их в файл с именем "output.txt". Каждая строка должна быть записана в отдельной строке файла.

text = input('Ввидите текст:  ')
text2 = input('Ввидите текст:  ')
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(f'{text}\n')
    f.write(f'{text2}\n')


#Задача подсчета слов:
#Напишите программу, которая открывает текстовый файл с именем "text.txt" и подсчитывает количество слов в файле. Выведите полученный результат на экран.

number_of_words = 0
with open('example.txt', 'r', encoding='utf-8') as f:
    content = f.read()
content = content.split()
for i in content:
    number_of_words += 1
print(number_of_words)
    

#Задача копирования файла:
#Напишите программу, которая открывает исходный файл с именем "source.txt" и создает новый файл с именем "destination.txt". Содержимое исходного файла должно быть скопировано в новый файл.

with open('example.txt', 'r', encoding='utf-8') as f:
    content = f.read()
with open('destination.txt', 'w', encoding='utf-8') as d:
    d.write(content)    


#Задача поиска информации:
#Напишите программу, которая открывает текстовый файл с именем "data.txt" и позволяет пользователю вводить поисковый запрос. Программа должна найти все строки, содержащие запрос, и вывести их на экран.

# with open('example.txt', 'r', encoding='utf-8') as f:
#     content = f.read()
''' Тут не понял задания'''


#Задача удаления файла:
#Напишите программу, которая удаляет текстовый файл с именем "file.txt" при наличии такого файла. Используйте модуль os

import os

if os.path.exists("C://projects/study/destination.txt"):
    os.remove("C://projects/study/destination.txt")
else:
    print("Такого файла нет")
