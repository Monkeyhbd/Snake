import tkinter


def board_init(master, h, w):
    board_dead_point = []
    board = tkinter.Canvas(master)
    for a in range(h):
        board_dead_point.append([-W, a * W])  # W
        board_dead_point.append([w * W, a * W])  # E
    for b in range(w):
        board_dead_point.append([b * W, -W])  # N
        board_dead_point.append([b * W, h * W])  # S
    board.size = [w, h]
    board.place(x=W, y=W, width=w * W, height=h * W)
    for a in range(h):
        for b in range(w):
            if a % 2 - b % 2 == 0:
                tkinter.Label(board, bg='white').place(x=b * W, y=a * W, width=W, height=W)
    board.border = board_dead_point
    return board


class Board(tkinter.Canvas):
    border: list[list[int, int]] = []
    wall: list[list[int, int]] = []

    def __init__(self, master, h, w):
        tkinter.Canvas.__init__(self, master)
        self.master = master
        self.w = w
        self.h = h
        self.W = master.W
        self.size = [w, h]

        for a in range(h):
            self.border.append([-self.master.W, a * self.master.W])  # W
            self.border.append([w * self.master.W, a * self.master.W])  # E
        for b in range(w):
            self.border.append([b * self.master.W, -self.master.W])  # N
            self.border.append([b * self.master.W, h * self.master.W])  # S

    def build(self):
        width = self.master.W
        for a in range(self.h):
            for b in range(self.w):
                if a % 2 - b % 2 == 0:
                    tkinter.Label(self, bg='white').place(x=b * width, y=a * width, width=width, height=width)

    def display(self):
        self.place(x=self.master.W, y=self.master.W, width=self.w * self.master.W, height=self.h * self.master.W)
        self.build()
