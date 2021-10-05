import tkinter
import time
import copy
import threading
import random

import module.data.logo as DataLogo
import module.data.char as DataChar
import module.data.wall as DataWall
import module.graphic.basic as GUIBasic

W = 30


class Public:
    board_dead_point = []  # *W
    wall_dead_point = []  # *W

    # 显示从place1到place2的蛇身Label，返回Label对象
    # Display the Label of snake's body form place1 to place2, and return this Label object.
    def show_label(master, place1, place2, color):  # basic
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

    # [place1] <-- [place2] : way = 'W'
    def report_way(place1, place2):  # basic
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

    def report_len(place1, place2):  # basic
        ex = place1[0] - place2[0]
        ey = place1[1] - place2[1]
        return int((ex ** 2 + ey ** 2) ** 0.5)

    def extend(point, point_history, n):  # basic
        idx = len(point) - 1
        p = point[-1]
        n = n * W
        point.pop()
        while True:
            e = Public.report_len(p, point_history[idx])
            w = Public.report_way(point_history[idx], p)
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


class GUI:
    current_page = None
    wall_list = []

    def win_init():
        globals()['lmy'] = tkinter.Tk()
        lmy.title('贪吃蛇')
        lmy.geometry('1260x660')
        lmy.update()

    def board_init(master, h=20, w=40):  # widget
        board = tkinter.Canvas(master)
        GUI.board = board
        for a in range(h):
            Public.board_dead_point.append([-W, a * W])  # W
            Public.board_dead_point.append([w * W, a * W])  # E
        for b in range(w):
            Public.board_dead_point.append([b * W, -W])  # N
            Public.board_dead_point.append([b * W, h * W])  # S
        board.size = [w, h]
        board.place(x=W, y=W, width=w * W, height=h * W)
        for a in range(h):
            for b in range(w):
                if a % 2 - b % 2 == 0:
                    tkinter.Label(board, bg='white').place(x=b * W, y=a * W, width=W, height=W)

        return board

    def wall_display(master, position_list, color='green'):  # basic
        for position in position_list:
            wall = tkinter.Label(master, text='X', bg=color)
            wall.place(x=position[0] * W, y=position[1] * W, width=W, height=W)
            GUI.wall_list.append(wall)
            Public.wall_dead_point.append([int(position[0] * W), position[1] * W])

    def wall_destroy():
        for wall in GUI.wall_list:
            wall.destroy()
        GUI.wall_list = []
        Public.wall_dead_point = []

    def door_init(master):
        bg1 = tkinter.Label(master, bg='white')
        bg1.place(x=0, y=int(W * 11), width=W, height=W)
        GUI.door1 = tkinter.Label(master, bg='black')
        GUI.door1.condition = 1  # open
        GUI.door1.root = master
        GUI.door1.place(x=int(W * 0.8), y=int(W * 11), width=int(W * 0.2), height=0)

        bg2 = tkinter.Label(master, bg='white')
        bg2.place(x=int(41 * W), y=int(W * 10), width=W, height=W)
        GUI.door2 = tkinter.Label(master, bg='black')
        GUI.door2.condition = 0  # close
        GUI.door2.root = master
        GUI.door2.place(x=int(41 * W), y=int(W * 10), width=int(W * 0.2), height=W)

    def door_open_close(door):
        if door.condition == 1:  # open
            door.condition = 0
            for x in range(1, 21):
                if monkeyhbd.condition == 3:
                    break
                door.place(height=int(W * 0.05 * x))
                door.root.update()
                time.sleep(0.05)
        else:  # open
            door.condition = 1
            for x in range(20, 0, -1):
                if monkeyhbd.condition == 3:
                    break
                door.place(height=int(W * 0.05 * x))
                door.root.update()
                time.sleep(0.05)

    def door_thread_creat():
        def md():
            time.sleep(3)
            GUI.door_open_close(GUI.door1)

            while monkeyhbd.len < 30 and monkeyhbd.condition != 3:
                time.sleep(1)

            if monkeyhbd.condition != 3:
                GUI.door_open_close(GUI.door2)

        door_thread = threading.Thread()
        door_thread.run = md
        door_thread.setDaemon(True)
        door_thread.start()

    def panel_init(master):
        def monkeyhbd_change_helpway(event):
            if event.keysym == 'Up':
                monkeyhbd.next_way_change('N')
            if event.keysym == 'Down':
                monkeyhbd.next_way_change('S')
            if event.keysym == 'Left':
                monkeyhbd.next_way_change('W')
            if event.keysym == 'Right':
                monkeyhbd.next_way_change('E')

        def suspend_continue_event(event):
            if event.keysym == 'space':
                suspend_continue()

        def suspend_continue():
            if monkeyhbd.condition == 1:  # 正在运行-->暂停
                monkeyhbd.condition = 2
            elif monkeyhbd.condition == 2:  # 暂停-->正在运行
                monkeyhbd.condition = 1

        lmy.bind('<Up>', monkeyhbd_change_helpway)
        lmy.bind('<Down>', monkeyhbd_change_helpway)
        lmy.bind('<Left>', monkeyhbd_change_helpway)
        lmy.bind('<Right>', monkeyhbd_change_helpway)

        lmy.bind('<space>', suspend_continue_event)

    def info_init(master):
        GUI.len_label1 = tkinter.Label(master, text='len', bg='white')
        GUI.len_label1.place(x=0 + W, y=master.winfo_height() - W + 2, width=30, height=W - 4)
        GUI.len_label2 = tkinter.Label(master, bg='white')
        GUI.len_label2.place(x=35 + W, y=master.winfo_height() - W + 2, width=40, height=W - 4)

        GUI.fps_label1 = tkinter.Label(master, text='fps', bg='white')
        GUI.fps_label1.place(x=master.winfo_width() - W - 75, y=master.winfo_height() - W + 2, width=30, height=W - 4)
        GUI.fps_label2 = tkinter.Label(master, bg='white')
        GUI.fps_label2.place(x=master.winfo_width() - W - 40, y=master.winfo_height() - W + 2, width=40, height=W - 4)

    def exit_init(master, mode='single'):
        if mode == 'single':
            exit_mess = tkinter.Canvas(master, bg='orange')
            w = int(1.5 * W)
            exit_mess.place(x=0.5 * master.winfo_width() - int(2 * w),
                            y=int(master.winfo_height() / 2) - int(2 * w),
                            width=4 * w,
                            height=4 * w)
            label_game_over = tkinter.Label(exit_mess, text='游戏结束', bg='white')
            label_game_over.place(x=0.5 * w, y=0.5 * w, width=3 * w, height=0.8 * w)

            label_score1 = tkinter.Label(exit_mess, text='得分', bg='white')
            label_score1.place(x=0.5 * w, y=w + 0.5 * w, width=1.4 * w, height=0.8 * w)
            label_game_over = tkinter.Label(exit_mess, text=monkeyhbd.len, bg='white')
            label_game_over.place(x=0.5 * w + 1.6 * w, y=w + 0.5 * w, width=1.4 * w, height=0.8 * w)

            button_back = tkinter.Button(exit_mess, text='Back', command=lambda: GUI.game_init())
            button_back.place(x=0.5 * w, y=2 * w + 0.5 * w, width=3 * w, height=w)

        if mode == 'level':
            exit_mess = tkinter.Canvas(master, bg='orange')
            w = int(1.5 * W)
            exit_mess.place(x=0.5 * master.winfo_width() - int(2 * w),
                            y=int(master.winfo_height() / 2) - int(2 * w),
                            width=4 * w,
                            height=4 * w)
            label_game_over = tkinter.Label(exit_mess, text='闯关失败', bg='white')
            label_game_over.place(x=0.5 * w, y=0.5 * w, width=3 * w, height=0.8 * w)

            label_score1 = tkinter.Label(exit_mess, text='得分', bg='white')
            label_score1.place(x=0.5 * w, y=w + 0.5 * w, width=1.4 * w, height=0.8 * w)
            label_game_over = tkinter.Label(exit_mess,
                                            text=str(monkeyhbd.level) + ' - ' + str(monkeyhbd.len), bg='white')
            label_game_over.place(x=0.5 * w + 1.6 * w, y=w + 0.5 * w, width=1.4 * w, height=0.8 * w)

            button_back = tkinter.Button(exit_mess, text='Back', command=lambda: GUI.game_init())
            button_back.place(x=0.5 * w, y=2 * w + 0.5 * w, width=3 * w, height=w)

        if mode == 'level_win':
            exit_mess = tkinter.Canvas(master, bg='orange')
            w = int(1.5 * W)
            exit_mess.place(x=0.5 * master.winfo_width() - int(2 * w),
                            y=int(master.winfo_height() / 2) - int(1.5 * w),
                            width=4 * w,
                            height=3 * w)
            label_game_over = tkinter.Label(exit_mess, text='闯关成功', bg='white', fg='red')
            label_game_over.place(x=0.5 * w, y=0.5 * w, width=3 * w, height=0.8 * w)

            button_back = tkinter.Button(exit_mess, text='Back', command=lambda: GUI.game_init())
            button_back.place(x=0.5 * w, y=1 * w + 0.5 * w, width=3 * w, height=w)

    def level_init(master, level):
        level_info = tkinter.Label(master, text='Level ' + str(level), bg='white')
        level_info.place(x=master.winfo_width() * 0.5 - 40, y=21 * W + 2, width=80, height=W - 4)

    def char_display(master, c, x, y, w, color='black'):
        position_list = DataChar.char_dict[c][1:]
        GUI_obj = []
        for position in position_list:
            block = tkinter.Label(master, bg=color)
            block.place(x=x + int((position[0]) * w), y=y + int((position[1]) * w), width=w, height=w)
            GUI_obj.append(block)
        return GUI_obj

    def str_display(master, s, x, y, w, color='black'):
        GUI_obj = []
        for c in s:
            GUI_obj += GUI.char_display(master, c, x, y, w, color)
            x += (DataChar.char_dict[c][0] + 1) * w
        return GUI_obj

    def obj_destroy(GUI_obj):
        for obj in GUI_obj:
            obj.destroy()

    def welcome_init():
        if GUI.current_page is not None:
            GUI.current_page.destroy()

        page_welcome = Page(lmy, x=0, y=0, width=lmy.winfo_width(), height=lmy.winfo_height())
        page_welcome.display()
        page_welcome.root.update()
        GUI.current_page = page_welcome

        logo_info = DataLogo.logo_info

        w = 0.5 * W

        logo_board = tkinter.Canvas(page_welcome.root)
        logo_board.place(x=0.5 * lmy.winfo_width() - 20 * w, y=0.5 * lmy.winfo_height() - 10 * w,
                         width=40 * w, height=20 * w)

        color = ['purple', 'blue', 'orange', 'red', 'green']
        for x in logo_info:
            block = tkinter.Label(logo_board, bg=color[random.randint(0, len(color) - 1)])
            block.place(x=x[0] * w, y=x[1] * w, width=w, height=w)
            time.sleep(0.03)
            page_welcome.root.update()

        page_welcome.root.update()

        # Total: 2.5s
        for x in range(50):
            time.sleep(0.05)
            page_welcome.root.update()

        GUI.game_init()

    def game_init():
        if GUI.current_page is not None:
            GUI.current_page.destroy()

        page_welcom = Page(lmy, x=0, y=0, width=lmy.winfo_width(), height=lmy.winfo_height())
        page_welcom.display()
        page_welcom.root.update()
        GUI.current_page = page_welcom

        GUI.str_display(master=page_welcom.root, s='SNAKE 2',
                        x=int(page_welcom.root.winfo_width() * 0.4) - W,
                        y=W * 2,
                        w=W / 30 * 10, color='purple')

        button_single = tkinter.Button(page_welcom.root, text='', command=lambda: GUI.game_single())
        button_single.place(x=int(page_welcom.root.winfo_width() * 0.4),
                            y=int(page_welcom.root.winfo_height() * 0.4),
                            width=int(page_welcom.root.winfo_width() * 0.2),
                            height=int(page_welcom.root.winfo_height() * 0.1))

        GUI.str_display(master=page_welcom.root, s='SINGLE MODE',
                        x=int(page_welcom.root.winfo_width() * 0.4) + W / 3,
                        y=int(page_welcom.root.winfo_height() * 0.4) + W / 1.5,
                        w=W / 30 * 4.5, color='green')

        button_level = tkinter.Button(page_welcom.root, text='', command=lambda: GUI.game_level_mode())
        button_level.place(x=int(page_welcom.root.winfo_width() * 0.4),
                           y=int(page_welcom.root.winfo_height() * 0.5),
                           width=int(page_welcom.root.winfo_width() * 0.2),
                           height=int(page_welcom.root.winfo_height() * 0.1))

        GUI.str_display(master=page_welcom.root, s='LEVEL MODE',
                        x=int(page_welcom.root.winfo_width() * 0.4) + W / 1.5,
                        y=int(page_welcom.root.winfo_height() * 0.5) + W / 1.5,
                        w=W / 30 * 4.5, color='orange')

        logo_info = DataLogo.logo_info

        w = 0.2 * W

        logo_board = tkinter.Canvas(GUI.current_page.root)
        logo_board.place(x=0.5 * lmy.winfo_width() - 20 * w, y=lmy.winfo_height() - 20 * w,
                         width=40 * w, height=20 * w)

        color = ['purple', 'blue', 'orange', 'red', 'green']
        for x in logo_info:
            block = tkinter.Label(logo_board, bg=color[random.randint(0, len(color) - 1)])
            block.place(x=x[0] * w, y=x[1] * w, width=w, height=w)

    def game_single():
        if GUI.current_page is not None:
            GUI.current_page.destroy()

        page_single = Page(lmy, x=0, y=0, width=lmy.winfo_width(), height=lmy.winfo_height())
        page_single.display()
        page_single.root.update()
        GUI.current_page = page_single

        tkinter.Label(page_single.root, bg='green').place(x=0,
                                                          y=0,
                                                          width=page_single.root.winfo_width(),
                                                          height=W)
        tkinter.Label(page_single.root, bg='green').place(x=0,
                                                          y=page_single.root.winfo_height() - W,
                                                          width=page_single.root.winfo_width(),
                                                          height=W)
        tkinter.Label(page_single.root, bg='green').place(x=0,
                                                          y=W,
                                                          width=W,
                                                          height=page_single.root.winfo_height() - 2 * W)
        tkinter.Label(page_single.root, bg='green').place(x=page_single.root.winfo_width() - W,
                                                          y=W,
                                                          width=W,
                                                          height=page_single.root.winfo_height() - 2 * W)

        board = GUI.board_init(page_single.root)
        GUI.panel_init(page_single.root)
        GUI.info_init(page_single.root)

        global monkeyhbd
        monkeyhbd = Snake(board, 1, 10, 15, 'black', 'red', int(W / 5))
        monkeyhbd.setDaemon(True)
        monkeyhbd.start()

        Back.single_back_creat()

    def game_level_mode():
        if GUI.current_page is not None:
            GUI.current_page.destroy()

        page_single = Page(lmy, x=0, y=0, width=lmy.winfo_width(), height=lmy.winfo_height())
        page_single.display()
        page_single.root.update()
        GUI.current_page = page_single

        tkinter.Label(page_single.root, bg='orange').place(x=0,
                                                           y=0,
                                                           width=page_single.root.winfo_width(),
                                                           height=W)
        tkinter.Label(page_single.root, bg='orange').place(x=0,
                                                           y=page_single.root.winfo_height() - W,
                                                           width=page_single.root.winfo_width(),
                                                           height=W)
        tkinter.Label(page_single.root, bg='orange').place(x=0,
                                                           y=W,
                                                           width=W,
                                                           height=page_single.root.winfo_height() - 2 * W)
        tkinter.Label(page_single.root, bg='orange').place(x=page_single.root.winfo_width() - W,
                                                           y=W,
                                                           width=W,
                                                           height=page_single.root.winfo_height() - 2 * W)

        board = GUI.board_init(page_single.root)
        GUI.panel_init(page_single.root)
        GUI.info_init(page_single.root)

        Back.level_back_creat()


