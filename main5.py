from tkinter import *


window = Tk()
window.title("Статистическая проверка гипотезы о равенстве дисперсий двух нормальных генеральных совокупностей (распределение Фишера-Снедекора)")
window.geometry('650x300')

lbl = Label(window, text="Введите количество опытов для случайной величины X:", font=("Arial Bold", 12))
lbl.place(x=10, y=10)
kol_entry_x = Entry(window, width=7)
kol_entry_x.place(x=435, y=10)
kol_entry_x.focus()


def point_amount_x():
    p_points = int(kol_entry_x.get())

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
            entries.append(_entry)
            entries[k].grid(row=row + 5, column=column + 1)
            k += 1


    def click_x():
        for i in range(len(entries)):
            list = int(entries[i].get())
            list_entry_x.append(list)

        window1 = Tk()
        window1.title("Статистическая проверка гипотезы о равенстве дисперсий двух нормальных генеральных совокупностей (распределение Фишера-Снедекора)")
        window.geometry('650x300')

        lbl = Label(window1, text="Введите количество опытов для случайной величины Y:", font=("Arial Bold", 12))
        lbl.place(x=10, y=10)
        kol_entry_y = Entry(window1, width=7)
        kol_entry_y.place(x=435, y=10)
        kol_entry_y.focus()

        def point_amount_y():
            p_points = int(kol_entry_y.get())

            lbl = Label(window1, text="Введите наблюдаемые значения случайной величины Y:", font=("Arial Bold", 12))
            lbl.place(x=10, y=50)

            l1 = Label(window1)
            l1.grid(row=0, column=1)
            l2 = Label(window1)
            l2.grid(row=2, column=1)
            l3 = Label(window1)
            l3.grid(row=3, column=1)
            l4 = Label(window1)
            l4.grid(row=4, column=1)

            tablewidth = p_points

            entries = []
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
                    entries.append(_entry)
                    entries[k].grid(row=row + 5, column=column + 1)
                    k += 1

            def click_y():
                for i in range(len(entries)):
                    list = int(entries[i].get())
                    list_entry_y.append(list)

                window2 = Tk()
                window2.title("Статистическая проверка гипотезы о равенстве дисперсий двух нормальных генеральных совокупностей (распределение Фишера-Снедекора)")
                window2.geometry('650x300')

                # Вычисляем выборочную среднюю (среднее арифметическое)
                mean_x = sum(list_entry_x) / len(list_entry_x)
                # Вычисляем оценку дисперсии
                variance_x = sum((x - mean_x) ** 2 for x in list_entry_x) / (len(list_entry_x) - 1)
                lab_disp = Label(window2, text="Выборочная дисперсия случайной величины X: " + str(round((variance_x), 2)), font=("Arial Bold", 12))
                lab_disp.place(x=10, y=10)

                # Вычисляем выборочную среднюю (среднее арифметическое)
                mean_y = sum(list_entry_y) / len(list_entry_y)
                # Вычисляем оценку дисперсии
                variance_y = sum((x - mean_y) ** 2 for x in list_entry_y) / (len(list_entry_y) - 1)
                lab_disp = Label(window2, text="Выборочная дисперсия случайной величины Y: " + str(round((variance_y), 2)), font=("Arial Bold", 12))
                lab_disp.place(x=10, y=40)

                if variance_x > variance_y:
                    f = variance_x / variance_y
                else:
                    f = variance_y / variance_x
                lab_disp = Label(window2, text="Случайная величина подчинена распределению Фишера - Снедекора: F = " + str(round((f), 2)), font=("Arial Bold", 12))
                lab_disp.place(x=10, y=70)

                lbl = Label(window2, text="Введите уровень значимости а (0.01 или 0.05):", font=("Arial Bold", 12))
                lbl.place(x=10, y=107)
                znach = Entry(window2, width=7)
                znach.place(x=370, y=110)


                def rez():
                    znach_kol = float(znach.get())

                    if variance_x > variance_y:
                        k1 = len(list_entry_x) - 1
                    else:
                        k1 = len(list_entry_y) - 1

                    if variance_x < variance_y:
                        k2 = len(list_entry_x) - 1
                    else:
                        k2 = len(list_entry_y) - 1
                    print(k1)
                    print(k2)

                    f_f = 0
                    if znach_kol == 0.01:
                        if k1 == 1:
                            if k2 == 1:
                                f_f = 4052
                            if k2 == 2:
                                f_f = 98.49
                            if k2 == 3:
                                f_f = 34.12
                            if k2 == 4:
                                f_f = 21.20
                            if k2 == 5:
                                f_f = 16.26
                            if k2 == 6:
                                f_f = 13.74
                        if k1 == 2:
                            if k2 == 1:
                                f_f = 4999
                            if k2 == 2:
                                f_f = 99.01
                            if k2 == 3:
                                f_f = 30.81
                            if k2 == 4:
                                f_f = 18.00
                            if k2 == 5:
                                f_f = 13.27
                            if k2 == 6:
                                f_f = 10.92
                        if k1 == 3:
                            if k2 == 1:
                                f_f = 5403
                            if k2 == 2:
                                f_f = 99.17
                            if k2 == 3:
                                f_f = 29.46
                            if k2 == 4:
                                f_f = 16.69
                            if k2 == 5:
                                f_f = 12.06
                            if k2 == 6:
                                f_f = 9.78
                        if k1 == 4:
                            if k2 == 1:
                                f_f = 5625
                            if k2 == 2:
                                f_f = 99.25
                            if k2 == 3:
                                f_f = 28.71
                            if k2 == 4:
                                f_f = 15.98
                            if k2 == 5:
                                f_f = 11.39
                            if k2 == 6:
                                f_f = 9.15
                        if k1 == 5:
                            if k2 == 1:
                                f_f = 5764
                            if k2 == 2:
                                f_f = 99.30
                            if k2 == 3:
                                f_f = 28.24
                            if k2 == 4:
                                f_f = 15.52
                            if k2 == 5:
                                f_f = 10.97
                            if k2 == 6:
                                f_f = 8.75
                        if k1 == 6:
                            if k2 == 1:
                                f_f = 5889
                            if k2 == 2:
                                f_f = 99.33
                            if k2 == 3:
                                f_f = 27.91
                            if k2 == 4:
                                f_f = 15.21
                            if k2 == 5:
                                f_f = 10.67
                            if k2 == 6:
                                f_f = 8.47

                    if znach_kol == 0.05:
                        if k1 == 1:
                            if k2 == 1:
                                f_f = 161.4
                            if k2 == 2:
                                f_f = 18.51
                            if k2 == 3:
                                f_f = 10.13
                            if k2 == 4:
                                f_f = 7.71
                            if k2 == 5:
                                f_f = 6.61
                            if k2 == 6:
                                f_f = 5.99
                        if k1 == 2:
                            if k2 == 1:
                                f_f = 199.5
                            if k2 == 2:
                                f_f = 19.00
                            if k2 == 3:
                                f_f = 9.55
                            if k2 == 4:
                                f_f = 6.94
                            if k2 == 5:
                                f_f = 5.79
                            if k2 == 6:
                                f_f = 5.14
                        if k1 == 3:
                            if k2 == 1:
                                f_f = 215.7
                            if k2 == 2:
                                f_f = 19.16
                            if k2 == 3:
                                f_f = 9.28
                            if k2 == 4:
                                f_f = 6.59
                            if k2 == 5:
                                f_f = 5.41
                            if k2 == 6:
                                f_f = 4.76
                        if k1 == 4:
                            if k2 == 1:
                                f_f = 224.6
                            if k2 == 2:
                                f_f = 19.25
                            if k2 == 3:
                                f_f = 9.12
                            if k2 == 4:
                                f_f = 6.39
                            if k2 == 5:
                                f_f = 5.19
                            if k2 == 6:
                                f_f = 4.53
                        if k1 == 5:
                            if k2 == 1:
                                f_f = 230.2
                            if k2 == 2:
                                f_f = 19.30
                            if k2 == 3:
                                f_f = 9.01
                            if k2 == 4:
                                f_f = 6.26
                            if k2 == 5:
                                f_f = 5.05
                            if k2 == 6:
                                f_f = 4.39
                        if k1 == 6:
                            if k2 == 1:
                                f_f = 234.0
                            if k2 == 2:
                                f_f = 19.33
                            if k2 == 3:
                                f_f = 8.94
                            if k2 == 4:
                                f_f = 6.16
                            if k2 == 5:
                                f_f = 4.95
                            if k2 == 6:
                                f_f = 4.28
                    print(f_f)

                    znach_lbl = Label(window2, text="Гипотеза о равенстве дисперсий 2ух нормальных генеральных совокупностей случайных величин X и Y проверена", font=("Arial Bold", 12))
                    znach_lbl.place(x=10, y=160)
                    if f > f_f:
                        znach_lbl1 = Label(window2, text="Вывод: Дисперсии не равны", font=("Arial Bold", 12))
                        znach_lbl1.place(x=10, y=185)
                    else:
                        znach_lbl1 = Label(window2, text="Вывод: Дисперсии равны", font=("Arial Bold", 12))
                        znach_lbl1.place(x=10, y=185)

                btn_znach = Button(window2, text="OK", command=rez, width=10)
                btn_znach.place(x=450, y=105)

            btn_entry = Button(window1, text='ОК - Далее', comman=click_y, width=15)
            btn_entry.place(x=10, y=140)

        btn_kol = Button(window1, text="OK", command=point_amount_y, width=10)
        btn_kol.place(x=515, y=4)

    btn_entry = Button(window, text='ОК - Далее', comman=click_x, width=15)
    btn_entry.place(x=10, y=140)

btn_kol = Button(window, text="OK", command=point_amount_x, width=10)
btn_kol.place(x=515, y=4)

window.mainloop()