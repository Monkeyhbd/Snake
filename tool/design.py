import tkinter
import tkinter.filedialog
import view as ToolView

W = 20
X = 40
Y = 20

current_color = 'black'
data = []  # data = [[x, y, 'color'] ... ]
pixel_board = []  # pixel = [[pixel00, pixel10 ... ] ... ]


class Pixel(tkinter.Button):
    def __init__(self, master, x, y):
        tkinter.Button.__init__(self, master, bg='white', command=self.click)
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


def clear_paper():
    for line in pixel_board:
        for p in line:
            if p.condition == 1:
                p.click()


def optimize_data():
    optimized = [[x[0], x[1], 1, 1, x[2]] for x in data]
    flag = True
    while flag:
        flag = False
        for unit in optimized:
            if [unit[0] + 1, unit[1], 1, 1, unit[4]] in optimized:
                flag = True
                break
        width = 0
        while [unit[0] + width, unit[1], 1, 1, unit[4]] in optimized:
            optimized.remove([unit[0] + width, unit[1], 1, 1, unit[4]])
            width += 1
        optimized.append([unit[0], unit[1], width, 1, unit[4]])
    return optimized


def menu(master):
    menu_bar = tkinter.Menu()
    master['menu'] = menu_bar

    file_menu = tkinter.Menu(tearoff=0)
    menu_bar.add_cascade(label='File', menu=file_menu)

    def open_command():
        open_target = tkinter.filedialog.askopenfile()
        try:
            target_read = open_target.read()
            open_target.close()
            target_data = eval(target_read)
            clear_paper()
            for unit in target_data:
                global current_color
                current_color = unit[2]
                pixel_board[unit[1]][unit[0]].click()
        except AttributeError:  # Cancel
            pass
    file_menu.add_command(label='Open', command=open_command)

    def save_command():
        save_target = tkinter.filedialog.asksaveasfile()
        try:
            save_target.write(str(data))
            save_target.close()
        except AttributeError:  # Cancel
            pass
    file_menu.add_command(label='Save', command=save_command)


def main_menu(master):
    master.update()
    bar = tkinter.Canvas(master, bg='white')
    bar.place(x=0, y=0.1 * W, width=master.winfo_width(), height=1.8 * W)

    current_x = 0

    clear_button = tkinter.Button(bar, text='Clear', command=clear_paper)
    clear_button.place(x=0.2 * W, y=0.2 * W, width=2 * W, height=1.4 * W)
    current_x += 0.2 * W + 2 * W

    print_button = tkinter.Button(bar, text='Print', command=lambda: print(data))
    print_button.place(x=current_x + 0.2 * W, y=0.2 * W, width=2 * W, height=1.4 * W)
    current_x += 0.2 * W + 2 * W

    print_without_color_button = tkinter.Button(bar, text='Print without color',
                                                command=lambda: print([x[: 2] for x in data]))
    print_without_color_button.place(x=current_x + 0.2 * W, y=0.2 * W, width=6 * W, height=1.4 * W)
    current_x += 0.2 * W + 6 * W

    def view_command():
        print(data)
        view_window = ToolView.Application('Editing', data, W)
        view_window.display()
        view_window.mainloop()
    view_button = tkinter.Button(bar, text='View', command=view_command)
    view_button.place(x=current_x + 0.2 * W, y=0.2 * W, width=2 * W, height=1.4 * W)
    current_x += 0.2 * W + 2 * W

    def view_turbo_command():
        print(optimize_data())
        view_window = ToolView.Application('Editing', optimize_data(), W)
        view_window.display_turbo()
        view_window.mainloop()
    view_turbo_button = tkinter.Button(bar, text='View Turbo', command=view_turbo_command)
    view_turbo_button.place(x=current_x + 0.2 * W, y=0.2 * W, width=4 * W, height=1.4 * W)
    current_x += 0.2 * W + 4 * W


def paper(master, x, y, w, h):
    pixel_board.clear()
    board = tkinter.Canvas(master)
    board.place(x=x, y=y, width=w * W, height=h * W)
    for yy in range(h):
        this_line = []
        for xx in range(w):
            p = Pixel(board, xx, yy)
            p.place(x=xx * W, y=yy * W, width=W, height=W)
            this_line.append(p)
            if xx == 0:
                p['text'] = yy
            if yy == 0:
                p['text'] = xx
        pixel_board.append(this_line)


def color_bar(master, x, y, width, height):
    board = tkinter.Canvas(master, bg='white')
    board.place(x=x, y=y, width=width, height=height)
    known_color = ['black', 'red', 'orange', 'green', 'blue', 'purple',
                   'Pink', 'Crimson', 'PaleVioletRed', 'HotPink', 'DeepPink', 'Violet',
                   'Fuchsia', 'BlueViolet', 'MediumPurple', 'SkyBlue', 'DeepSkyBlue', 'Cyan',
                   'MediumSpringGreen', 'SpringGreen', 'LimeGreen', 'Lime', 'ForestGreen', 'DarkGreen',
                   'Chartreuse', 'GreenYellow', 'OliveDrab', 'Yellow', 'Gold', 'Goldenrod',
                   'Tan', 'DarkOrange', 'Peru', 'Coral', 'OrangeRed', 'Tomato',
                   'Brown', 'SaddleBrown', 'Sienna', 'Chocolate']

    def change_color_function(new_color):
        def md():
            globals()['current_color'] = new_color
        return md

    current_x, current_y = 0, 0
    for color in known_color:
        color_button = tkinter.Button(board, bg=color, command=change_color_function(color))
        color_button.place(x=current_x, y=current_y, width=W, height=W)
        current_x += W
        if current_x + W > width:  # New line.
            current_x = 0
            current_y += W


if __name__ == '__main__':
    lmy = tkinter.Tk()
    lmy.title('Mokey Designer')
    lmy.geometry("{}x{}".format(int((X + 2.2) * W), int((Y + 2) * W)))
    menu(lmy)
    main_menu(lmy)
    color_bar(lmy, 0, 2 * W, 2 * W, Y * W)
    paper(lmy, 2.2 * W, 2 * W, X, Y)
    lmy.mainloop()
