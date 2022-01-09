import tkinter
import time

from data import char as DataChar


def char_display(master, c, x, y, w, color, option='default'):
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
    str_width = 0
    for c in s:
        str_width += (DataChar.char_dict[c][0] + 1) * w
    str_width -= w  # The space between two character
    str_height = 5 * w
    str_x = x + 0.5 * width - 0.5 * str_width
    str_y = y + 0.5 * height - 0.5 * str_height
    rtn = str_display(master, s, str_x, str_y, w, color, option)
    return rtn
