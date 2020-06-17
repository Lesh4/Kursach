"""
Модуль Eiler:
Функция, которая вычисляет y методом Эйлера.
Формальные параметры:
x и x_last - интервал, на котором ищется решение функции;
y - переменная для начального значения y;
h - шаг;
uravn - функция вида y` = f(x;y).
Локальные переменные:
res – список выходных данных;
uravn_res - значение функция вида y` = f(x;y);
y_del - переменная, которая содержит в себе величину приращения функции.
"""
from math import *
from packages.methods_funcs import zamena, check_znaki

def Eiler(x, x_last, y, h, uravn):
    """
    Решение методом Эйлера.
"""
    res = []
    try:
        kol = check_znaki(x, x_last, y, h) + 2
        while x <= x_last:
            uravn_res = round(eval(zamena(x, y, uravn)), kol)
            y_del = round(h * uravn_res, kol)
            res.append([round(x, kol), round(y, kol),
                        uravn_res, y_del])
            y += y_del
            x += h
    except:
        res.append("Error")
    return res
