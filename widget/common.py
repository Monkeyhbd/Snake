import tkinter

from . import pixel as WidgetPixel


class Button(tkinter.Canvas):

    place_backup = tkinter.Canvas.place

    def __init__(self, master, bg='White', active_background='LightGrey', fg='Black', text='', w=1, command=None):
        tkinter.Canvas.__init__(self, master, bg=bg)
        self.bg = bg
        self.active_background = active_background
        self.fg = fg
        self.text = text
        self.w = w
        self.command = command

        def enter(_):
            self['bg'] = active_background

        def leave(_):
            self['bg'] = bg

        self.bind('<Enter>', enter)
        self.bind('<Leave>', leave)
        if command is not None:
            self.bind('<Button-1>', command)

    def place(self, *args, **kwargs):
        self.place_backup(*args, **kwargs)
        self.update()
        WidgetPixel.str_middle(self, s=self.text, x=0, y=0, width=self.winfo_width(),
                               height=self.winfo_height(), w=self.w, color=self.fg)
