import math
from tkinter import filedialog
import matplotlib.pyplot as plt
from tkinter import *


window = Tk()
window.title("Оценка числовых характеристик случайных величин и построение эмпирических законов их распределения")
window.geometry('450x300')

lbl = Label(window, text="Введите количество опытов:", font=("Arial Bold", 12))
lbl.place(x=10, y=10)
kol_entry = Entry(window, width=7)
kol_entry.place(x=240, y=10)
kol_entry.focus()


def point_amount():
    p_points = int(kol_entry.get())

    lbl = Label(window, text="Введите наблюдаемые значения случайной величины Х:", font=("Arial Bold", 12))
    lbl.place(x=10, y=50)

    l1 = Label(window)
    l1.grid(row=0, column=1)
    l2 = Label(window)
    l2.grid(row=2, column=1)
    l3 = Label(window)
    l3.grid(row=3, column=1)
    l4 = Label(window)
    l4.grid(row=4, column=1)

    tablewidth = p_points

    entries = []
    list_entry = []
    list_number = []

    i = 0
    k = 0
    for row in range(1):
        for column in range(tablewidth):
            if i != p_points:
                _number = Label(window, text=i + 1, width=7)
                list_number.append(_number)
                list_number[i].grid(row=row + 4, column=column + 1)
                i += 1

            _entry = Entry(window, width=7)
            entries.append(_entry)
            entries[k].grid(row=row + 5, column=column + 1)
            k += 1


    def click():
        for i in range(len(entries)):
            list = int(entries[i].get())
            list_entry.append(list)

        # Открываем диалоговое окно для сохранения файла и записываем массив
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        with open(file_path, "w") as file:
            for value in list_entry:
                file.write(f"{value}\n")

        # Вычисляем выборочную среднюю (среднее арифметическое)
        mean = sum(list_entry) / len(list_entry)
        # Вычисляем оценку дисперсии
        variance = sum((x - mean) ** 2 for x in list_entry) / (len(list_entry) - 1)

        lab_sred = Label(window, text="Выборочная средняя: " + str(round((mean), 2)), font=("Arial Bold", 12))
        lab_sred.place(x=10, y=185)
        lab_disp = Label(window, text="Оценка дисперсии: " + str(round((variance), 2)), font=("Arial Bold", 12))
        lab_disp.place(x=10, y=215)

        btn_1 = Button(window, text='Далее', comman=okno1, width=10)
        btn_1.place(x=10, y=250)

    btn_entry = Button(window, text='OK', comman=click, width=10)
    btn_entry.place(x=10, y=140)


    def okno1():
        window1 = Tk()
        window1.title("Оценка числовых характеристик случайных величин и построение эмпирических законов их распределения")
        window1.geometry('450x300')

        emp_lbl = Label(window1, text="Построение эмпирического закона случайной величины:", font=("Arial Bold", 12))
        emp_lbl.place(x=10, y=10)

        # формула Стерджесса
        min_value = min(list_entry)
        max_value = max(list_entry)
        f_Ster = 1 + (3.322 * math.log10(len(list_entry)))
        delta = (max_value - min_value) / f_Ster
        print(f"Значение f_Ster: {(f_Ster)}")
        print(f"Значение delta: {delta}")

        l5 = Label(window1)
        l5.grid(row=0, column=1)
        l6 = Label(window1)
        l6.grid(row=2, column=1)

        inter_gran = min_value

        intervals_ = []
        interval1 = []

        m = 0
        l = 0
        for row in range(1):
            for column in range(tablewidth):
                if l == 0:
                    str_1 = Label(window1, text="Границы интервалов")
                    str_1.grid(row=row + 4, column=column)
                    str_2 = Label(window1, text="Эмпирические частоты")
                    str_2.grid(row=row + 5, column=column)

                inter_gran_1 = min_value + (delta * (m + 1))
                inter_gran_str = f"{inter_gran:.2f} - {round((inter_gran_1), 2):.2f}"
                x = Label(window1, text=inter_gran_str, width=10)
                x.grid(row=row + 4, column=column + 1)
                intervals_.append(inter_gran_str)
                inter_gran = inter_gran_1
                m += 1

                start, end = map(float, intervals_[l].split(' - '))
                print(start, " ", end)
                count = sum(1 for value in list_entry if start <= value <= end)
                print(count)
                x_n1_str = round((count / len(list_entry)), 2)
                print(x_n1_str)
                x_n1 = Label(window1, text=x_n1_str, width=10)
                x_n1.grid(row=row + 5, column=column + 1)
                interval1.append(x_n1_str)
                l += 1

        # Графическое представление гистограммы
        plt.figure(figsize=(8, 4))
        plt.bar(range(len(intervals_)), interval1, align='center', color='green', edgecolor='black')
        plt.xticks(range(len(intervals_)), intervals_)
        plt.xlabel('Границы интервалов')
        plt.ylabel('Эмпирические частоты')
        plt.title('Эмпирический закон распределения случайной величины Х')
        plt.tight_layout()
        plt.show()


        def okno2():
            window2 = Tk()
            window2.title("Оценка числовых характеристик случайных величин и построение эмпирических законов их распределения")
            window2.geometry('450x300')

            emp_lbl = Label(window2, text="Построение статистической функции распределения случайной величины:", font=("Arial Bold", 12))
            emp_lbl.place(x=10, y=10)

            l7 = Label(window2)
            l7.grid(row=0, column=1)
            l8 = Label(window2)
            l8.grid(row=2, column=1)

            interval2 = []

            l = 0
            emp_ch = 0
            for row in range(1):
                for column in range(tablewidth):
                    if l == 0:
                        str_3 = Label(window2, text="Границы интервалов")
                        str_3.grid(row=row + 4, column=column)
                        str_4 = Label(window2, text="Значения функции")
                        str_4.grid(row=row + 5, column=column)

                    emp_ch2 = Label(window2, text=intervals_[l], width=10)
                    emp_ch2.grid(row=row + 4, column=column + 1)

                    emp_ch = emp_ch + interval1[l]
                    emp_ch1 = Label(window2, text=emp_ch, width=7)
                    emp_ch1.grid(row=row + 5, column=column + 1)
                    interval2.append(emp_ch)
                    l += 1

            # Построение статистической функции распределения
            plt.figure(figsize=(8, 4))
            plt.step(range(len(intervals_)), interval2, where='post', color='green')
            plt.xticks(range(len(intervals_)), intervals_)
            plt.grid(True)
            plt.xlabel('Границы интервалов')
            plt.ylabel('Значения функции')
            plt.title('Статистическая функция распределения случайной величины Х')
            plt.tight_layout()
            plt.show()

        btn_2 = Button(window1, text='Далее', comman=okno2, width=10)
        btn_2.place(x=10, y=110)

btn_kol = Button(window, text="OK", command=point_amount, width=10)
btn_kol.place(x=320, y=4)

window.mainloop()