class Page:
    def __init__(self, master, x, y, width, height):
        self.master = master
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.inside = []

        self.root = tkinter.Canvas(self.master)

    def display(self, flash=False):
        self.root.place(x=self.x, y=self.y, width=self.width, height=self.height)

    def destroy(self, flash=False):
        self.root.destroy()


class Snake(threading.Thread):
    def __init__(self, master, x, y, n, head_color='black', body_color='red', step=2):
        threading.Thread.__init__(self)
        self.master = master
        self.head = [x * W, y * W]
        self.point = [self.head, [self.head[0] - n * W, self.head[1]]]  # [头，转弯节点，转弯节点 ... 末位位置]，len >= 2
        self.point_history = [self.head, [0, self.head[1]], [-int(10 * W), self.head[1]]]  # way = 'E'
        self.point_body = []  # 蛇身在棋盘上占据的点
        self.food = []  # [x, y, n, food_label]
        self.body = []  # [head_label, body_label, ...]
        self.len = n
        self.body_color = body_color
        self.head_color = head_color
        self.way = 'E'
        self.next_way = 'E'
        self.step = step
        self.condition = 0  # 0-已初始化未开始 1-正在运行 2-暂停 3-停止并结束 11-要求body_update使用body_show

        self.counter = 0

        self.body_show()
        self.feed()

    def body_show(self):
        idx = 0
        self.body = []
        head = tkinter.Label(self.master, bg=self.head_color)
        head.place(x=self.point[0][0], y=self.point[0][1], width=W, height=W)
        self.body.append(head)
        while True:
            self.body.append(GUIBasic.show_label(self.master, self.point[idx], self.point[idx + 1], self.body_color))
            idx += 1
            if idx == len(self.point) - 1:
                break

    def body_destroy(self):
        for body_label in self.body:
            body_label.destroy()
        self.body = []

    def body_update(self):
        if self.condition == 11 or self.condition == 2:
            body_backup = self.body
            self.body_show()
            self.master.update()
            for body_label in body_backup:
                body_label.destroy()
            self.condition = 1
        elif len(self.body) != len(self.point):  # 尾已经减为0，或新增了转弯节点
            body_backup = self.body
            self.body_show()
            self.master.update()
            for body_label in body_backup:
                body_label.destroy()
        else:
            if len(self.body) == 2:  # 只有head和一个body
                body_backup = self.body
                self.body_show()
                self.master.update()
                for body_label in body_backup:
                    body_label.destroy()
            else:
                head_backup = self.body[0]
                first_body_backup = self.body[1]
                tail_backup = self.body[-1]
                self.body[0] = tkinter.Label(self.master, bg=self.head_color)
                self.body[0].place(x=self.head[0], y=self.head[1], width=W, height=W)
                self.body[1] = GUIBasic.show_label(self.master, self.point[0], self.point[1], self.body_color)
                self.body[-1] = GUIBasic.show_label(self.master, self.point[-2], self.point[-1], self.body_color)
                self.master.update()
                head_backup.destroy()
                first_body_backup.destroy()
                tail_backup.destroy()

    def point_update(self):
        # 更新头部
        if self.way == 'N':
            self.head[1] -= self.step
        if self.way == 'S':
            self.head[1] += self.step
        if self.way == 'W':
            self.head[0] -= self.step
        if self.way == 'E':
            self.head[0] += self.step
        # 更新尾部
        tail = self.point[-2:]  # tail = [[20, 40], [20, 100]] --> w = 'N'
        w = Public.report_way(tail[0], tail[1])
        if w == 'N':
            self.point[-1][1] -= self.step
        if w == 'S':
            self.point[-1][1] += self.step
        if w == 'W':
            self.point[-1][0] -= self.step
        if w == 'E':
            self.point[-1][0] += self.step

        if self.point[-1] == self.point[-2]:
            self.point.pop()

    def point_to_point_body(self):
        if self.head[0] % W == 0 and self.head[1] % W == 0:
            b = []
            a = self.point
            for idx in range(len(a) - 1):
                ex = a[idx + 1][0] - a[idx][0]
                ey = a[idx + 1][1] - a[idx][1]
                if ex == 0 and ey > 0:
                    b += [[a[idx][0], y] for y in range(a[idx][1], a[idx + 1][1], W)]
                elif ex == 0 and ey < 0:
                    b += [[a[idx][0], y] for y in range(a[idx][1], a[idx + 1][1], -W)]
                elif ex < 0 and ey == 0:
                    b += [[x, a[idx][1]] for x in range(a[idx][0], a[idx + 1][0], -W)]
                elif ex > 0 and ey == 0:
                    b += [[x, a[idx][1]] for x in range(a[idx][0], a[idx + 1][0], W)]
            self.point_body = b

    def way_change(self):
        if self.head[0] % W == 0 and self.head[1] % W == 0:
            if self.next_way != self.way:
                self.way = self.next_way
                self.point.insert(1, self.head.copy())
                self.point_history.insert(1, self.head.copy())

    def next_way_change(self, way):  # 用于方向按钮控制方向
        if not ((way in ['N', 'S'] and self.way in ['N', 'S']) or
                (way in ['W', 'E'] and self.way in ['W', 'E'])):
            self.next_way = way

    def check(self):
        if self.head[0] % W == 0 and self.head[1] % W == 0:
            way = self.way
            point_dead = self.point_body + Public.board_dead_point + Public.wall_dead_point
            if way == 'N':
                if [self.head[0], self.head[1] - W] in point_dead:
                    self.condition = 3
            elif way == 'S':
                if [self.head[0], self.head[1] + W] in point_dead:
                    self.condition = 3
            elif way == 'W':
                if [self.head[0] - W, self.head[1]] in point_dead:
                    self.condition = 3
            elif way == 'E':
                if [self.head[0] + W, self.head[1]] in point_dead:
                    self.condition = 3

            food = self.food[:2]
            if way == 'N':
                if [self.head[0], self.head[1] - W] == food:
                    self.condition = 11
                    self.point = Public.extend(self.point, self.point_history, self.food[2])
                    self.len += self.food[2]
                    self.food[3].destroy()
                    self.feed()
            elif way == 'S':
                if [self.head[0], self.head[1] + W] == food:
                    self.condition = 11
                    self.point = Public.extend(self.point, self.point_history, self.food[2])
                    self.len += self.food[2]
                    self.food[3].destroy()
                    self.feed()
            elif way == 'W':
                if [self.head[0] - W, self.head[1]] == food:
                    self.condition = 11
                    self.point = Public.extend(self.point, self.point_history, self.food[2])
                    self.len += self.food[2]
                    self.food[3].destroy()
                    self.feed()
            elif way == 'E':
                if [self.head[0] + W, self.head[1]] == food:
                    self.condition = 11
                    self.point = Public.extend(self.point, self.point_history, self.food[2])
                    self.len += self.food[2]
                    self.food[3].destroy()
                    self.feed()

    def feed(self):
        GUI.len_label2['text'] = self.len
        self.food = [random.randint(0, self.master.size[0] - 1) * W,
                     random.randint(0, self.master.size[1] - 1) * W]
        while self.food in self.point_body + Public.wall_dead_point:
            self.food = [random.randint(0, self.master.size[0] - 1) * W,
                         random.randint(0, self.master.size[1] - 1) * W]
        self.food.append(random.randint(1, 3))
        food_label = tkinter.Label(self.master, text=self.food[2], fg='white', bg='blue')
        food_label.place(x=self.food[0], y=self.food[1], width=W, height=W)
        self.food.append(food_label)

    def play(self):
        self.condition = 1

        while True:

            self.counter += 1

            t0 = time.perf_counter()

            while self.condition == 2:
                time.sleep(0.05)

            if self.condition == 3:
                break

            self.way_change()

            self.check()

            self.point_update()
            self.point_to_point_body()

            self.body_update()

            te = time.perf_counter()

            tt = te - t0
            sleep_time = 0.02 - tt

            if sleep_time > 0:
                time.sleep(sleep_time)
                # print('sleep' + str(self.counter))

            if self.counter % 5 == 0:
                GUI.fps_label2['text'] = Public.format_fps(time.perf_counter() - t0)

    def run(self):  # Overwrite
        self.play()


