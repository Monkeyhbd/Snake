import tkinter
import time
import random

from . import pixel as WidgetPixel
from data import theme as DataTheme
from data import logo as DataLogo

W = 20


def exit_init(master, snake, mode='single'):  # master is a Page.
    global W
    W = master.W

    if mode == 'single':
        exit_mess = tkinter.Canvas(master, bg=DataTheme.exit_mess)
        w = int(1.5 * W)
        exit_mess.place(x=0.5 * master.winfo_width() - int(1.7 * w),
                        y=int(master.winfo_height() / 2) - int(1.7 * w),
                        width=3.4 * w,
                        height=3.4 * w)
        label_game_over = tkinter.Label(exit_mess, bg='white')
        label_game_over.place(x=0.2 * w, y=0.2 * w, width=3 * w, height=0.8 * w)
        WidgetPixel.str_middle(exit_mess, s='GAME OVER', x=0.2 * w, y=0.2 * w, width=3 * w, height=0.8 * w,
                               w=0.1 * W, color=DataTheme.exit_win)

        label_score1 = tkinter.Label(exit_mess, bg='white')
        label_score1.place(x=0.2 * w, y=0.7 * w + 0.5 * w, width=1.4 * w, height=0.8 * w)
        WidgetPixel.str_middle(exit_mess, s='SCORE', x=0.2 * w, y=0.7 * w + 0.5 * w, width=1.4 * w, height=0.8 * w,
                               w=0.068 * W, color=DataTheme.default)
        label_score2 = tkinter.Label(exit_mess, bg='white')
        label_score2.place(x=0.2 * w + 1.6 * w, y=0.7 * w + 0.5 * w, width=1.4 * w, height=0.8 * w)
        WidgetPixel.str_middle(exit_mess, s=str(snake.len),
                               x=0.2 * w + 1.6 * w, y=0.7 * w + 0.5 * w, width=1.4 * w, height=0.8 * w,
                               w=0.068 * W, color=DataTheme.default)

        def md():
            master.destroy()

        button_back = tkinter.Button(exit_mess, command=md)
        button_back.place(x=0.2 * w, y=1.7 * w + 0.5 * w, width=3 * w, height=w)
        WidgetPixel.str_middle(exit_mess, s='BACK', x=0.2 * w, y=1.7 * w + 0.5 * w, width=3 * w, height=w,
                               w=0.1 * W, color=DataTheme.default)

    if mode == 'level':
        exit_mess = tkinter.Canvas(master, bg=DataTheme.exit_mess)
        w = int(1.5 * W)
        exit_mess.place(x=0.5 * master.winfo_width() - int(1.7 * w),
                        y=int(master.winfo_height() / 2) - int(1.7 * w),
                        width=3.4 * w,
                        height=3.4 * w)
        label_game_over = tkinter.Label(exit_mess, bg='white')
        label_game_over.place(x=0.2 * w, y=0.2 * w, width=3 * w, height=0.8 * w)
        WidgetPixel.str_middle(exit_mess, s='F A I L', x=0.2 * w, y=0.2 * w, width=3 * w, height=0.8 * w,
                               w=0.12 * W, color=DataTheme.exit_fail)

        label_score1 = tkinter.Label(exit_mess, bg='white')
        label_score1.place(x=0.2 * w, y=w + 0.2 * w, width=1.4 * w, height=0.8 * w)
        WidgetPixel.str_middle(exit_mess, s='SCORE', x=0.2 * w, y=w + 0.2 * w, width=1.4 * w, height=0.8 * w,
                               w=0.068 * W, color=DataTheme.default)
        label_score2 = tkinter.Label(exit_mess, bg='white')
        label_score2.place(x=0.2 * w + 1.6 * w, y=w + 0.2 * w, width=1.4 * w, height=0.8 * w)
        WidgetPixel.str_middle(exit_mess, s=str(snake.level) + ' - ' + str(snake.len),
                               x=0.2 * w + 1.6 * w, y=w + 0.2 * w, width=1.4 * w, height=0.8 * w,
                               w=0.068 * W, color=DataTheme.default)

        def md():
            master.destroy()

        button_back = tkinter.Button(exit_mess, command=md)
        button_back.place(x=0.2 * w, y=2 * w + 0.2 * w, width=3 * w, height=w)
        WidgetPixel.str_middle(exit_mess, s='BACK', x=0.2 * w, y=2 * w + 0.2 * w, width=3 * w, height=w,
                               w=0.1 * W, color=DataTheme.default)

    if mode == 'level_win':
        w = 0.5 * W
        logo_board_border = tkinter.Canvas(master, bg=DataTheme.exit_mess)
        logo_board_border.place(x=int(master.winfo_width() * 0.5 - 20.3 * w),
                                y=int(master.winfo_height() * 0.5 - 4.3 * w),
                                width=int(40.6 * w), height=int(8.6 * w))
        logo_board = tkinter.Canvas(master)
        logo_board.place(x=int(master.winfo_width() * 0.5 - 20 * w), y=int(master.winfo_height() * 0.5 - 4 * w),
                         width=int(40 * w), height=int(8 * w))
        logo_info = DataLogo.logo_info
        color = DataTheme.mokey_logo_colors
        block_list = []
        for x in logo_info:
            block = tkinter.Label(logo_board, bg=color[random.randint(0, len(color) - 1)])
            block.place(x=x[0] * w, y=x[1] * w - 6 * w, width=w, height=w)
            block_list.append(block)
            time.sleep(0.02)
            logo_board.update()
        time.sleep(2)
        for block in block_list:
            block.destroy()
            time.sleep(0.03)
            logo_board.update()

        WidgetPixel.str_middle(master, s='SUCCESS',
                               x=int(master.winfo_width() * 0.5 - 20 * w), y=int(master.winfo_height() * 0.5 - 4 * w),
                               width=int(40 * w), height=int(8 * w),
                               w=0.3 * W, color=DataTheme.exit_win)
        master.update()

        time.sleep(1)
        exit_mess = tkinter.Canvas(master, bg=DataTheme.exit_mess)
        exit_mess.place(x=0.5 * master.winfo_width() - int(1.5 * W),
                        y=int(master.winfo_height() / 2) + int(3.0 * W),
                        width=3 * W,
                        height=1.4 * W)

        def md():
            master.destroy()

        button_back = tkinter.Button(exit_mess, command=md)
        button_back.place(x=0.15 * W, y=0.15 * W, width=2.7 * W, height=1.1 * W)
        WidgetPixel.str_middle(master, s='BACK',
                               x=0.5 * master.winfo_width() - int(1.5 * W),
                               y=int(master.winfo_height() / 2) + int(3.0 * W),
                               width=3 * W,
                               height=1.4 * W,
                               w=0.1 * W, color=DataTheme.default)
        master.update()
