import math
from tkinter import *
from tkinter import filedialog
import numpy as np


window = Tk()
window.title("Статистическая проверка гипотезы о законе распределения случайной гипотезы по критерию согласия (критерию Пирсона)")
window.geometry('450x300')


def zagruzka():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    with open(file_path, "r") as file:
        mas = file.readlines()

    list_entry = []
    float_data = []

    for line in mas:
        items = line.split()
        for item in items:
            try:
                item = int(item)  # Преобразование строки в целое число
                list_entry.append(item)
            except ValueError:
                pass  # Если строка не может быть преобразована в целое число, ничего не делать
            try:
                item = float(item)  # Преобразование строки в число с плавающей запятой
                float_data.append(item)
            except ValueError:
                pass  # Если строка не может быть преобразована в число с плавающей запятой, ничего не делать

    print("Целочисленные данные:", list_entry)
    print("Данные с плавающей запятой:", float_data)

    # Вычисляем выборочную среднюю (среднее арифметическое)
    mean = sum(list_entry) / len(list_entry)
    print(mean)
    # Вычисляем среднее квадратичное отклонение
    variance = math.sqrt(sum((x - mean) ** 2 for x in list_entry) / (len(list_entry) - 1))
    print(variance)

    emp_lbl = Label(window, text="Построение теоретической частоты попадания случайной величины в интервалы:", font=("Arial Bold", 12))
    emp_lbl.place(x=10, y=50)

    # формула Стерджесса
    min_value = min(list_entry)
    max_value = max(list_entry)
    f_Ster = 1 + (3.322 * math.log10(len(list_entry)))
    delta = (max_value - min_value) / f_Ster
    print(f"Значение f_Ster: {(f_Ster)}")
    print(f"Значение delta: {delta}")

    l1 = Label(window)
    l1.grid(row=0, column=1)
    l2 = Label(window)
    l2.grid(row=2, column=1)
    l3 = Label(window)
    l3.grid(row=3, column=1)
    l4 = Label(window)
    l4.grid(row=4, column=1)

    inter_gran = min_value

    intervals_ = []
    p_mas = []
    n_mas = []

    m = 0
    l = 0
    for row in range(1):
        for column in range(len(list_entry)):
            if l == 0:
                str_1 = Label(window, text="Границы интервалов")
                str_1.grid(row=row + 4, column=column)
                str_2 = Label(window, text="Теоретические частоты")
                str_2.grid(row=row + 5, column=column)
                str_3 = Label(window, text="Эмпирические частоты")
                str_3.grid(row=row + 6, column=column)

            inter_gran_1 = min_value + (delta * (m + 1))
            inter_gran_str = f"{inter_gran:.2f} - {round((inter_gran_1), 2):.2f}"
            x = Label(window, text=inter_gran_str, width=12)
            x.grid(row=row + 4, column=column + 1)
            intervals_.append(inter_gran_str)
            inter_gran = inter_gran_1
            m += 1

            start, end = map(float, intervals_[l].split(' - '))
            print(start, " ", end)

            f_start = 0.5 + (0.5 * np.exp(-0.5 * ((start - mean) / variance) ** 2) / math.sqrt(2 * math.pi))
            print(f_start)

            f_end = 0.5 + (0.5 * np.exp(-0.5 * ((end - mean) / variance) ** 2) / math.sqrt(2 * math.pi))
            print(f_end)

            p = round((f_end - f_start), 4)
            p_lab = Label(window, text=p, width=12)
            p_lab.grid(row=row + 5, column=column + 1)
            print(p)
            p_mas.append(p)

            count = sum(1 for value in list_entry if start <= value <= end)
            print(count)
            x_n1_str = round((count / len(list_entry)), 2)
            print(x_n1_str)
            x_n1 = Label(window, text=x_n1_str, width=12)
            x_n1.grid(row=row + 6, column=column + 1)
            n_mas.append(x_n1_str)
            l += 1

    pirs = math.sqrt(sum((n - len(list_entry) * p) ** 2 for n in n_mas / (len(list_entry) * p) for p in p_mas))
    print(pirs)
    a = round((1 - max(p for p in p_mas)), 2)
    k = len(list_entry) - 1
    print(a)

    x_x = 0
    if k == 1:
        if a == 0.99:
            x_x = 0.00016
        elif a == 0.98:
            x_x = 0.00628
        elif a == 0.95:
            x_x = 0.00393
        elif a == 0.90:
            x_x = 0.0158
        elif a == 0.80:
            x_x = 0.0642
        elif a == 0.70:
            x_x = 0.148
        elif a == 0.50:
            x_x = 0.455
        elif a == 0.30:
            x_x = 1.074
        elif a == 0.20:
            x_x = 1.642
        elif a == 0.10:
            x_x = 2.706
        elif a == 0.05:
            x_x = 3.841
        elif a == 0.02:
            x_x = 5.412
        elif a == 0.01:
            x_x = 6.635
    if k == 2:
        if a == 0.99:
            x_x = 0.0201
        elif a == 0.98:
            x_x = 0.0404
        elif a == 0.95:
            x_x = 0.103
        elif a == 0.90:
            x_x = 0.211
        elif a == 0.80:
            x_x = 0.446
        elif a == 0.70:
            x_x = 0.713
        elif a == 0.50:
            x_x = 1.386
        elif a == 0.30:
            x_x = 2.408
        elif a == 0.20:
            x_x = 3.219
        elif a == 0.10:
            x_x = 4.605
        elif a == 0.05:
            x_x = 5.991
        elif a == 0.02:
            x_x = 7.824
        elif a == 0.01:
            x_x = 9.210
    if k == 3:
        if a == 0.99:
            x_x = 0.115
        elif a == 0.98:
            x_x = 0.185
        elif a == 0.95:
            x_x = 0.352
        elif a == 0.90:
            x_x = 0.584
        elif a == 0.80:
            x_x = 1.005
        elif a == 0.70:
            x_x = 1.424
        elif a == 0.50:
            x_x = 2.366
        elif a == 0.30:
            x_x = 3.605
        elif a == 0.20:
            x_x = 4.642
        elif a == 0.10:
            x_x = 6.251
        elif a == 0.05:
            x_x = 7.815
        elif a == 0.02:
            x_x = 9.837
        elif a == 0.01:
            x_x = 11.345
    if k == 4:
        if a == 0.99:
            x_x = 0.297
        elif a == 0.98:
            x_x = 0.429
        elif a == 0.95:
            x_x = 0.711
        elif a == 0.90:
            x_x = 1.064
        elif a == 0.80:
            x_x = 1.649
        elif a == 0.70:
            x_x = 2.195
        elif a == 0.50:
            x_x = 3.357
        elif a == 0.30:
            x_x = 4.878
        elif a == 0.20:
            x_x = 5.989
        elif a == 0.10:
            x_x = 7.779
        elif a == 0.05:
            x_x = 9.488
        elif a == 0.02:
            x_x = 11.668
        elif a == 0.01:
            x_x = 13.277
    print(x_x)

    zn_lbl1 = Label(window, text="Значение уровня значимости возьмем, равное max доверительной вероятности - " + str(a), font=("Arial Bold", 12))
    zn_lbl1.place(x=10, y=160)
    zn_lbl2 = Label(window, text="Число степеней свободы - " + str(k), font=("Arial Bold", 12))
    zn_lbl2.place(x=10, y=185)

    if pirs < (x_x ** 2):
        gip_lbl1 = Label(window, text="Эмпирический закон распределения случайной величины соответствует нормальному теоретическому закону", font=("Arial Bold", 12))
        gip_lbl1.place(x=10, y=220)
        gip_lbl2 = Label(window, text="Вывод: Распределние нормальное", font=("Arial Bold", 12))
        gip_lbl2.place(x=10, y=245)
    else:
        gip_lbl1 = Label(window, text="Эмпирический закон распределения случайной величины не соответствует нормальному теоретическому закону", font=("Arial Bold", 12))
        gip_lbl1.place(x=10, y=220)
        gip_lbl2 = Label(window, text="Вывод: Распределние ненормальное", font=("Arial Bold", 12))
        gip_lbl2.place(x=10, y=245)

btn_zagruz = Button(window, text="Загрузить данные из файла", command=zagruzka, width=30)
btn_zagruz.place(x=10, y=10)

window.mainloop()