class Back:
    def single_back_creat():
        def md():
            while monkeyhbd.condition != 3:
                time.sleep(1)
            GUI.exit_init(GUI.current_page.root)

        single_back = threading.Thread()
        single_back.run = md
        single_back.setDaemon(True)
        single_back.start()

    def level_back_creat():
        def wait_len(n):
            while monkeyhbd.condition != 3:
                time.sleep(1)
            if monkeyhbd.len >= n and monkeyhbd.head[1] == 9 * W and monkeyhbd.head[0] >= 19 * W:
                return 1
            else:
                return 0

        def md():
            Public.wall_dead_point = []
            for x in range(1):

                # level 1
                GUI.door_init(GUI.current_page.root)

                GUI.level_init(GUI.current_page.root, 1)
                GUI_obj = GUI.str_display(master=GUI.current_page.root, s='LEVEL 1',
                                          x=int(GUI.current_page.root.winfo_width() * 0.4) + W * 2,
                                          y=int(GUI.current_page.root.winfo_height() * 0.4) + W * 2,
                                          w=W / 30 * 4.5, color='red')
                time.sleep(1)
                GUI.obj_destroy(GUI_obj)

                GUI.wall_display(GUI.board, DataWall.level1, 'green')

                global monkeyhbd
                monkeyhbd = Snake(GUI.board, 1, 10, 15, 'black', 'red', int(W / 5))
                monkeyhbd.level = 1
                monkeyhbd.setDaemon(True)
                monkeyhbd.start()

                GUI.door_thread_creat()
                result = wait_len(30)
                if result == 0:
                    GUI.exit_init(GUI.current_page.root, 'level')
                    break
                else:
                    print('AC')
                monkeyhbd.body_destroy()
                monkeyhbd.food[3].destroy()
                GUI.wall_destroy()

                # level 2
                GUI.door_init(GUI.current_page.root)

                GUI.level_init(GUI.current_page.root, 2)
                GUI_obj = GUI.str_display(master=GUI.current_page.root, s='LEVEL 2',
                                          x=int(GUI.current_page.root.winfo_width() * 0.4) + W * 2,
                                          y=int(GUI.current_page.root.winfo_height() * 0.4) + W * 2,
                                          w=W / 30 * 4.5, color='red')
                time.sleep(1)
                GUI.obj_destroy(GUI_obj)

                GUI.wall_display(GUI.board, DataWall.level2, 'green')

                monkeyhbd = Snake(GUI.board, 1, 10, 15, 'black', 'red', int(W / 5))
                monkeyhbd.level = 2
                monkeyhbd.setDaemon(True)
                monkeyhbd.start()

                GUI.door_thread_creat()
                result = wait_len(30)
                if result == 0:
                    GUI.exit_init(GUI.current_page.root, 'level')
                    break
                else:
                    print('AC')
                monkeyhbd.body_destroy()
                monkeyhbd.food[3].destroy()
                GUI.wall_destroy()

                # level 3
                GUI.door_init(GUI.current_page.root)

                GUI.level_init(GUI.current_page.root, 3)
                GUI_obj = GUI.str_display(master=GUI.current_page.root, s='LEVEL 3',
                                          x=int(GUI.current_page.root.winfo_width() * 0.4) + W * 2,
                                          y=int(GUI.current_page.root.winfo_height() * 0.4) + W * 2,
                                          w=W / 30 * 4.5, color='red')
                time.sleep(1)
                GUI.obj_destroy(GUI_obj)

                GUI.wall_display(GUI.board, DataWall.level3, 'green')

                monkeyhbd = Snake(GUI.board, 1, 10, 15, 'black', 'red', int(W / 5))
                monkeyhbd.level = 3
                monkeyhbd.setDaemon(True)
                monkeyhbd.start()

                GUI.door_thread_creat()
                result = wait_len(30)
                if result == 0:
                    GUI.exit_init(GUI.current_page.root, 'level')
                    break
                else:
                    print('AC')

                # win
                GUI.exit_init(GUI.current_page.root, 'level_win')

            Public.wall_dead_point = []

        level_back = threading.Thread()
        level_back.run = md
        level_back.setDaemon(True)
        level_back.start()


if __name__ == '__main__':
    GUI.win_init()
    GUI.welcome_init()
    lmy.mainloop()
