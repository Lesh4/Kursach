"""
Модуль UpgradeEiler:
Функция, которая вычисляет y усовершенствованным методом Эйлера.
Формальные параметры:
x и x_last - интервал, на котором ищется решение функции;
y - переменная для начального значения y;
h - шаг;
uravn - функция вида y` = f(x;y).
Локальные переменные:
h_pol - величина шага, деленного на 2;
res – список выходных данных;
y_shtrih – значение функция вида y` = f(x;y);
uravn_res - значение функция вида y` = f(x+h/2;y+f(x;y));
y_del - переменная, которая содержит в себе величину приращения функции.
"""

from math import *
from packages.methods_funcs import zamena, check_znaki

def UpgradeEiler(x, x_last, y, h, uravn):
    """
    Решение усовершенствованным методом Эйлера.
    """
    res = []
    try:
        kol = '.' + str(check_znaki(x, x_last, y, h)+2) + 'f'
        while x <= x_last:
            h_pol = h*0.5
            y_shtrih = eval(zamena(x, y, uravn))*(h_pol)
            uravn_res = eval(zamena(x+h_pol,y+y_shtrih , uravn))
            y_del = uravn_res * h
            res.append([float(format(x, kol)), float(format(y, kol)),
                        float(format(uravn_res, kol)), float(format(y_del, kol))])
            y += y_del
            x += h
    except:
        res.append("Error")
    return res
