import tkinter

W = 20
X = 40
Y = 20

current_color = 'black'
data = []  # data = [[x, y, 'color'] ... ]


class Pixel(tkinter.Button):
    def __init__(self, master, x, y):
        super().__init__(master, bg='white', command=self.click)
        self.x = x
        self.y = y
        self.condition = 0  # 0 - Unselected, 1 - Selected

    def click(self):
        if self.condition == 0:  # Unselected
            self['bg'] = current_color
            data.append([self.x, self.y, current_color])
            self.condition = 1
        else:  # Selected
            bg_backup = self['bg']
            self['bg'] = 'white'
            data.remove([self.x, self.y, bg_backup])
            self.condition = 0


def main_menu(master):
    master.update()
    bar = tkinter.Canvas(master, bg='white')
    bar.place(x=0, y=0, width=master.winfo_width(), height=1.8 * W)

    current_x = 0

    print_button = tkinter.Button(bar, text='Print', command=lambda: print(data))
    print_button.place(x=0.2 * W, y=0.2 * W, width=2 * W, height=1.4 * W)
    current_x += 0.2 * W + 2 * W

    print_without_color_button = tkinter.Button(bar, text='Print without color',
                                                command=lambda: print([x[: 2] for x in data]))
    print_without_color_button.place(x=current_x + 0.2 * W, y=0.2 * W, width=6 * W, height=1.4 * W)
    current_x += 0.2 * W + 6 * W


def paper(master, x, y, w, h):
    board = tkinter.Canvas(master)
    board.place(x=x, y=y, width=w * W, height=h * W)
    for yy in range(h):
        for xx in range(w):
            p = Pixel(board, xx, yy)
            p.place(x=xx * W, y=yy * W, width=W, height=W)
            if xx == 0:
                p['text'] = yy
            if yy == 0:
                p['text'] = xx


if __name__ == '__main__':
    lmy = tkinter.Tk()
    lmy.title('Mokey Designer')
    lmy.geometry("{}x{}".format(int(X * W), int((Y + 2) * W)))
    main_menu(lmy)
    paper(lmy, 0, 2 * W, X, Y)
    lmy.mainloop()
