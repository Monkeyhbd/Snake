import tkinter
import time
import threading

from avatar import demo as AvatarDemo
from widget import door as WidgetDoor
from widget import progressBar as WidgetProgressBar
from widget import pixel as WidgetPixel
from widget import panel as WidgetPanel
from widget import gameOverMessage as WidgetGameOverMessage
from data import theme as DataTheme
from data import wall as DataWall


def level_init(master, level_n):
    w = master.W
    level_info = tkinter.Label(master, bg='white')
    level_info.place(x=master.winfo_width() * 0.5 - 2.4 * w, y=21 * w + 0.1 * w, width=4.8 * w, height=0.8 * w)
    WidgetPixel.str_middle(master, s='LEVEL ' + str(level_n),
                           x=master.winfo_width() * 0.5 - 2.4 * w, y=21 * w + 0.1 * w, width=4.8 * w, height=0.8 * w,
                           w=w / 12, color=DataTheme.default)


def wall_display(master, position_list, color, wall_dead_point, wall_list):
    w = master.W
    wall_dead_point.clear()
    wall_list.clear()
    for position in position_list:
        wall = tkinter.Label(master, text='X', bg=color)
        wall.place(x=position[0] * w, y=position[1] * w, width=w, height=w)
        wall_list.append(wall)
        wall_dead_point.append([int(position[0] * w), position[1] * w])


def wall_destroy(wall_dead_point, wall_list):
    for wall in wall_list:
        wall.destroy()
    wall_list.clear()
    wall_dead_point.clear()


def obj_destroy(obj_list):
    for obj in obj_list:
        obj.destroy()


def wait_len(snake: AvatarDemo.Snake, length: int) -> bool:  # length : expected length
    w = snake.master.W
    while snake.condition != 3:
        time.sleep(1)
    if snake.len >= length and snake.head[1] == 9 * w and snake.head[0] >= 19 * w:
        return True
    else:
        return False


def level(page, level_n: int) -> bool:
    w = page.W
    wall_list = []

    # level level_n
    return_obj = WidgetDoor.door_init(page)
    door1 = return_obj['door1']
    door2 = return_obj['door2']

    progress_bar = WidgetProgressBar.progress_bar_init(page)
    progress_bar.val_sum = 30

    level_init(page, level_n)
    obj_list = WidgetPixel.str_display(master=page, s='LEVEL ' + str(level_n),
                                       x=int(page.winfo_width() * 0.4) + w * 2,
                                       y=int(page.winfo_height() * 0.4) + w * 2,
                                       w=w / 30 * 4.5, color=DataTheme.level_tip)
    time.sleep(1)
    obj_destroy(obj_list)

    wall_display(page.board, DataWall.level_box[level_n - 1], DataTheme.wall, page.board.wall, wall_list)

    monkeyhbd = AvatarDemo.Snake(master=page.board, x=1, y=10, w=w, length=5, step=int(w / 5),
                                 head_color=DataTheme.snake_head, body_color=DataTheme.snake_body,
                                 len_label2=page.len_label2, fps_label2=page.fps_label2,
                                 progress_bar=progress_bar)
    WidgetPanel.panel_init(page.master, monkeyhbd)
    monkeyhbd.level = level_n
    monkeyhbd.start()

    WidgetDoor.door_thread_create(door1, door2, monkeyhbd)
    result = wait_len(monkeyhbd, 30)
    if not result:
        print("Dead")
        WidgetGameOverMessage.exit_init(page, monkeyhbd, 'level')
        return False
    else:
        print('Access')
        if level_n == len(DataWall.level_box):  # Last level
            print("Win")

            WidgetGameOverMessage.exit_init(page, monkeyhbd, 'level_win')
        else:
            monkeyhbd.body_destroy()
            monkeyhbd.food[3].destroy()
            wall_destroy(page.board.wall, wall_list)
        return True


class Back(threading.Thread):
    def __init__(self, page):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.page = page

    def run(self):
        for level_n in range(1, len(DataWall.level_box) + 1):
            rtn = level(self.page, level_n)
            if rtn == 0:
                break
