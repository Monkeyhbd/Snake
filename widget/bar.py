import tkinter
import tkinter.font

from . import pixel as WidgetPixel
from data import theme as DataTheme


W = 20


def info_init(master):
    len_label1 = tkinter.Label(master, bg='white')
    len_label1.place(x=0 + W, y=master.winfo_height() - 0.9 * W, width=1.5 * W, height=0.8 * W)
    WidgetPixel.str_middle(master, s='LEN', x=0 + W, y=master.winfo_height() - 0.9 * W, width=1.5 * W, height=0.8 * W,
                           w=W / 12, color=DataTheme.default)
    len_label2 = tkinter.Label(master, bg='white', font=tkinter.font.Font(size=int(2 * W ** 0.5)))
    len_label2.place(x=0 + W + 1.5 * W + 0.1 * W, y=master.winfo_height() - 0.9 * W, width=1.5 * W, height=0.8 * W)

    fps_label1 = tkinter.Label(master, bg='white')
    fps_label1.place(x=master.winfo_width() - W - 3 * W - 0.1 * W, y=master.winfo_height() - 0.9 * W,
                     width=1.5 * W, height=0.8 * W)
    WidgetPixel.str_middle(master, s='FPS',
                           x=master.winfo_width() - W - 3 * W - 0.1 * W, y=master.winfo_height() - 0.9 * W,
                           width=1.5 * W, height=0.8 * W,
                           w=W / 12, color=DataTheme.default)
    fps_label2 = tkinter.Label(master, bg='white', font=tkinter.font.Font(size=int(2 * W ** 0.5)))
    fps_label2.place(x=master.winfo_width() - W - 1.5 * W, y=master.winfo_height() - 0.9 * W,
                     width=1.5 * W, height=0.8 * W)

    return {'len_label2': len_label2, 'fps_label2': fps_label2}
