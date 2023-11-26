import math
from tkinter import filedialog
from tkinter import *


window = Tk()
window.title("Статистическая проверка гипотезы о законе распределения случайной величины с помощью коэффициента асимметрии А и эксцесса Е")
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

    a = sum((x - mean) ** 3 for x in list_entry) / ((len(list_entry) - 1) * variance ** 3)
    print(a)
    lbl = Label(window, text="Коэффициент асимметрии А: " + str(round((a), 2)), font=("Arial Bold", 12))
    lbl.place(x=10, y=55)
    if a == 0:
        lbl1 = Label(window, text="Коэффициент асимметрии А соответствует теоретическому нормальному закону, А = 0", font=("Arial Bold", 12))
        lbl1.place(x=10, y=80)
    else:
        lbl1 = Label(window, text="Коэффициент асимметрии А не соответствует теоретическому нормальному закону", font=("Arial Bold", 12))
        lbl1.place(x=10, y=80)

    e = (sum((x - mean) ** 4 for x in list_entry) / ((len(list_entry) - 1) * variance ** 4)) - 3
    print(e)
    lbl2 = Label(window, text="Эксцесс Е: " + str(round((e), 2)), font=("Arial Bold", 12))
    lbl2.place(x=10, y=125)
    if e == 0:
        lbl3 = Label(window, text="Эксцесс Е соответствует теоретическому нормальному закону, E = 0", font=("Arial Bold", 12))
        lbl3.place(x=10, y=150)
    else:
        lbl3 = Label(window, text="Эксцесс Е не соответствует теоретическому нормальному закону", font=("Arial Bold", 12))
        lbl3.place(x=10, y=150)

btn_zagruz = Button(window, text="Загрузить данные из файла", command=zagruzka, width=30)
btn_zagruz.place(x=10, y=10)

window.mainloop()