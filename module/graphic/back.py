import threading
import time

from . import basic as GUIBasic
from . import widget as GUIWidget
from . import door as GUIDoor
from . import snake as GUISnake
from ..data import wall as DataWall
from ..parameter import color as ParameterColor

W = GUIBasic.W


def single_back_create(master, monkeyhbd):
    def md():
        while monkeyhbd.condition != 3:
            time.sleep(1)
        GUIWidget.exit_init(master.current_page.root, monkeyhbd, 'single')

    single_back = threading.Thread()
    single_back.run = md
    single_back.setDaemon(True)
    single_back.start()


def level_back_create(master, board):
    def wait_len(monkeyhbd, n):  # n : expected length
        while monkeyhbd.condition != 3:
            time.sleep(1)
        if monkeyhbd.len >= n and monkeyhbd.head[1] == 9 * W and monkeyhbd.head[0] >= 19 * W:
            return 1
        else:
            return 0

    def level(level_n):
        wall_dead_point = []
        wall_list = []

        # level level_n
        return_obj = GUIDoor.door_init(master.current_page.root)
        door1 = return_obj['door1']
        door2 = return_obj['door2']

        progress_bar = GUIWidget.progress_bar_init(master.current_page.root)
        progress_bar.val_sum = 30

        GUIWidget.level_init(master.current_page.root, level_n)
        obj_list = GUIBasic.str_display(master=master.current_page.root, s='LEVEL ' + str(level_n),
                                        x=int(master.current_page.root.winfo_width() * 0.4) + W * 2,
                                        y=int(master.current_page.root.winfo_height() * 0.4) + W * 2,
                                        w=W / 30 * 4.5, color=ParameterColor.level_tip)
        time.sleep(1)
        GUIBasic.obj_destroy(obj_list)

        GUIBasic.wall_display(board, DataWall.level_box[level_n-1], ParameterColor.wall, wall_dead_point, wall_list)

        monkeyhbd = GUISnake.Snake(board, 1, 10, 5,
                                   ParameterColor.snake_head, ParameterColor.snake_body,
                                   int(W / 5), master.len_label2,
                                   master.fps_label2, wall_dead_point, progress_bar)
        GUIWidget.panel_init(master, monkeyhbd)
        monkeyhbd.level = level_n
        monkeyhbd.setDaemon(True)
        monkeyhbd.start()

        GUIDoor.door_thread_create(door1, door2, monkeyhbd)
        result = wait_len(monkeyhbd, 30)
        if result == 0:
            GUIWidget.exit_init(master.current_page.root, monkeyhbd, 'level')
            return result
        else:
            print('AC')
            if level_n == len(DataWall.level_box):  # Last level
                # monkeyhbd.body_destroy()
                # monkeyhbd.food[3].destroy()
                # GUIBasic.wall_destroy(wall_dead_point, wall_list)

                GUIWidget.exit_init(master.current_page.root, monkeyhbd, 'level_win')
            else:
                monkeyhbd.body_destroy()
                monkeyhbd.food[3].destroy()
                GUIBasic.wall_destroy(wall_dead_point, wall_list)
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
