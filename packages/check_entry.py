"""
Модуль для проверки входных данных.
"""
from tkinter import messagebox
from packages.methods_funcs import zamena
from math import *
def check_h(h):
    """
    Проверка шага, который должен быть больше 0.
    """
    if h > 0:
        return True
    else:
        messagebox.showerror("Неверный ввод", "Шаг должен быть больше 0")
def check_x(x_start, x_last):
    """
    Проверка х с условием, что х нчальный меньше х конечного.
    """
    if x_start < x_last:
        return True
    else:
        messagebox.showerror("Неверный ввод", "X начальный должен быть меньше X конечного")
def check_func(x, y, func):
    """
    Проверка функции, которая должна корректно выполняться встроенной функцией eval().
    """
    try:
        eval(zamena(x, y, func))
        return True
    except:
        messagebox.showerror("Неверный ввод", "Функция введена неверно")
def check_predel(x_start, x_last, h):
    """
    Проверка на предел итераций, который равен 100.
    """
    if (x_last - x_start)/h <= 100:
        return True
    else:
        messagebox.showerror("Ошибка", "Количество итераций превышает 100")
