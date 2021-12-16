import tkinter
import tkinter.font
import time
import threading
import random

from . import basic as GUIBasic
from ..parameter import color as ParameterColor

W = GUIBasic.W

INIT = 0
RUN = 1
WAIT = 2
END = 3
BAD = 11


class Snake(threading.Thread):
    def __init__(self, master, x, y, n, head_color='black', body_color='red', step=2, len_label2=None, fps_label2=None,
                 wall_dead_point=[]):
        threading.Thread.__init__(self)
        self.master = master
        self.head = [x * W, y * W]
        self.point = [self.head, [self.head[0] - n * W, self.head[1]]]  # [头，转弯节点，转弯节点 ... 末位位置]，len >= 2
        self.point_history = [self.head, [0, self.head[1]], [-int(1000 * W), self.head[1]]]  # way = 'E'
        self.point_body = []  # 蛇身在棋盘上占据的点
        self.food = []  # [x, y, n, food_label]
        self.body = []  # [head_label, body_label, ...]
        self.len = n
        self.body_color = body_color
        self.head_color = head_color
        self.way = 'E'
        self.next_way = 'E'
        self.step = step

        self.condition = INIT
        # 0(INIT)-已初始化未开始 1(RUN)-正在运行 2(WAIT)-暂停 3(END)-停止并结束 11(BAD)-要求body_update使用body_show

        self.counter = 0

        self.len_label2 = len_label2
        self.fps_label2 = fps_label2
        self.wall_dead_point = wall_dead_point

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

    def body_reshow(self):
        body_backup = self.body
        self.body_show()
        self.master.update()
        for body_label in body_backup:
            body_label.destroy()

    # 1.由暂停状态恢复，其他情况 2.尾已经减为0，或新增了转弯节点 3.只有head和一个body
    def body_update(self):
        if self.condition == WAIT or self.condition == BAD or len(self.body) != len(self.point):
            self.body_reshow()
            self.condition = RUN
        else:
            if len(self.body) == 2:
                self.body_reshow()
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
        w = GUIBasic.report_way(tail[0], tail[1])
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

    def check(self):  # Check if food or wall in front of snake.
        if self.head[0] % W == 0 and self.head[1] % W == 0:
            way = self.way
            point_dead = self.point_body + self.master.board_dead_point + self.wall_dead_point
            if way == 'N':
                if [self.head[0], self.head[1] - W] in point_dead:
                    self.condition = END
            elif way == 'S':
                if [self.head[0], self.head[1] + W] in point_dead:
                    self.condition = END
            elif way == 'W':
                if [self.head[0] - W, self.head[1]] in point_dead:
                    self.condition = END
            elif way == 'E':
                if [self.head[0] + W, self.head[1]] in point_dead:
                    self.condition = END

            food = self.food[:2]
            if way == 'N':
                if [self.head[0], self.head[1] - W] == food:
                    self.eat()
            elif way == 'S':
                if [self.head[0], self.head[1] + W] == food:
                    self.eat()
            elif way == 'W':
                if [self.head[0] - W, self.head[1]] == food:
                    self.eat()
            elif way == 'E':
                if [self.head[0] + W, self.head[1]] == food:
                    self.eat()

    def eat(self):
        self.condition = BAD
        self.point = GUIBasic.extend(self.point, self.point_history, self.food[2])
        self.len += self.food[2]
        self.len_label2['text'] = self.len
        self.food[3].destroy()
        self.feed()

    def feed(self):
        self.food = [random.randint(0, self.master.size[0] - 1) * W,
                     random.randint(0, self.master.size[1] - 1) * W]
        while self.food in self.point_body + self.wall_dead_point:
            self.food = [random.randint(0, self.master.size[0] - 1) * W,
                         random.randint(0, self.master.size[1] - 1) * W]
        self.food.append(random.randint(1, 3))
        food_label = tkinter.Label(self.master, text=self.food[2], fg='white', bg=ParameterColor.food,
                                   font=tkinter.font.Font(size=int(2 * W ** 0.5)))
        food_label.place(x=self.food[0], y=self.food[1], width=W, height=W)
        self.food.append(food_label)

    def play(self):
        self.condition = RUN
        self.len_label2['text'] = self.len

        while True:

            self.counter += 1

            t0 = time.perf_counter()

            while self.condition == WAIT:
                time.sleep(0.05)

            self.way_change()

            self.check()

            if self.condition == END:
                self.point_update()
                self.point_to_point_body()
                self.body_update()
                self.condition = END  # Above 3 lines of code maybe change self.condition.
                break

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
                self.fps_label2['text'] = GUIBasic.format_fps(time.perf_counter() - t0)

    def run(self):  # Overwrite
        self.play()
