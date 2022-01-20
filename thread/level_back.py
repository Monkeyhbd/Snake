import tkinter
import time
import threading

from avatar import demo as AvatarDemo
from widget import board as WidgetBoard
from widget import door as WidgetDoor
from widget import progressBar as WidgetProgressBar
from widget import pixel as WidgetPixel
from widget import panel as WidgetPanel
from data import theme as DataTheme
from data import wall as DataWall

W = 20


def level_init(master, level):
    level_info = tkinter.Label(master, bg='white')
    level_info.place(x=master.winfo_width() * 0.5 - 2.4 * W, y=21 * W + 0.1 * W, width=4.8 * W, height=0.8 * W)
    WidgetPixel.str_middle(master, s='LEVEL ' + str(level),
                           x=master.winfo_width() * 0.5 - 2.4 * W, y=21 * W + 0.1 * W, width=4.8 * W, height=0.8 * W,
                           w=W / 12, color=DataTheme.default)


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


def obj_destroy(obj_list):
    for obj in obj_list:
        obj.destroy()


def level_back_create(page, board: WidgetBoard.Board):
    def wait_len(monkeyhbd, n):  # n : expected length
        while monkeyhbd.condition != 3:
            time.sleep(1)
        if monkeyhbd.len >= n and monkeyhbd.head[1] == 9 * W and monkeyhbd.head[0] >= 19 * W:
            return 1
        else:
            return 0

    def level(level_n):
        wall_list = []

        # level level_n
        return_obj = WidgetDoor.door_init(page)
        door1 = return_obj['door1']
        door2 = return_obj['door2']

        progress_bar = WidgetProgressBar.progress_bar_init(page)
        progress_bar.val_sum = 30

        level_init(page, level_n)
        obj_list = WidgetPixel.str_display(master=page, s='LEVEL ' + str(level_n),
                                           x=int(page.winfo_width() * 0.4) + W * 2,
                                           y=int(page.winfo_height() * 0.4) + W * 2,
                                           w=W / 30 * 4.5, color=DataTheme.level_tip)
        time.sleep(1)
        obj_destroy(obj_list)

        wall_display(board, DataWall.level_box[level_n - 1], DataTheme.wall, board.wall, wall_list)

        monkeyhbd = AvatarDemo.Snake(master=board, x=1, y=10, length=5, step=int(W / 5),
                                     head_color=DataTheme.snake_head, body_color=DataTheme.snake_body,
                                     len_label2=page.len_label2, fps_label2=page.fps_label2,
                                     progress_bar=progress_bar)
        WidgetPanel.panel_init(page.master, monkeyhbd)
        monkeyhbd.level = level_n
        monkeyhbd.start()

        WidgetDoor.door_thread_create(door1, door2, monkeyhbd)
        result = wait_len(monkeyhbd, 30)
        if result == 0:
            print("Dead")
            # GUIWidget.exit_init(master.current_page.root, monkeyhbd, 'level')
            return result
        else:
            print('AC')
            if level_n == len(DataWall.level_box):  # Last level
                print("Win")

                # GUIWidget.exit_init(master.current_page.root, monkeyhbd, 'level_win')
            else:
                monkeyhbd.body_destroy()
                monkeyhbd.food[3].destroy()
                wall_destroy(board.wall, wall_list)
                print(board.wall)
            return 1

    def md():
        for level_n in range(1, len(DataWall.level_box) + 1):
            rtn = level(level_n)
            if rtn == 0:
                break

    level_back = threading.Thread()
    level_back.run = md
    level_back.setDaemon(True)
    level_back.start()
