# -*- coding: utf-8 -*-
"""03_Ввод, модули и обработка данных.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Tg0Isjxi11Hs07Y2VSRAeCkML_hZk718

# 03 Ввод данных. input()

Познакомимся с функцией input() - ввод. Это функция позволяет нам просить
пользователя что-нибудь ввести или принять на ввод какие-то данные.
"""

x = input('Как вас зовут?')
print(x)

"""'Как вас зовут?' - аргумент функции input(), который будет отображаться в строке ввода. Он необязателен, но он может быть полезен для вас (особенно, если в задаче требуется ввести больше одной строки данных и нужно не запутаться).

Обратите внимание, что функция  input() все сохраняет в строковом формате данных. Но мы можем сделать из
числа-строки число-число с помощью функции int(). Введите "1" в обоих случаях и сравните результат.
"""

print(type(input()))
print(type(int(input())))

"""Нужно следить за тем, какие данные вы считываете и менять их при необходимости. Сравните два примере ниже."""

x = input('Input x value: ')
y = input('Input y value: ')
print(x + y) # произошла склейка строк, по умолчанию input() сохраняет значение типа str

x = int(input('Input x value: '))
y = int(input('Input y value: '))
print(x + y) # вот теперь произошло сложение чисел

"""## Задача 1. Pig Latin 1

Pig Latin - вымышленный язык, который в конец каждого слова подставляет 'yay' (на самом деле оригинальные условия задачи несколько хитрее, но мы будем к ней возвращаться по ходу курса.

**Формат ввода**  
Пользователь вводит слова.

**Формат вывода**
Слово на Pig Latin.


#### Примеры
Тест 1  
**Ввод:**  
apple

**Вывод:**  
appleyay
"""

word = input('Введите слово: ')
print(word+'yay')

"""## Задача 2. Как перевести градусы Цельсия в градусы Фаренгейта
Чтобы при помощи Python перевести градусы Цельсия в градусы Фаренгейта (или наоборот), необходимо реализовать в коде следующие формулы:

Градусы Цельсия в градусы Фаренгейта:
F = 1.8 x C + 32

Градусы Фаренгейта в градусы Цельсия:
C = (F - 32) / 1.8
"""

# Запросить пользовательский ввод (температуру в градусах Цельсия)
c = float(input("Give me a temperature in celcius: "))
# Преобразовать значение, введенное пользователем, в градусы Фаренгейта
f = 1.8 * c + 32
# Вывести результат
print("The temperature is ",f," in fahrenheit")

# Здесь напишите программу для преобразования градусов Фаренгейта в градусы Цельсия
f = float(input("Give me a temperature in fahrenheit: "))
# Преобразовать значение, введенное пользователем, в градусы Фаренгейта
c = (f - 32)/1.8
# Вывести результат
print("The temperature is ",c," in celcius")

"""## Импорт модулей
По мере количества строк вашего кода будет не лишним начинать пользоваться модулями.

Модуль — это файл, содержащий функции и операторы. У всех модулей в Python есть имя, которое заканчивается расширением .py.

Операторы внутри модуля могут быть импортированы в другой модуль или в интерпретатор Python. Для этого мы используем ключевое слово import.

Например, мы можем импортировать модуль math. Делается это следующим образом:

`import math`
"""

import math
print(math.pi)

"""## Модуль random
Модуль random позволяет генерировать случайные числа. Прежде чем использовать модуль, необходимо подключить его

`import random`

## randint

Функция randint(a, b) получает на вход два целых числа и возвращает случайное значение из диапазона [a,b]    (a и b входят в этот диапазон).
"""

import random

random_number = random.randint(0, 125)
print(random_number)

"""## randrange

В функцию randrange(start, stop[, step]) передают три целых числа:

start
 – начало диапазона (входит в последовательность);

stop
 – конец диапазона (в последовательность не входит);

step
 – шаг генерации (если на его месте написать 0, получим ошибку "ValueError").

На выходе функция выдает случайное число в заданном диапазоне
"""

import random

random_number = random.randrange(1, 100, 2)
print(random_number)

"""## random

Функция  random()  выдает вещественные числа, в диапазоне [0.0, 1.0)

 (включая 0.0, но не включая 1.0).
"""

import random

random_number = random.random()
print(random_number)

"""## Задача 3. Как перевести случайные градусы Цельсия в градусы Фаренгейта.

Сделайте снова перевод градусов Цельсия в Фаренгейт, только теперь не запрашивайте градусы с клавиатуры, а сгенерируйте случайно в диапазоне [-50, 42]
"""



"""# Задание 1

Карандаш стоит X рублей за штуку. Покупатель дал кассиру Y рублей и хочет купить 8 карандашей. Какую сдачу он должен получить? Ответ дайте в рублях. (X и Y запросить у пользователя)

"""



"""# Задание 3

Ребенок в день съедает X творожка. Творожок продается в упаковках по Y штук. Какое наименьшее число упаковок надо купить, чтобы ребенку хватило на две недели?  (X и Y запросить у пользователя)
"""

t = float(input())
u = float(input())
res = t * 14 / u
import math
res = math.ceil(res)
print(res)

"""# Задание 4

Килограмм картошки стоит Х рублей. У Олега есть 1000 р, из этой суммы он 640 р должен положить на телефон, а на остальные деньги он купил картошку. Сколько килограмм купил Олег, если он получил сдачу Y рублей?
 (X и Y запросить у пользователя)
"""

x = int(input())
y = int(input())
kg = (1000 - 640) / x - y
print(kg)

