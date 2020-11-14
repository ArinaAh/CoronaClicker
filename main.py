import tkinter as tk
import random

virus = 0
virus_increaser = 1
amount_of_viruses = 0
viruses = []
day = 0
Enter = True
money = 0
count = 0
autoclickers = []
time_change_screen = 100
time_auto_handler = 500
time_to_update_virus = 150
stop_number = 1000
time_to_plus_day = 11000
plus_money = 0.5


class AutoClicker:
    value = 0
    point = 0

    def __init__(self, value_, point_):
        self.value = value_
        self.point = point_

    def get_value(self):
        return self.value

    def get_point(self):
        return self.point


def createAutoClicker(value, point):
    global money
    global autoclickers
    if money >= value:
        money -= value
        clicker = AutoClicker(value, point)
        autoclickers.append(clicker)


def autoClickersHandler():
    global virus
    global time_auto_handler
    for i in autoclickers:
        if virus > i.get_point():
            virus -= i.get_point()
    inf_virus.after(time_auto_handler, autoClickersHandler)


def play(event):
    global Enter
    if not Enter:
        pass
    else:
        main_text.config(text="")
        updateVirus()
        changeDay()
        changeScreen()
        autoClickersHandler()
        Enter = False


def changeScreen():
    global virus
    global day
    global money
    inf_virus.config(text="Уровень распространения:" + str(virus))
    inf_day.config(text="День:" + str(day))
    inf_money.config(text='Деньги:' + str(money))
    virus_screen.after(time_change_screen, changeScreen)


def updateVirus():
    global viruses
    global virus
    global amount_of_viruses
    global virus_increaser
    global time_to_update_virus
    virus += virus_increaser
    if amount_of_viruses < virus // 10:
        amount_of_viruses += 1
        for i in range(2):
            tk.Label(root, image=photo_virus).grid(row=random.randint(3, 10),
                                                   column=random.randint(3, 10))

    if amount_of_viruses > virus // 10:
        amount_of_viruses -= 1
        grid_slaves = root.grid_slaves()
        for l in grid_slaves:
            l.destroy()
    if notQuarantine():
        if len(autoclickers) > 0:
            virus_increaser = 1 + day / 2
        inf_virus.after(time_to_update_virus, updateVirus)


def notQuarantine():
    global virus
    global stop_number
    if virus >= stop_number:
        finalLabel1 = tk.Label(root, text="Прожито дней: " + str(day),
                               font=("Helvetica", 25)).grid(row=1, column=0)
        finalLabel = tk.Label(root, image=photo_final_virus).grid(row=2, column=0)
        title.destroy()
        return False
    else:
        return True


def changeDay():
    global day
    global time_to_plus_day

    if notQuarantine():
        day += 1
        inf_day.after(time_to_plus_day, changeDay)


def stopKorona():
    global money
    global virus
    global plus_money
    if notQuarantine():
        if virus > 0:
            virus -= 1
            money += plus_money


root = tk.Tk()
root.title("Дави их!#мирбезкороны")
root.geometry("500x500")

title = tk.Label(root, text="Давай раздавим их!", font=("Helvetica", 12))
main_text = tk.Label(root, text="Нажми Enter чтобы начать",
                     font=("Helvetica", 10))
inf_virus = tk.Label(root, text="Уровень распространения:" + str(virus),
                     font=("Helvetica", 12))
inf_day = tk.Label(root, text="День:" + str(day),
                   font=("Helvetica", 12))
inf_money = tk.Label(root, text='Деньги:' + str(money),
                     font=("Helvetica", 12))
mask_buy = tk.Button(root, text='Купи маску 10',
                     command=lambda: createAutoClicker(10, 1))
antiseptic_buy = tk.Button(root, text='Купи антисептик 50',
                           command=lambda: createAutoClicker(50, 5))
vaccine_buy = tk.Button(root, text='Купи вакцину 100',
                        command=lambda: createAutoClicker(100, 10))
button_minus_virus = tk.Button(root, text='Убить вирус', height=5,
                               background="#C71585", width=10, command=lambda: stopKorona())

title.place(x=180, y=10)
main_text.place(x=180, y=40)
inf_virus.place(x=0, y=60)
inf_day.place(x=0, y=80)
inf_money.place(x=0, y=100)
mask_buy.place(x=10, y=320)
antiseptic_buy.place(x=10, y=350)
vaccine_buy.place(x=10, y=380)
button_minus_virus.place(x=200, y=200)

photo_final_virus = tk.PhotoImage(file="virus4.png")
photo_virus = tk.PhotoImage(file="virus.png")
virus_screen = tk.Label(root, image=photo_virus)
root.bind('<Return>', play)
root.mainloop()
