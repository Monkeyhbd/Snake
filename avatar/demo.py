import tkinter
import tkinter.font
import time
import threading
import random

from data import theme as DataTheme
from widget import board as WidgetBoard


# Display the Label of snake's body form place1 to place2, and return this Label object.
def show_label(master, place1, place2, w, color):
    body_label = tkinter.Label(master, bg=color)
    ex = place1[0] - place2[0]
    ey = place1[1] - place2[1]
    if ex == 0 and ey > 0:
        body_label.place(x=place2[0], y=place2[1], width=w, height=ey)
    elif ex == 0 and ey < 0:
        body_label.place(x=place2[0], y=place2[1] + ey + w, width=w, height=-ey)
    elif ex < 0 and ey == 0:
        body_label.place(x=place2[0] + ex + w, y=place2[1], width=-ex, height=w)
    elif ex > 0 and ey == 0:
        body_label.place(x=place2[0], y=place2[1], width=ex, height=w)
    return body_label


def report_len(place1, place2):
    ex = place1[0] - place2[0]
    ey = place1[1] - place2[1]
    return int((ex ** 2 + ey ** 2) ** 0.5)


# [place1] <-- [place2] : way = 'W'
def report_way(place1, place2):
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


def extend(point, point_history, n, w):
    idx = len(point) - 1
    p = point[-1]
    n = n * w
    point.pop()
    while True:
        e = report_len(p, point_history[idx])
        w = report_way(point_history[idx], p)
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


