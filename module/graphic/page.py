import tkinter
import time
import random

from . import basic as GUIBasic
from . import widget as GUIWidget
from . import snake as GUISnake
from . import back as GUIBack
from . import logo as GUILogo
from . import light as GUILight
from ..data import logo as DataLogo
from ..data import graphic as DataGraphic
from ..parameter import color as ParameterColor

W = GUIBasic.W


class Page:
    def __init__(self, master, x, y, width, height):
        self.master = master
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.root = tkinter.Canvas(self.master)

    def display(self):
        self.root.place(x=self.x, y=self.y, width=self.width, height=self.height)

    def destroy(self):
        self.root.destroy()


def welcome_page(master):
    if master.current_page is not None:
        master.current_page.destroy()

    welcome = Page(master, x=0, y=0, width=master.winfo_width(), height=master.winfo_height())
    welcome.display()
    welcome.root.update()
    master.current_page = welcome

    logo_info = DataLogo.logo_info

    w = 0.5 * W

    logo_board = tkinter.Canvas(welcome.root)
    logo_board.place(x=0.5 * master.winfo_width() - 20 * w, y=0.5 * master.winfo_height() - 10 * w,
                     width=40 * w, height=20 * w)

    color = ParameterColor.mokey_logo_colors
    for x in logo_info:
        block = tkinter.Label(logo_board, bg=color[random.randint(0, len(color) - 1)])
        block.place(x=x[0] * w, y=x[1] * w, width=w, height=w)
        time.sleep(0.03)
        welcome.root.update()

    welcome.root.update()

    # Total: 2.5s
    for _ in range(50):
        time.sleep(0.05)
        welcome.root.update()

    main_page(master)


def main_page(master):
    if master.current_page is not None:
        master.current_page.destroy()

    game_main = Page(master, x=0, y=0, width=master.winfo_width(), height=master.winfo_height())
    game_main.display()
    game_main.root.update()
    master.current_page = game_main

    GUIBasic.graphic_display(game_main.root, DataGraphic.christmas, W, W, W)

    GUIBasic.str_middle(master=game_main.root, s='SNAKE',
                        x=20 * W, y=2.75 * W, width=3 * W, height=2 * W,
                        w=0.1 * W, color=ParameterColor.snake_logo, option='above')

    f11 = tkinter.Label(game_main.root, bg='LimeGreen')
    f11.place(x=20 * W, y=5 * W, width=3 * W, height=1 * W)
    f12 = tkinter.Label(game_main.root, bg='LimeGreen')
    f12.place(x=19 * W, y=6 * W, width=5 * W, height=1 * W)
    f13 = tkinter.Label(game_main.root, bg='LimeGreen')
    f13.place(x=18 * W, y=7 * W, width=7 * W, height=1 * W)

    def f1_enter(_):
        for f1 in [f11, f12, f13]:
            f1['bg'] = 'SpringGreen'

    def f1_leave(_):
        for f1 in [f11, f12, f13]:
            f1['bg'] = 'LimeGreen'

    def f1_click(_):
        game_single(master)

    for f in [f11, f12, f13]:
        f.bind('<Enter>', f1_enter)
        f.bind('<Leave>', f1_leave)
        f.bind('<Button-1>', f1_click)

    # button_single = tkinter.Button(game_main.root, text='', command=lambda: game_single(master))
    # button_single.place(x=19.25 * W, y=6.5 * W, width=4.5 * W, height=1 * W)

    GUIBasic.str_middle(master=game_main.root, s='SINGLE',
                        x=19 * W, y=6 * W, width=5 * W, height=2 * W,
                        w=0.14 * W, color=ParameterColor.single_theme, option='above')

    f21 = tkinter.Label(game_main.root, bg='ForestGreen')
    f21.place(x=19 * W, y=8 * W, width=5 * W, height=1 * W)
    f22 = tkinter.Label(game_main.root, bg='ForestGreen')
    f22.place(x=18 * W, y=9 * W, width=7 * W, height=1 * W)
    f23 = tkinter.Label(game_main.root, bg='ForestGreen')
    f23.place(x=17 * W, y=10 * W, width=9 * W, height=1 * W)

    def f2_enter(_):
        for f2 in [f21, f22, f23]:
            f2['bg'] = 'SpringGreen'

    def f2_leave(_):
        for f2 in [f21, f22, f23]:
            f2['bg'] = 'ForestGreen'

    def f2_click(_):
        game_level_mode(master)

    for f in [f21, f22, f23]:
        f.bind('<Enter>', f2_enter)
        f.bind('<Leave>', f2_leave)
        f.bind('<Button-1>', f2_click)

    # button_level = tkinter.Button(game_main.root, text='', command=lambda: game_level_mode(master))
    # button_level.place(x=19.25 * W, y=9.5 * W, width=4.5 * W, height=1 * W)

    GUIBasic.str_middle(master=game_main.root, s='LEVEL MODE',
                        x=19 * W, y=9 * W, width=5 * W, height=2 * W,
                        w=0.14 * W, color=ParameterColor.level_theme, option='above')

    GUILogo.logo_middle(game_main.root,
                        x=19 * W, y=12 * W, width=5 * W, height=2 * W,
                        w=0.2 * W, colors=ParameterColor.mokey_logo_colors, option='above')

    light1 = GUILight.light_display(game_main.root, x=18, y=11, width=7, height=0.8,
                                    light_width_range=[2, 2.5], idle_range=[5, 8])
    light2 = GUILight.light_display(game_main.root, x=19, y=8, width=5, height=0.7,
                                    light_width_range=[2, 2.5], idle_range=[4, 7])
    light3 = GUILight.light_display(game_main.root, x=20, y=5, width=3, height=0.6,
                                    light_width_range=[1.8, 2.2], idle_range=[3, 5])

    GUILight.light_thread_create(light1 + light2 + light3)


