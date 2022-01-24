import tkinter
import tkinter.font

from . import pixel as WidgetPixel
from data import theme as DataTheme


def info_init(master):
    w = master.W
    len_label1 = tkinter.Label(master, bg='white')
    len_label1.place(x=0 + w, y=master.winfo_height() - 0.9 * w, width=1.5 * w, height=0.8 * w)
    WidgetPixel.str_middle(master, s='LEN', x=0 + w, y=master.winfo_height() - 0.9 * w, width=1.5 * w, height=0.8 * w,
                           w=w / 12, color=DataTheme.default)
    len_label2 = tkinter.Label(master, bg='white', font=tkinter.font.Font(size=int(2 * w ** 0.5)))
    len_label2.place(x=0 + w + 1.5 * w + 0.1 * w, y=master.winfo_height() - 0.9 * w, width=1.5 * w, height=0.8 * w)

    fps_label1 = tkinter.Label(master, bg='white')
    fps_label1.place(x=master.winfo_width() - w - 3 * w - 0.1 * w, y=master.winfo_height() - 0.9 * w,
                     width=1.5 * w, height=0.8 * w)
    WidgetPixel.str_middle(master, s='FPS',
                           x=master.winfo_width() - w - 3 * w - 0.1 * w, y=master.winfo_height() - 0.9 * w,
                           width=1.5 * w, height=0.8 * w,
                           w=w / 12, color=DataTheme.default)
    fps_label2 = tkinter.Label(master, bg='white', font=tkinter.font.Font(size=int(2 * w ** 0.5)))
    fps_label2.place(x=master.winfo_width() - w - 1.5 * w, y=master.winfo_height() - 0.9 * w,
                     width=1.5 * w, height=0.8 * w)

    return {'len_label2': len_label2, 'fps_label2': fps_label2}
