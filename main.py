"""
***************************************************************
Курсовой проект по предмету МДК 03.01 Технология разработки программного обеспечения
по теме: «Разработка программы решения дифференциальных уравнений»
Язык: Python 3.8
Среда: Visual Studio Code
Название программы: Решение дифференциальных уравнений
Разработал: Абакумов А.С.
Дата: 15.02.2020
****************************************************************
Задание:
Разработать программу решения дифференциальных уравнений:
- методом Эйлера;
- усовершенствованным методом Эйлера.
***************************************************************
Используемые переменные в основной программе:
Eiler_list - результат, подсчитанный методом Эйлера;
UpgradeEiler_list - результат, подсчитанный усовершенствованным методом Эйлера;
self.x_start и self.x_last - интервал, на котором ищется решение функции;
self.y - переменная для начального значения y;
self.h - переменная значения шага;
self.func - переменная для функции вида y` = f(x;y).
***************************************************************
Используемые функции:
Eiler - функция нахождения значений методом Эйлера;
UpgradeEiler - функция нахождения значений усовершенствованным методом Эйлера;
check_entry - функции для проверки вводимых данных:
    check_h - функция для поверки шага;
    check_x - функция для поверки интервала;
    check_func - функция для поверки функции;
    methods_funcs - второстепенные функции для корректной работы методов решения ДУ:
    check_znaki - функция для нахождения необходимого количества знаков после запятой
    у численных результатов методов;
    zamena - функция для замены данных типа float на данные типа string.
***************************************************************
"""
import tkinter as tk
from packages.check_entry import check_h, check_x, check_func, check_predel
from packages.Eiler import Eiler
from packages.UpgradeEiler import UpgradeEiler
from tkinter import messagebox