class Snake(threading.Thread):
    INIT = 0
    RUN = 1
    WAIT = 2
    END = 3
    BAD = 11

    body: list = []  # [head_label, body_label, ...]

    food: list = []  # [x, y, n, food_label]

    def __init__(self,
                 master: WidgetBoard.Board,
                 x: int = 0,
                 y: int = 0,
                 w: "the width of a block" = 20,
                 length: "initial length of snake" = 5,
                 step=2,
                 head_color: "the color of snake's head" = 'black',
                 body_color: "the color of snake's body" = 'red',
                 len_label2=None,
                 fps_label2=None,
                 progress_bar=None):
        threading.Thread.__init__(self)
        self.daemon = True
        self.master = master
        self.head = [x * w, y * w]
        self.point = [self.head, [self.head[0] - length * w, self.head[1]]]  # [头，转弯节点，转弯节点 ... 末位位置]，len >= 2
        self.point_history = [self.head, [0, self.head[1]], [-int(1000 * w), self.head[1]]]  # way = 'E'
        self.point_body = []  # 蛇身在棋盘上占据的点
        self.w = w
        self.len = length
        self.head_color = head_color
        self.body_color = body_color
        self.way = 'E'
        self.next_way = 'E'
        self.step = step

        self.condition = self.INIT
        # 0(INIT)-已初始化未开始 1(RUN)-正在运行 2(WAIT)-暂停 3(END)-停止并结束 11(BAD)-要求body_update使用body_show

        self.counter = 0

        self.len_label2 = len_label2
        self.fps_label2 = fps_label2
        self.obstacle: list = master.border + master.wall

        self.progress_bar = progress_bar  # Level mode

        self.body_show()
        self.feed()

    def body_show(self):
        idx = 0
        self.body = []
        head = tkinter.Label(self.master, bg=self.head_color)
        head.place(x=self.point[0][0], y=self.point[0][1], width=self.w, height=self.w)
        self.body.append(head)
        while True:
            self.body.append(show_label(self.master, self.point[idx], self.point[idx + 1], self.w, self.body_color))
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
        if self.condition == self.WAIT or self.condition == self.BAD or len(self.body) != len(self.point):
            self.body_reshow()
            self.condition = self.RUN
        else:
            if len(self.body) == 2:
                self.body_reshow()
            else:
                head_backup = self.body[0]
                first_body_backup = self.body[1]
                tail_backup = self.body[-1]
                self.body[0] = tkinter.Label(self.master, bg=self.head_color)
                self.body[0].place(x=self.head[0], y=self.head[1], width=self.w, height=self.w)
                self.body[1] = show_label(self.master, self.point[0], self.point[1], self.w, self.body_color)
                self.body[-1] = show_label(self.master, self.point[-2], self.point[-1], self.w, self.body_color)
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
        w = report_way(tail[0], tail[1])
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
        if self.head[0] % self.w == 0 and self.head[1] % self.w == 0:
            b = []
            a = self.point
            for idx in range(len(a) - 1):
                ex = a[idx + 1][0] - a[idx][0]
                ey = a[idx + 1][1] - a[idx][1]
                if ex == 0 and ey > 0:
                    b += [[a[idx][0], y] for y in range(a[idx][1], a[idx + 1][1], self.w)]
                elif ex == 0 and ey < 0:
                    b += [[a[idx][0], y] for y in range(a[idx][1], a[idx + 1][1], -self.w)]
                elif ex < 0 and ey == 0:
                    b += [[x, a[idx][1]] for x in range(a[idx][0], a[idx + 1][0], -self.w)]
                elif ex > 0 and ey == 0:
                    b += [[x, a[idx][1]] for x in range(a[idx][0], a[idx + 1][0], self.w)]
            self.point_body = b

    def way_change(self):
        if self.head[0] % self.w == 0 and self.head[1] % self.w == 0:
            if self.next_way != self.way:
                self.way = self.next_way
                self.point.insert(1, self.head.copy())
                self.point_history.insert(1, self.head.copy())

    def next_way_change(self, way):  # 用于方向按钮控制方向
        if not ((way in ['N', 'S'] and self.way in ['N', 'S']) or
                (way in ['W', 'E'] and self.way in ['W', 'E'])):
            self.next_way = way

    def check(self):  # Check if food or wall in front of snake.
        if self.head[0] % self.w == 0 and self.head[1] % self.w == 0:
            way = self.way
            point_dead = self.point_body + self.obstacle
            # point_dead = self.point_body + self.master.board_dead_point + self.wall_dead_point
            if way == 'N':
                if [self.head[0], self.head[1] - self.w] in point_dead:
                    self.condition = self.END
            elif way == 'S':
                if [self.head[0], self.head[1] + self.w] in point_dead:
                    self.condition = self.END
            elif way == 'W':
                if [self.head[0] - self.w, self.head[1]] in point_dead:
                    self.condition = self.END
            elif way == 'E':
                if [self.head[0] + self.w, self.head[1]] in point_dead:
                    self.condition = self.END

            food = self.food[:2]
            if way == 'N':
                if [self.head[0], self.head[1] - self.w] == food:
                    self.eat()
            elif way == 'S':
                if [self.head[0], self.head[1] + self.w] == food:
                    self.eat()
            elif way == 'W':
                if [self.head[0] - self.w, self.head[1]] == food:
                    self.eat()
            elif way == 'E':
                if [self.head[0] + self.w, self.head[1]] == food:
                    self.eat()

    def eat(self):
        self.condition = self.BAD
        self.point = extend(self.point, self.point_history, self.food[2], self.w)
        self.len += self.food[2]
        self.len_label2['text'] = self.len
        if self.progress_bar is not None:
            self.progress_bar.update(self.len / self.progress_bar.val_sum)
            if self.len >= self.progress_bar.val_sum:
                self.progress_bar.label_act['bg'] = 'Chartreuse'
        self.food[3].destroy()
        self.feed()

    def feed(self):
        self.food = [random.randint(0, self.master.size[0] - 1) * self.w,
                     random.randint(0, self.master.size[1] - 1) * self.w]
        while self.food in self.point_body + self.obstacle:
            self.food = [random.randint(0, self.master.size[0] - 1) * self.w,
                         random.randint(0, self.master.size[1] - 1) * self.w]
        self.food.append(random.randint(1, 5))
        food_label = tkinter.Label(self.master, text=self.food[2], fg='white', bg=DataTheme.food,
                                   font=tkinter.font.Font(size=int(2 * self.w ** 0.5)))
        food_label.place(x=self.food[0], y=self.food[1], width=self.w, height=self.w)
        self.food.append(food_label)

    def play(self):
        self.condition = self.RUN
        self.len_label2['text'] = self.len
        if self.progress_bar is not None:
            self.progress_bar.update(self.len / self.progress_bar.val_sum)

        fps_t = 0

        idle = 0.032  # Default, Linux.
        try:
            if self.master.master.master.os == 'Windows':
                idle = 0.02
        except AttributeError:
            import platform
            self.master.master.master.os = platform.system()
            if self.master.master.master.os == 'Windows':
                idle = 0.02

        while True:

            self.counter += 1

            t0 = time.perf_counter()

            while self.condition == self.WAIT:
                time.sleep(0.05)

            self.way_change()

            self.check()

            if self.condition == self.END:
                self.point_update()
                self.point_to_point_body()
                self.body_update()
                self.condition = self.END  # Above 3 lines of code maybe change self.condition.
                break

            self.point_update()
            self.point_to_point_body()

            self.body_update()

            if self.counter % 5 == 0:
                this_fps_t = time.perf_counter()
                # print(this_fps_t)
                self.fps_label2['text'] = format_fps((this_fps_t - fps_t) / 5)
                fps_t = this_fps_t

            te = time.perf_counter()

            tt = te - t0
            sleep_time = idle - tt

            if sleep_time > 0:
                time.sleep(sleep_time)
                # print('sleep' + str(self.counter))

    def run(self):  # Overwrite
        self.play()
