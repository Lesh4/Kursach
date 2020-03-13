"""
Модуль Eiler:
Функция, которая вычисляет y методом Эйлера.
Формальные параметры:
x – x начальный;
x_last - x конечный;
y - y начальный;
h - шаг;
uravn - функция вида y` = f(x;y).
Локальные переменные:
res – список выходных данных;
uravn_res - значение функция вида y` = f(x;y);
y_del - y дельта.
"""
from math import *
from packages.methods_funcs import zamena, check_znaki

def Eiler(x, x_last, y, h, uravn):
    res = []
    kol = '.' + str(check_znaki(x, x_last, y, h)+1) + 'f'
    while x <= x_last:
        uravn_res = eval(zamena(x, y, uravn))
        y_del = h*uravn_res
        res.append([float(format(x, kol)), float(format(y, kol)), float(format(uravn_res, kol)), float(format(y_del, kol))])
        y += y_del
        x += h
    return res

    #чисто чекнуть че по чем
    #testing