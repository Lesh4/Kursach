"""
Модуль UpgradeEiler:
Функция, которая вычисляет y усовершенствованным методом Эйлера.
Формальные параметры:
x – x начальный;
x_last - x конечный;
y - y начальный;
h - шаг;
uravn - функция вида y` = f(x;y).
Локальные переменные:
res – список выходных данных;
y_shtrih – значение функция вида y` = f(x;y);
uravn_res - значение функция вида y` = f(x+h/2;y+f(x;y));
y_del - y дельта.
"""

from math import *
from zamena import zamena

def UpgradeEiler(x, x_last, y, h, uravn):
    res = []
    while x <= x_last:
        y_shtrih = eval(zamena(x, y, uravn))*(h/2)
        uravn_res = eval(zamena(x+h/2,y+y_shtrih , uravn))
        y_del = uravn_res * h
        res.append([float(format(x, ".4f")), float(format(y, ".4f")), float(format(uravn_res, ".4f")), float(format(y_del, ".4f"))])
        y += y_del
        x += h
    return res
