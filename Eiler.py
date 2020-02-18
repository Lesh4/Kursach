"""Метод Эйлера"""
from zamena import zamena
from math import *

def Eiler(x, x_last, y, h, uravn):
    res = []
    while x <= x_last:
        uravn_res = eval(zamena(x, y, uravn))
        y_del = h*uravn_res
        res.append([float(format(x, ".3f")), float(format(y, ".3f")), float(format(uravn_res, ".3f")), float(format(y_del, ".3f"))])
        y += y_del
        x += h
    return res
