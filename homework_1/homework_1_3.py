# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки
lst = input("Введите через пробел координаты двух точек: ")
x_1, y_1, x_2, y_2 = lst.split()
x_1, y_1, x_2, y_2 = int(x_1),int(y_1), int(x_2), int(y_2)

k = (y_1-y_2) / (x_1-x_2)
b = y_2 - k * x_2

print(f'y = {k}x + {b}')