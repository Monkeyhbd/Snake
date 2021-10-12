import tkinter

from . import basic as GUIBasic
from . import page as GUIPage

W = GUIBasic.W


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
    board.board_dead_point = board_dead_point
    return board


def info_init(master):
    len_label1 = tkinter.Label(master, text='len', bg='white')
    len_label1.place(x=0 + W, y=master.winfo_height() - W + 2, width=30, height=W - 4)
    len_label2 = tkinter.Label(master, bg='white')
    len_label2.place(x=35 + W, y=master.winfo_height() - W + 2, width=40, height=W - 4)

    fps_label1 = tkinter.Label(master, text='fps', bg='white')
    fps_label1.place(x=master.winfo_width() - W - 75, y=master.winfo_height() - W + 2, width=30, height=W - 4)
    fps_label2 = tkinter.Label(master, bg='white')
    fps_label2.place(x=master.winfo_width() - W - 40, y=master.winfo_height() - W + 2, width=40, height=W - 4)

    return {'len_label2': len_label2, 'fps_label2': fps_label2}


def exit_init(master, snake, mode='single'):  # master is a Page.
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
        label_game_over = tkinter.Label(exit_mess, text=snake.len, bg='white')
        label_game_over.place(x=0.5 * w + 1.6 * w, y=w + 0.5 * w, width=1.4 * w, height=0.8 * w)

        button_back = tkinter.Button(exit_mess, text='Back', command=lambda: GUIPage.main_page(master.master))
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
                                        text=str(snake.level) + ' - ' + str(snake.len), bg='white')
        label_game_over.place(x=0.5 * w + 1.6 * w, y=w + 0.5 * w, width=1.4 * w, height=0.8 * w)

        button_back = tkinter.Button(exit_mess, text='Back', command=lambda: GUIPage.main_page(master.master))
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

        button_back = tkinter.Button(exit_mess, text='Back', command=lambda: GUIPage.main_page(master.master))
        button_back.place(x=0.5 * w, y=1 * w + 0.5 * w, width=3 * w, height=w)


def level_init(master, level):
    level_info = tkinter.Label(master, text='Level ' + str(level), bg='white')
    level_info.place(x=master.winfo_width() * 0.5 - 40, y=21 * W + 2, width=80, height=W - 4)


def panel_init(master, snake):
    def snake_change_next_way(event):
        if event.keysym == 'Up':
            snake.next_way_change('N')
        if event.keysym == 'Down':
            snake.next_way_change('S')
        if event.keysym == 'Left':
            snake.next_way_change('W')
        if event.keysym == 'Right':
            snake.next_way_change('E')

    def suspend_continue_event(event):
        if event.keysym == 'space':
            suspend_continue()

    def suspend_continue():
        if snake.condition == 1:  # 正在运行-->暂停
            snake.condition = 2
        elif snake.condition == 2:  # 暂停-->正在运行
            snake.condition = 1

    master.bind('<Up>', snake_change_next_way)
    master.bind('<Down>', snake_change_next_way)
    master.bind('<Left>', snake_change_next_way)
    master.bind('<Right>', snake_change_next_way)

    master.bind('<space>', suspend_continue_event)
