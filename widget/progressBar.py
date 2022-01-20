import tkinter

W = 20


class ProgressBar:
    def __init__(self, master, x, y, width, height, color_sum, color_act):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label_sum = tkinter.Label(master, bg=color_sum)
        self.label_act = tkinter.Label(master, bg=color_act)

    def display(self):
        self.label_sum.place(x=self.x, y=self.y, width=self.width, height=self.height)
        self.label_act.place(x=self.x, y=self.y, width=0, height=self.height)

    def destroy(self):
        self.label_act.destroy()
        self.label_sum.destroy()

    def update(self, rate):
        if rate < 0:
            rate = 0
        if rate > 1:
            rate = 1
        self.label_act.place(width=rate * self.width)


def progress_bar_init(master):
    progress_bar = ProgressBar(master, x=master.winfo_width() * 0.5 - 2.5 * W, y=0.25 * W,
                               width=5 * W, height=0.5 * W,
                               color_sum='white', color_act='red')
    progress_bar.display()
    return progress_bar
