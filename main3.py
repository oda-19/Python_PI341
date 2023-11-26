import math
from tkinter import *
from tkinter import filedialog
import numpy as np


window = Tk()
window.title("Вычисление вероятности попадания случайной величины, распределенной по нормальному закону, на заданный участок")
window.geometry('450x300')


def zagruzka():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    with open(file_path, "r") as file:
        list_entry = [int(line) for line in file.read().split()]
    for i in range(len(list_entry)):
        print(list_entry[i])

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

    m = 0
    l = 0
    for row in range(1):
        for column in range(len(list_entry)):
            if l == 0:
                str_1 = Label(window, text="Границы интервалов")
                str_1.grid(row=row + 4, column=column)
                str_2 = Label(window, text="Теоретические частоты")
                str_2.grid(row=row + 5, column=column)

            inter_gran_1 = min_value + (delta * (m + 1))
            inter_gran_str = f"{inter_gran:.2f} - {round((inter_gran_1), 2):.2f}"
            x = Label(window, text=inter_gran_str, width=10)
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
            p_mas.append(p)
            print(p)
            l += 1

    # Открываем диалоговое окно для сохранения файла
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    with open(file_path, "w") as file:
        for value in list_entry:
            file.write(f"{value}\n")
        for value in p_mas:
            file.write(f"{value}\n")

btn_zagruz = Button(window, text="Загрузить данные из файла", command=zagruzka, width=30)
btn_zagruz.place(x=10, y=10)

window.mainloop()