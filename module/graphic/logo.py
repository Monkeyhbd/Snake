import tkinter
import random
import time

from ..data import logo as DataLogo

# The "Mokey hbd" logo's width is 38 and height is 6.


def logo_flash(master, x, y, w, colors, idle, option='default'):
    w = int(w)
    obj_list = []
    logo_info = DataLogo.logo_data
    num_of_color = len(colors)
    for unit in logo_info:
        pixel = tkinter.Label(master, bg=colors[random.randint(0, num_of_color - 1)])
        pixel.place(x=x + unit[0] * w, y=y + unit[1] * w, width=w, height=w)
        obj_list.append(pixel)
        if option == 'above':
            white = tkinter.Label(master, bg='white')
            white.place(x=x + unit[0] * w - 0.15 * w, y=y + unit[1] * w - 0.15 * w, width=1.3 * w, height=1.3 * w)
            white.lower(pixel)
            obj_list.append(white)
        if idle > 0:
            master.update()
            time.sleep(idle)
    return obj_list


def logo_display(master, x, y, w, colors, option='default'):
    w = int(w)
    rtn = logo_flash(master, x, y, w, colors, idle=-1, option=option)
    return rtn


def logo_middle(master, x, y, width, height, w, colors, option='default'):
    w = int(w)
    logo_info = DataLogo.logo_data
    max_x, max_y = 0, 0
    for unit in logo_info:
        if unit[0] > max_x:
            max_x = unit[0]
        if unit[1] > max_y:
            max_y = unit[1]
    rtn = logo_display(master,
                       x=x + 0.5 * width - 0.5 * (max_x + 1) * w,
                       y=y + 0.5 * height - 0.5 * (max_y + 1) * w,
                       w=w, colors=colors, option=option)
    return rtn
