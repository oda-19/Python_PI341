import math
from tkinter import *


window = Tk()
window.title("Корреляционный анализ")
window.geometry('650x300')

lbl = Label(window, text="Введите длину выборки случайных величин X, Y, Z:", font=("Arial Bold", 12))
lbl.place(x=10, y=10)
kol_entry = Entry(window, width=7)
kol_entry.place(x=400, y=10)
kol_entry.focus()


def point_amount_x():
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

    entries_x = []
    list_entry_x = []
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
            entries_x.append(_entry)
            entries_x[k].grid(row=row + 5, column=column + 1)
            k += 1


    def click_x():
        for i in range(len(entries_x)):
            list = int(entries_x[i].get())
            list_entry_x.append(list)

        window1 = Tk()
        window1.title("Корреляционный анализ")
        window.geometry('650x300')

        lbl = Label(window1, text="Введите наблюдаемые значения случайной величины Y:", font=("Arial Bold", 12))
        lbl.place(x=10, y=10)

        l1 = Label(window1)
        l1.grid(row=0, column=1)
        l2 = Label(window1)
        l2.grid(row=2, column=1)

        tablewidth = p_points

        entries_y = []
        list_entry_y = []
        list_number = []

        i = 0
        k = 0
        for row in range(1):
            for column in range(tablewidth):
                if i != p_points:
                    _number = Label(window1, text=i + 1, width=7)
                    list_number.append(_number)
                    list_number[i].grid(row=row + 4, column=column + 1)
                    i += 1

                _entry = Entry(window1, width=7)
                entries_y.append(_entry)
                entries_y[k].grid(row=row + 5, column=column + 1)
                k += 1

        def click_y():
            for i in range(len(entries_y)):
                list = int(entries_y[i].get())
                list_entry_y.append(list)

            window2 = Tk()
            window2.title("Корреляционный анализ")
            window.geometry('650x300')

            lbl = Label(window2, text="Введите наблюдаемые значения случайной величины Z:", font=("Arial Bold", 12))
            lbl.place(x=10, y=10)

            l1 = Label(window2)
            l1.grid(row=0, column=1)
            l2 = Label(window2)
            l2.grid(row=2, column=1)

            tablewidth = p_points

            entries_z = []
            list_entry_z = []
            list_number = []

            i = 0
            k = 0
            for row in range(1):
                for column in range(tablewidth):
                    if i != p_points:
                        _number = Label(window2, text=i + 1, width=7)
                        list_number.append(_number)
                        list_number[i].grid(row=row + 4, column=column + 1)
                        i += 1

                    _entry = Entry(window2, width=7)
                    entries_z.append(_entry)
                    entries_z[k].grid(row=row + 5, column=column + 1)
                    k += 1

            def click_z():
                for i in range(len(entries_z)):
                    list = int(entries_z[i].get())
                    list_entry_z.append(list)

                window3 = Tk()
                window3.title("Корреляционный анализ")
                window3.geometry('650x300')

                # Вычисляем выборочную среднюю (среднее арифметическое)
                mean_x = sum(list_entry_x) / len(list_entry_x)
                # Вычисляем оценку дисперсии
                variance_x = math.sqrt(sum((x - mean_x) ** 2 for x in list_entry_x) / (len(list_entry_x) - 1))
                lab_sred = Label(window3, text="Выборочная средняя случайной величины X: " + str(round((mean_x), 2)), font=("Arial Bold", 12))
                lab_sred.place(x=10, y=10)
                lab_disp = Label(window3, text="Среднее квадратическое отклонение случайной величины X: " + str(round((variance_x), 2)), font=("Arial Bold", 12))
                lab_disp.place(x=10, y=40)

                # Вычисляем выборочную среднюю (среднее арифметическое)
                mean_y = sum(list_entry_y) / len(list_entry_y)
                # Вычисляем оценку дисперсии
                variance_y = math.sqrt(sum((x - mean_y) ** 2 for x in list_entry_y) / (len(list_entry_y) - 1))
                lab_sred = Label(window3, text="Выборочная средняя случайной величины Y: " + str(round((mean_y), 2)), font=("Arial Bold", 12))
                lab_sred.place(x=10, y=70)
                lab_disp = Label(window3, text="Среднее квадратическое отклонение случайной величины Y: " + str(round((variance_y), 2)), font=("Arial Bold", 12))
                lab_disp.place(x=10, y=100)

                # Вычисляем выборочную среднюю (среднее арифметическое)
                mean_z = sum(list_entry_z) / len(list_entry_z)
                # Вычисляем оценку дисперсии
                variance_z = math.sqrt(sum((x - mean_z) ** 2 for x in list_entry_z) / (len(list_entry_z) - 1))
                lab_sred = Label(window3, text="Выборочная средняя случайной величины Z: " + str(round((mean_z), 2)), font=("Arial Bold", 12))
                lab_sred.place(x=10, y=130)
                lab_disp = Label(window3, text="Среднее квадратическое отклонение случайной величины Z: " + str(round((variance_z), 2)), font=("Arial Bold", 12))
                lab_disp.place(x=10, y=160)

                r_xy = (sum((x - mean_x) * (y - mean_y) for x, y in zip(list_entry_x, list_entry_y))) / (p_points * variance_x * variance_y)
                print(r_xy)
                r_xz = (sum((x - mean_x) * (z - mean_z) for x, z in zip(list_entry_x, list_entry_z))) / (p_points * variance_x * variance_z)
                print(r_xz)
                r_yz = (sum((y - mean_y) * (z - mean_z) for y, z in zip(list_entry_y, list_entry_z))) / (p_points * variance_y * variance_z)
                print(r_yz)

                lab_matr = Label(window3, text="Матрица коэффициентов парных корреляций:", font=("Arial Bold", 12))
                lab_matr.place(x=10, y=190)

                lab_matr1 = Label(window3, text="          1     " + str(round(r_xy, 2)) + "     " + str(round(r_xz, 2)), font=("Arial Bold", 12))
                lab_matr1.place(x=10, y=220)

                lab_matr2 = Label(window3, text="||r|| = " + "            1       " + str(round(r_yz, 2)), font=("Arial Bold", 12))
                lab_matr2.place(x=10, y=250)

                lab_matr3 = Label(window3, text="                                 1", font=("Arial Bold", 12))
                lab_matr3.place(x=10, y=280)

            btn_entry = Button(window2, text='ОК - Далее', comman=click_z, width=15)
            btn_entry.place(x=10, y=115)

        btn_entry = Button(window1, text='ОК - Далее', comman=click_y, width=15)
        btn_entry.place(x=10, y=115)

    btn_entry = Button(window, text='ОК - Далее', comman=click_x, width=15)
    btn_entry.place(x=10, y=140)

btn_kol = Button(window, text="OK", command=point_amount_x, width=10)
btn_kol.place(x=485, y=4)

window.mainloop()