import tkinter

from . import basic as GUIBasic
from ..data import char as DataChar


W = GUIBasic.W


def board_init(master, h, w, board_dead_point):
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
    return board
