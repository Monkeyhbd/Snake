import tkinter
import random

from . import basic as GUIBasic
from ..parameter import color as ParameterColor


W = GUIBasic.W


def f3_line(x, width, height):
    return x * (width * W - x) / W / width / width * 4 * height


def light_display(master, x, y, width, height, light_width_range, idle_range):  # (2, 2.5) (5, 8)
    obj_list = []
    xx = W / 8
    colors = ParameterColor.light_colors
    num_of_color = len(colors)
    while xx < width * W - W / 5:
        light_width = W / 90 * 0.01 * random.uniform(light_width_range[0] * 100, light_width_range[1] * 100)
        lb = tkinter.Label(master, bg=colors[random.randint(0, num_of_color - 1)])
        lb.place(x=x * W + xx, y=y * W + f3_line(x=xx, width=width, height=height),
                 width=W / 10 * light_width, height=W / 10 * light_width)
        obj_list.append(lb)
        xx += W / 10 * 0.01 * random.uniform(idle_range[0] * 100, idle_range[1] * 100)