class Menu(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        root.title("Решение дифференциальных уравнений")
        root.geometry("740x400")
        root.resizable(0, 0)
        root.config(background="#F5F5DC")
        self.start = tk.Frame(root, bg="#F5F5DC")
        self.start.grid(ipadx=740, ipady=400)
        self.EilerWindow = tk.Frame(root, bg="#F5F5DC")
        self.UpgradeEilerWindow = tk.Frame(root, bg="#F5F5DC")
        self.create_widgets_start()

    def save_entry(self):
        """
        Функция для сохранения значения диффернциального уравнения.
        """
        try:
            self.x_start = float(self.entry_start_x.get().replace(',', '.'))
            self.x_last = float(self.entry_last_x.get().replace(',', '.'))
            self.y = float(self.entry_y.get().replace(',', '.'))
            self.h = float(self.entry_h.get().replace(',', '.'))
            self.func = self.entry_func.get()
            if (check_h(self.h) and check_x(self.x_start, self.x_last) and
                    check_func(self.x_start, self.y, self.func) and
                    check_predel(self.x_start, self.x_last, self.h)):
                return True
        except:
            messagebox.showerror("Ошибка", "Недопустимые значения")
        return False


    def start_Eiler(self):
        """
        Запуск главного окна.
        """
        if self.save_entry():
            self.create_EilerWindow()

    def start_UpgradeEiler(self):
        """
        Запуск окна с результатами решения усовершенствованным методом Эйлера.
        """
        if self.save_entry():
            self.create_UpgradeEilerWindow()

    def create_widgets_start(self):
        """
        Создание элементов в главном окне.
        """
        tk.Label(self.start, text="Решение дифференциальных уравнений",
                 font=("Segoe print", 18), bg="#F5F5DC").place(x=120, y=30)
        tk.Label(self.start, text="X начальное",
                 font=("Segoe print", 14), bg="#F5F5DC").place(x=30, y=100)
        self.entry_start_x = tk.Entry(self.start, width=10)
        self.entry_start_x.place(x=190, y=110)

        tk.Label(self.start, text="X конечное",
                 font=("Segoe print", 14), bg="#F5F5DC").place(x=400, y=100)
        self.entry_last_x = tk.Entry(self.start, width=10)
        self.entry_last_x.place(x=560, y=110)

        tk.Label(self.start, text="Y начальное",
                 font=("Segoe print", 14), bg="#F5F5DC").place(x=30, y=140)
        self.entry_y = tk.Entry(self.start, width=10)
        self.entry_y.place(x=190, y=150)

        tk.Label(self.start, text="Шаг",
                 font=("Segoe print", 14), bg="#F5F5DC").place(x=430, y=140)
        self.entry_h = tk.Entry(self.start, width=10)
        self.entry_h.place(x=560, y=150)

        tk.Label(self.start, text="Функция вида: y` = f(x;y)",
                 font=("Segoe print", 14), bg="#F5F5DC").place(x=30, y=240)
        self.entry_func = tk.Entry(self.start, width=35)
        self.entry_func.place(x=45, y=300, height=50)

        tk.Button(self.start, text="Метод Эйлера", command=self.start_Eiler,
                  font=("Segoe print", 11), bg="#FAEBD7").place(x=500, y=240)
        tk.Button(self.start, text="Усовершенствованный метод Эйлера",
                  command=self.start_UpgradeEiler, font=("Segoe print", 11),
                  bg="#FAEBD7").place(x=400, y=300)

    def create_widgets_EilerWindow(self):
        """
        Создание элементов и вывод результатов в окне Эйлер.
        """
        tk.Label(self.EilerWindow, text="Метод Эйлера",
                 font=("Segoe print", 18), bg="#F5F5DC").place(x=270, y=30)
        text = tk.Text(self.EilerWindow, bg="#F5F5DC", height=14, width=50)
        text.place(x=160, y=100)
        scrollbar = tk.Scrollbar(self.EilerWindow, orient=tk.VERTICAL, command=text.yview)
        scrollbar.place(x=720, y=0, height=400)

        Eiler_list = Eiler(self.x_start, self.x_last,
                           self.y, self.h, self.func)
        for elem in Eiler_list:
            if elem != "Error":
                mas = [str(el) for el in elem]
                string = "x = {0}\ny = {1}\ny` = {2}\nyΔ = {3}".format(
                    mas[0], mas[1], mas[2], mas[3])
            else:
                string = elem
            text.insert(tk.END, string+'\n\n')
        text.insert(tk.END, "Результат численного метода: " + str(Eiler_list[-1][-3]))
        tk.Button(self.EilerWindow, text="Назад", font=("Segoe print", 11),
                  bg="#FAEBD7", width=10, command=self.create_start).place(x=580, y=340)

    def create_widgets_UpgradeEilerWindow(self):
        """
        Создание элементов и вывод результатов в окне Усовершенствованный Эйлер.
        """
        tk.Label(self.UpgradeEilerWindow, text="Усовершенствованный метод Эйлера",
                 font=("Segoe print", 18), bg="#F5F5DC").place(x=135, y=30)
        text = tk.Text(self.UpgradeEilerWindow, bg="#F5F5DC", height=14, width=50)
        text.place(x=160, y=100)
        scrollbar = tk.Scrollbar(self.UpgradeEilerWindow, orient=tk.VERTICAL, command=text.yview)
        scrollbar.place(x=720, y=0, height=400)

        UpgradeEiler_list = UpgradeEiler(self.x_start, self.x_last, self.y, self.h, self.func)
        for elem in UpgradeEiler_list:
            if elem != "Error":
                mas = [str(el) for el in elem]
                string = "x = {0}\ny = {1}\ny` = {2}\nyΔ = {3}".format(
                    mas[0], mas[1], mas[2], mas[3])
            else:
                string = elem
            text.insert(tk.END, string+'\n\n')
        text.insert(tk.END, "Результат численного метода: " + str(UpgradeEiler_list[-1][-3]))
        tk.Button(self.UpgradeEilerWindow, text="Назад", font=("Segoe print", 11),
                  bg="#FAEBD7", width=10, command=self.create_start).place(x=580, y=320)

    def create_start(self):
        """
        Создание главного окна и уничтожение окон Эйлер и Усовершенствованный Эйлер.
        """
        self.EilerWindow.destroy()
        self.UpgradeEilerWindow.destroy()
        self.start.grid(ipadx=740, ipady=400)
        self.create_widgets_start()

    def create_EilerWindow(self):
        """
        Создание окна Эйлер.
        """
        self.start.grid_forget()
        self.EilerWindow = tk.Frame(root, bg="#F5F5DC")
        self.EilerWindow.grid(ipadx=740, ipady=400)
        self.create_widgets_EilerWindow()

    def create_UpgradeEilerWindow(self):
        """
        Создание окна Усовершенствованный Эйлер.
        """
        self.start.grid_forget()
        self.UpgradeEilerWindow = tk.Frame(root, bg="#F5F5DC")
        self.UpgradeEilerWindow.grid(ipadx=740, ipady=400)
        self.create_widgets_UpgradeEilerWindow()


root = tk.Tk()
run = Menu(root)
root.mainloop()
 