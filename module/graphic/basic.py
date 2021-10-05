import tkinter


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