def game_single(master):
    if master.current_page is not None:
        master.current_page.destroy()

    page_single = Page(master, x=0, y=0, width=master.winfo_width(), height=master.winfo_height())
    page_single.display()
    page_single.root.update()
    master.current_page = page_single

    border_color = ParameterColor.single_theme
    tkinter.Label(page_single.root, bg=border_color).place(x=0,
                                                           y=0,
                                                           width=page_single.root.winfo_width(),
                                                           height=W)
    tkinter.Label(page_single.root, bg=border_color).place(x=0,
                                                           y=page_single.root.winfo_height() - W,
                                                           width=page_single.root.winfo_width(),
                                                           height=W)
    tkinter.Label(page_single.root, bg=border_color).place(x=0,
                                                           y=W,
                                                           width=W,
                                                           height=page_single.root.winfo_height() - 2 * W)
    tkinter.Label(page_single.root, bg=border_color).place(x=page_single.root.winfo_width() - W,
                                                           y=W,
                                                           width=W,
                                                           height=page_single.root.winfo_height() - 2 * W)

    board = GUIWidget.board_init(page_single.root, 20, 40)
    return_obj = GUIWidget.info_init(page_single.root)
    master.len_label2 = return_obj['len_label2']
    master.fps_label2 = return_obj['fps_label2']

    monkeyhbd = GUISnake.Snake(board, 1, 10, 15,
                               ParameterColor.snake_head, ParameterColor.snake_body,
                               int(W / 5), master.len_label2, master.fps_label2, [])
    GUIWidget.panel_init(master, monkeyhbd)
    monkeyhbd.setDaemon(True)
    monkeyhbd.start()

    GUIBack.single_back_create(master, monkeyhbd)


def game_level_mode(master):
    if master.current_page is not None:
        master.current_page.destroy()

    page_single = Page(master, x=0, y=0, width=master.winfo_width(), height=master.winfo_height())
    page_single.display()
    page_single.root.update()
    master.current_page = page_single

    border_color = ParameterColor.level_theme
    tkinter.Label(page_single.root, bg=border_color).place(x=0,
                                                           y=0,
                                                           width=page_single.root.winfo_width(),
                                                           height=W)
    tkinter.Label(page_single.root, bg=border_color).place(x=0,
                                                           y=page_single.root.winfo_height() - W,
                                                           width=page_single.root.winfo_width(),
                                                           height=W)
    tkinter.Label(page_single.root, bg=border_color).place(x=0,
                                                           y=W,
                                                           width=W,
                                                           height=page_single.root.winfo_height() - 2 * W)
    tkinter.Label(page_single.root, bg=border_color).place(x=page_single.root.winfo_width() - W,
                                                           y=W,
                                                           width=W,
                                                           height=page_single.root.winfo_height() - 2 * W)

    board = GUIWidget.board_init(page_single.root, 20, 40)
    return_obj = GUIWidget.info_init(page_single.root)
    master.len_label2 = return_obj['len_label2']
    master.fps_label2 = return_obj['fps_label2']

    GUIBack.level_back_create(master, board)
