from tkinter import *
import datetime as dt
import time
'''''
время может отличаться от настоящего на сервере
'''''
# константы
WINDOW_W = 400
WINDOW_H = 1000
BG_COLOR = '#C0C0C0'
FG_COLOR = 'white'


utc = {
    'RUSSIA CENTRAL':7,
    'RUSSIA WEST':3,
    'RUSSIA EAST':10,
    'Africa':3,
    'Chine':8,
    'Singapore':8,
    'Korea':9,
    'Japane':9,
    'Australia':10,
    'Europe WEST':0,
    'Europe SOUTH':3,
    'Europe NORTH':2,
    'Europe EAST':3,
    'Europe CENTRAL':1,
    'Middle East':3,
    'ME - Dubai':4,
    'South America':3,
    'SA - colombia':5,
    'North America WEST':8,
    'North America SOUTH EAST':5,
    'North America SOUTH':7,
    'North America NORTH EAST':5,
    'North America CENTRAL':6
}


# Сервер : UTC для регионов
servers = {
    'RUSSIA CENTRAL':None,
    'RUSSIA WEST':None,
    'RUSSIA EAST':None,
    'Africa':None,
    'Chine':None,
    'Singapore':None,
    'Korea':None,
    'Japane':None,
    'Australia':None,
    'Europe WEST':None,
    'Europe SOUTH':None,
    'Europe NORTH':None,
    'Europe EAST':None,
    'Europe CENTRAL':None,
    'Middle East':None,
    'ME - Dubai':None,
    'South America':None,
    'SA - colombia':None,
    'North America WEST':None,
    'North America SOUTH EAST':None,
    'North America SOUTH':None,
    'North America NORTH EAST':None,
    'North America CENTRAL':None
}

text_list = []

# форматирование времени до видо Ч:М:С
def formated_time(server):
    return server.strftime("%H:%M")


# присвоение значений для словаря servers из переменной time_test
def set_time():
    for i in servers:
        servers[i] = dt.datetime.utcnow() + dt.timedelta(hours=utc[i])
    return servers


# вывод сервера и времени в окне
def output():
    global text_list
    for i in servers:
        text = Label(root, text=i + "----------" + formated_time(servers[i]), font=('Arial 100', 12), bg=BG_COLOR)
        text.pack()
        text_list.append(text)
    pass


def del_():
    global text_list
    for i in text_list:
        i.destroy()
    text_list = []
    pass


def update():
    set_time()
    output()
    #root.after(1000, update)
    pass




root = Tk()
root.title("EFT Servers time")
root.resizable(False, False)
canvas = Canvas(root, bg=BG_COLOR, height=WINDOW_H, width=WINDOW_W)
canvas.place(x=-10, y=-10)
root.geometry('300x550')


#set_time()
#output()
update()

root.mainloop()

