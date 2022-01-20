import tkinter
import time
import threading

from data import theme as DataTheme

W = 20


def door_init(master):
    bg1 = tkinter.Label(master, bg='white')
    bg1.place(x=0, y=int(W * 11), width=W, height=W)
    door1 = tkinter.Label(master, bg=DataTheme.default)
    door1.condition = 1  # open
    door1.root = master
    door1.place(x=int(W * 0.8), y=int(W * 11), width=int(W * 0.2), height=0)

    bg2 = tkinter.Label(master, bg='white')
    bg2.place(x=int(41 * W), y=int(W * 10), width=W, height=W)
    door2 = tkinter.Label(master, bg=DataTheme.default)
    door2.condition = 0  # close
    door2.root = master
    door2.place(x=int(41 * W), y=int(W * 10), width=int(W * 0.2), height=W)

    return {'door1': door1, 'door2': door2}


def door_open_close(door, snake):
    if door.condition == 1:  # open
        door.condition = 0
        for x in range(1, 21):
            if snake.condition == 3:
                break
            door.place(height=int(W * 0.05 * x))
            door.root.update()
            time.sleep(0.05)
    else:  # open
        door.condition = 1
        for x in range(20, 0, -1):
            if snake.condition == 3:
                break
            door.place(height=int(W * 0.05 * x))
            door.root.update()
            time.sleep(0.05)


def door_thread_create(door1, door2, snake):
    def md():
        time.sleep(3)
        door_open_close(door1, snake)

        while snake.len < 30 and snake.condition != 3:
            time.sleep(1)

        if snake.condition != 3:
            door_open_close(door2, snake)

    door_thread = threading.Thread()
    door_thread.run = md
    door_thread.setDaemon(True)
    door_thread.start()
