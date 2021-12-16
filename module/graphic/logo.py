import tkinter
import random
import time

from ..data import logo as DataLogo

# The "Mokey hbd" logo's width is 38 and height is 6.


def logo_display(master, x, y, w, colors):
    obj_list = []
    logo_info = DataLogo.logo_data
    num_of_color = len(colors)
    for unit in logo_info:
        pixel = tkinter.Label(master, bg=colors[random.randint(0, num_of_color - 1)])
        pixel.place(x=x + unit[0] * w, y=y + unit[1] * w, width=w, height=w)
        obj_list.append(pixel)
    return obj_list


def logo_flash(master, x, y, w, colors, idle):
    obj_list = []
    logo_info = DataLogo.logo_data
    num_of_color = len(colors)
    for unit in logo_info:
        pixel = tkinter.Label(master, bg=colors[random.randint(0, num_of_color - 1)])
        pixel.place(x=x + unit[0] * w, y=y + unit[1] * w, width=w, height=w)
        obj_list.append(pixel)
        master.update()
        time.sleep(idle)
    return obj_list
