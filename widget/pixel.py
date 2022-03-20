import tkinter
import time
import random

from data import char as DataChar


def char_display(master, c, x, y, w, color, option='default'):
    x, y = int(x), int(y)
    w = int(w)
    position_list = DataChar.char_dict[c][1:]
    obj_list = []
    for position in position_list:
        block = tkinter.Label(master, bg=color)
        block.place(x=x + int((position[0]) * w), y=y + int((position[1]) * w), width=w, height=w)
        obj_list.append(block)
        if option == 'above':
            white = tkinter.Label(master, bg='white')
            boundary_width = int(0.15 * w)
            if boundary_width < 1:
                boundary_width = 1
            white.place(x=x + position[0] * w - boundary_width, y=y + position[1] * w - boundary_width,
                        width=w + 2 * boundary_width, height=w + 2 * boundary_width)
            white.lower(obj_list[0])
            obj_list.append(white)
    return obj_list


def str_one_by_one(master, s, x, y, w, color, idle, option='default'):
    obj_list = []
    for c in s:
        obj_list += char_display(master, c, x, y, w, color, option)
        x += (DataChar.char_dict[c][0] + 1) * w
        master.update()
        time.sleep(idle)
    return obj_list


def str_display(master, s, x, y, w, color, option='default'):
    obj_list = []
    for c in s:
        obj_list += char_display(master, c, x, y, w, color, option)
        x += (DataChar.char_dict[c][0] + 1) * w
    return obj_list


# Display s in the middle of an area(x, y, width, height).
def str_middle(master, s, x, y, width, height, w, color, option='default'):
    w = int(w)
    str_width = 0
    for c in s:
        str_width += (DataChar.char_dict[c][0] + 1) * w
    str_width -= w  # The space between two character
    str_height = 5 * w
    str_x = x + 0.5 * width - 0.5 * str_width
    str_y = y + 0.5 * height - 0.5 * str_height
    rtn = str_display(master, s, str_x, str_y, w, color, option)
    return rtn


def graphic_display(master, data, x, y, w):
    w = int(w)
    obj_list = []
    for unit in data:
        pixel = tkinter.Label(master, bg=unit[2])
        pixel.place(x=x + unit[0] * w, y=y + unit[1] * w, width=w, height=w)
        obj_list.append(pixel)
    return obj_list


def graphic_middle(master, data, x, y, width, height, w):
    w = int(w)
    graphic_width, graphic_height = 0, 0
    for position in data:
        if position[0] + 1 > graphic_width:
            graphic_width = position[0] + 1
        if position[1] + 1 > graphic_height:
            graphic_height = position[1] + 1
    graphic_width *= w
    graphic_height *= w
    graphic_x = x + 0.5 * width - 0.5 * graphic_width
    graphic_y = y + 0.5 * height - 0.5 * graphic_width
    rtn = graphic_display(master=master, data=data, x=graphic_x, y=graphic_y, w=w)
    return rtn


def graphic_display_turbo(master, data, x, y, w):
    w = int(w)
    obj_list = []
    for unit in data:
        pixel = tkinter.Label(master, bg=unit[4])
        pixel.place(x=x + unit[0] * w, y=y + unit[1] * w, width=unit[2] * w, height=unit[3] * w)
        obj_list.append(pixel)
    return obj_list


def logo_flash(master, x, y, w, logo_info, colors, idle, option='default'):
    w = int(w)
    obj_list = []
    num_of_color = len(colors)
    for unit in logo_info:
        pixel = tkinter.Label(master, bg=colors[random.randint(0, num_of_color - 1)])
        pixel.place(x=x + unit[0] * w, y=y + unit[1] * w, width=w, height=w)
        obj_list.append(pixel)
        if option == 'above':
            white = tkinter.Label(master, bg='white')
            boundary_width = int(0.15 * w)
            if boundary_width < 1:
                boundary_width = 1
            white.place(x=x + unit[0] * w - boundary_width, y=y + unit[1] * w - boundary_width,
                        width=w + 2 * boundary_width, height=w + 2 * boundary_width)
            white.lower(obj_list[0])
            obj_list.append(white)
        if idle > 0:
            master.update()
            time.sleep(idle)
    return obj_list


def logo_display(master, x, y, w, logo_info, colors, option='default'):
    w = int(w)
    rtn = logo_flash(master, x, y, w, logo_info, colors, idle=-1, option=option)
    return rtn


def logo_middle(master, x, y, width, height, w, logo_info, colors, option='default'):
    w = int(w)
    max_x, max_y = 0, 0
    for unit in logo_info:
        if unit[0] > max_x:
            max_x = unit[0]
        if unit[1] > max_y:
            max_y = unit[1]
    rtn = logo_display(master,
                       x=x + 0.5 * width - 0.5 * (max_x + 1) * w,
                       y=y + 0.5 * height - 0.5 * (max_y + 1) * w,
                       w=w, logo_info=logo_info, colors=colors, option=option)
    return rtn
