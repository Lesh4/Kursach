from math import *
import copy

print('Введите начальные условия')

x_start = float(input('x0: '))
y_start = float(input('y0: '))
x_search = float(input('Искомое значение: '))
pgr = float(input('Погрешность: '))

h = abs(abs(x_search)-abs(x_start))
n = ceil( h / (pgr**(1/4)))
h = h/n

rez = []

y = [y_start]
h = abs((x_start-x_search)/n)
x = [x_start+h*i for i in range(n+1)]

def zamena(x,y):
    uravn_copy = copy.copy(uravn)
    uravn_copy = uravn_copy.replace('y', str(y))
    uravn_copy = uravn_copy.replace('x', str(x))
    return uravn_copy

print("Введите функцию f(x,y) уравнения типа y'=f(x,y):")
uravn = input()
uravn = uravn.replace('^', '**')

for i in range(n):
    k1 = h * eval(zamena(x[i], y[i]))
    k2 = h * eval(zamena(x[i] + h / 2, y[i] + k1 / 2))
    k3 = h * eval(zamena(x[i] + h / 2, y[i] + k2 / 2))
    k4 = h * eval(zamena(x[i] + h, y[i] + k3))
    dy = (k1 + k2*2 + k3*2 + k4) / 6
    y.append(y[i]+dy)
    rez.append({'x':x[i],'y':y[i], 'k1':k1, 'k2':k2, 'k3':k3, 'k4':k4, 'dy':dy})
rez.append({'x':x[i+1],'y':y[i+1]})

print("i  x      y      k1     k2     k3     k4     dy")
for i in range(n):
    print("%2d" % i, "%.4f" % (rez[i]['x']), "%.4f" % (rez[i]['y']), "%.4f" % (rez[i]['k1']), "%.4f" % (rez[i]['k2']), "%.4f" % (rez[i]['k3']), "%.4f" % (rez[i]['k4']), "%.4f" % (rez[i]['dy']))
i+=1
print("%2d" % i, "%.4f" % (x[i]), "%.4f" % (y[i]))

f = open("output.txt", "w")
f.write("y0 = " + str(y_start) + "; x0 = " + str(x_start) + "; x искомое = " + str(x_search) + "\n")
f.write("погрешность = " + str(pgr) + "; шаг =  " + str(h) + "\n")
f.write("дифференицальное уравнение: y'= " + uravn + "\n")
f.write("i  x      y      k1     k2     k3     k4     dy\n")
for i in range(n):
    output = "%2d" % i + " "
    output += "%.4f" % (rez[i]['x']) + " "
    output += "%.4f" % (rez[i]['y']) + " "
    output += "%.4f" % (rez[i]['k1']) + " "
    output += "%.4f" % (rez[i]['k2']) + " "
    output += "%.4f" % (rez[i]['k3']) + " "
    output += "%.4f" % (rez[i]['k4']) + " "
    output += "%.4f" % (rez[i]['dy']) + "\n"
    f.write(output)
i+=1
f.write("%2d" % i + " " + "%.4f" % (x[i]) + " " + "%.4f" % (y[i]))
f.close()

input()
