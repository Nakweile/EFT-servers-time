import datetime as dt
import flet as ft
'''''
время может отличаться от настоящего на сервере
'''''

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



def time_set(utc):
    return (dt.datetime.utcnow() + dt.timedelta(hours=utc)).strftime("%H:%M")


def main(page: ft.Page):
    page.title = "EFT Servers time"


    t1 = ft.Text()
    t2 = ft.Text()
    t3 = ft.Text()
    t4 = ft.Text()
    t5 = ft.Text()
    t6 = ft.Text()
    t7 = ft.Text()
    t8 = ft.Text()
    t9 = ft.Text()
    t10 = ft.Text()
    t11 = ft.Text()
    t12 = ft.Text()
    t13 = ft.Text()
    t14 = ft.Text()
    t15 = ft.Text()
    t16 = ft.Text()
    t17 = ft.Text()
    t18 = ft.Text()
    t19 = ft.Text()
    t20 = ft.Text()
    t21 = ft.Text()
    t22 = ft.Text()


    page.add(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22)

    while(True):
        t1.value = f"RUSSIA CENTRAL {time_set(utc['RUSSIA CENTRAL'])}"
        t2.value = f"RUSSIA WEST {time_set(utc['RUSSIA WEST'])}"
        t3.value = f"Africa {time_set(utc['Africa'])}"
        t4.value = f"Chine {time_set(utc['Chine'])}"
        t5.value = f"Singapore {time_set(utc['Singapore'])}"
        t6.value = f"Korea {time_set(utc['Korea'])}"
        t7.value = f"Japane {time_set(utc['Japane'])}"
        t8.value = f"Australia {time_set(utc['Australia'])}"
        t9.value = f"Europe WEST {time_set(utc['Europe WEST'])}"
        t10.value = f"Europe SOUTH {time_set(utc['Europe SOUTH'])}"
        t11.value = f"Europe NORTH {time_set(utc['Europe NORTH'])}"
        t12.value = f"Europe EAST {time_set(utc['Europe EAST'])}"
        t13.value = f"Europe CENTRAL {time_set(utc['Europe CENTRAL'])}"
        t14.value = f"Middle East {time_set(utc['Middle East'])}"
        t15.value = f"ME - Dubai {time_set(utc['ME - Dubai'])}"
        t16.value = f"South America {time_set(utc['South America'])}"
        t17.value = f"SA - colombia {time_set(utc['SA - colombia'])}"
        t18.value = f"North America WEST {time_set(utc['North America WEST'])}"
        t19.value = f"North America SOUTH EAST {time_set(utc['North America SOUTH EAST'])}"
        t20.value = f"North America SOUTH {time_set(utc['North America SOUTH'])}"
        t21.value = f"North America NORTH EAST {time_set(utc['North America NORTH EAST'])}"
        t22.value = f"North America CENTRAL {time_set(utc['North America CENTRAL'])}"
        page.update()


ft.app(target=main)


