from tkinter import *
import random

virus = 0
amount_of_viruses = 0
viruses = []
day = 0
Enter = True
money = 0
count = 0
autoclickers = []


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
    for i in autoclickers:
        if virus > i.get_point():
            virus -= i.get_point()
    inf_virus.after(500, autoClickersHandler)


def play(event):
    global Enter
    if not Enter:
        pass
    else:
        main_text.config(text="")
        updateVirus()
        changeDay()
        changeScrin()
        autoClickersHandler()
        Enter = False


def changeScrin():
    global virus
    global day
    global money
    inf_virus.config(text="Уровень распространения:" + str(virus))
    inf_day.config(text="День:" + str(day))
    inf_money.config(text='Деньги:' + str(money))
    virus_scrin.after(100, changeScrin)


def updateVirus():
    global viruses
    global virus
    global amount_of_viruses
    virus += 1
    if amount_of_viruses < virus // 10:
        amount_of_viruses += 1
        Label(root, image=photo_virus).grid(row=random.randint(3, 10), column=random.randint(3, 10))
        Label(root, image=photo_virus).grid(row=random.randint(3, 10), column=random.randint(3, 10))
        Label(root, image=photo_virus).grid(row=random.randint(3, 10), column=random.randint(3, 10))
    if amount_of_viruses > virus // 10:
        amount_of_viruses -= 1
        grid_slaves = root.grid_slaves()
        for l in grid_slaves:
            l.destroy()
    if notKorona():
        if len(autoclickers) > 0:
            inf_virus.after(150 - len(autoclickers) * 3, updateVirus)
        else:
            inf_virus.after(150, updateVirus)


def notKorona():
    global virus
    if virus >= 1000:
        finalLabel = Label(root, image=photo_final_virus).grid(row=0, column=0)
        return False
    else:
        return True


def changeDay():
    global day
    day += 1
    if notKorona():
        inf_day.after(5000, changeDay)


def stopKorona(event):
    global money
    global virus
    if notKorona():
        if virus > 0:
            virus -= 1
            money += 0.5


root = Tk()
root.title("Дави их!#мирбезкороны")
root.geometry("500x500")

title = Label(root, text="Давай раздавим их!", font=("Helvetica", 12))
main_text = Label(root, text="Нажми Enter чтобы начать", font=("Helvetica", 10))
inf_virus = Label(root, text="Уровень распространения:" + str(virus), font=("Helvetica", 12))
inf_day = Label(root, text="День:" + str(day), font=("Helvetica", 12))
inf_money = Label(root, text='Деньги:' + str(money), font=("Helvetica", 12))
mask_buy = Button(root, text='Купи маску 10', command=lambda: createAutoClicker(10, 1))
antiseptic_buy = Button(root, text='Купи антисептик 50', command=lambda: createAutoClicker(50, 5))
vaccine_buy = Button(root, text='Купи вакцину 100', command=lambda: createAutoClicker(100, 10))

title.place(x=180, y=10)
main_text.place(x=180, y=40)
inf_virus.place(x=0, y=60)
inf_day.place(x=0, y=80)
inf_money.place(x=0, y=100)
mask_buy.place(x=10, y=320)
antiseptic_buy.place(x=10, y=350)
vaccine_buy.place(x=10, y=380)

photo_final_virus = PhotoImage(file="virus4.png")
photo_virus = PhotoImage(file="virus.png")
virus_scrin = Label(root, image=photo_virus)

root.bind('<space>', stopKorona)
root.bind('<Return>', play)
root.mainloop()
