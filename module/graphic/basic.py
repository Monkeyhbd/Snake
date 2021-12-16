import tkinter

from ..data import char as DataChar
from ..parameter import color as ParameterColor

W = 30


# [place1] <-- [place2] : way = 'W'
def report_way(place1, place2):
    ex = place1[0] - place2[0]
    ey = place1[1] - place2[1]
    if ex == 0 and ey > 0:
        return 'S'
    elif ex == 0 and ey < 0:
        return 'N'
    elif ex < 0 and ey == 0:
        return 'W'
    elif ex > 0 and ey == 0:
        return 'E'


def report_len(place1, place2):
    ex = place1[0] - place2[0]
    ey = place1[1] - place2[1]
    return int((ex ** 2 + ey ** 2) ** 0.5)


def extend(point, point_history, n):
    idx = len(point) - 1
    p = point[-1]
    n = n * W
    point.pop()
    while True:
        e = report_len(p, point_history[idx])
        w = report_way(point_history[idx], p)
        if n <= e:
            if w == 'N':
                p[1] -= n
            if w == 'S':
                p[1] += n
            if w == 'W':
                p[0] -= n
            if w == 'E':
                p[0] += n
            point.append(p)
            break
        elif n > e:
            n = n - e
            p = point_history[idx]
            idx += 1
            point.append(p.copy())
    return point


def format_fps(tt):  # basic
    if tt == 0:
        return '+∞'
    fps = str(1 / tt)
    return fps[:5]


def obj_destroy(obj_list):
    for obj in obj_list:
        obj.destroy()


# Display the Label of snake's body form place1 to place2, and return this Label object.
def show_label(master, place1, place2, color):
    body_label = tkinter.Label(master, bg=color)
    ex = place1[0] - place2[0]
    ey = place1[1] - place2[1]
    if ex == 0 and ey > 0:
        body_label.place(x=place2[0], y=place2[1], width=W, height=ey)
    elif ex == 0 and ey < 0:
        body_label.place(x=place2[0], y=place2[1] + ey + W, width=W, height=-ey)
    elif ex < 0 and ey == 0:
        body_label.place(x=place2[0] + ex + W, y=place2[1], width=-ex, height=W)
    elif ex > 0 and ey == 0:
        body_label.place(x=place2[0], y=place2[1], width=ex, height=W)
    return body_label


def wall_display(master, position_list, color, wall_dead_point, wall_list):
    wall_dead_point.clear()
    wall_list.clear()
    for position in position_list:
        wall = tkinter.Label(master, text='X', bg=color)
        wall.place(x=position[0] * W, y=position[1] * W, width=W, height=W)
        wall_list.append(wall)
        wall_dead_point.append([int(position[0] * W), position[1] * W])


def wall_destroy(wall_dead_point, wall_list):
    for wall in wall_list:
        wall.destroy()
    wall_list.clear()
    wall_dead_point.clear()


def char_display(master, c, x, y, w, color=ParameterColor.default, option='default'):
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


def str_display(master, s, x, y, w, color=ParameterColor.default, option='default'):
    w = int(w)
    obj_list = []
    for c in s:
        obj_list += char_display(master, c, x, y, w, color, option)
        x += (DataChar.char_dict[c][0] + 1) * w
    return obj_list


# Display s in the middle of an area(x, y, width, height).
def str_middle(master, s, x, y, width, height, w, color=ParameterColor.default, option='default'):
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
    obj_list = []
    for unit in data:
        pixel = tkinter.Label(master, bg=unit[2])
        pixel.place(x=x + unit[0] * w, y=y + unit[1] * w, width=w, height=w)
        obj_list.append(pixel)
    return obj_list


# Sub data can contain in data.
def graphic_display2(master, data, x, y, w):
    return graphic_display_core(master, data, x, y, w * 2)


def graphic_display_core(master, data, x, y, w):
    if type(data[0]) != list:  # Boundary condition
        pixel = tkinter.Label(master, bg=data[2])
        pixel.place(x=x + data[0] * w, y=y + data[1] * w, width=w, height=w)
        return [pixel]
    else:
        obj_list = []
        for unit in data:
            rtn = graphic_display_core(master, unit, x, y, w / 2)
            obj_list += rtn
        return obj_list
