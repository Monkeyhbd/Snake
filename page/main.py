import tkinter

from . import demo as PageDemo
from data import graphic as DataGraphic
from data import logo as DataLogo
from data import theme as DataTheme
from widget import pixel as WidgetPixel
from widget import light as WidgetLight
from thread import light as ThreadLight


class Page(PageDemo.Page):
    def __init__(self, master):
        PageDemo.Page.__init__(self, master=master)

    def custom_button(self):
        W = self.W
        f11 = tkinter.Label(self, bg='LimeGreen')
        f11.place(x=20 * W, y=5 * W, width=3 * W, height=1 * W)
        f12 = tkinter.Label(self, bg='LimeGreen')
        f12.place(x=19 * W, y=6 * W, width=5 * W, height=1 * W)
        f13 = tkinter.Label(self, bg='LimeGreen')
        f13.place(x=18 * W, y=7 * W, width=7 * W, height=1 * W)

        def f1_enter(_):
            for f1 in [f11, f12, f13]:
                f1['bg'] = 'SpringGreen'

        def f1_leave(_):
            for f1 in [f11, f12, f13]:
                f1['bg'] = 'LimeGreen'

        def f1_click(_):
            pass
            # game_single(master)

        for f in [f11, f12, f13]:
            f.bind('<Enter>', f1_enter)
            f.bind('<Leave>', f1_leave)
            f.bind('<Button-1>', f1_click)

        f21 = tkinter.Label(self, bg='ForestGreen')
        f21.place(x=19 * W, y=8 * W, width=5 * W, height=1 * W)
        f22 = tkinter.Label(self, bg='ForestGreen')
        f22.place(x=18 * W, y=9 * W, width=7 * W, height=1 * W)
        f23 = tkinter.Label(self, bg='ForestGreen')
        f23.place(x=17 * W, y=10 * W, width=9 * W, height=1 * W)

        def f2_enter(_):
            for f2 in [f21, f22, f23]:
                f2['bg'] = 'SpringGreen'

        def f2_leave(_):
            for f2 in [f21, f22, f23]:
                f2['bg'] = 'ForestGreen'

        def f2_click(_):
            pass
            # game_level_mode(master)

        for f in [f21, f22, f23]:
            f.bind('<Enter>', f2_enter)
            f.bind('<Leave>', f2_leave)
            f.bind('<Button-1>', f2_click)

    def build(self):
        W = self.W
        WidgetPixel.graphic_display_turbo(self, DataGraphic.christmas_optimized, W, W, W)

        self.custom_button()

        WidgetPixel.str_middle(master=self, s='SNAKE',
                               x=20 * W, y=2.75 * W, width=3 * W, height=2 * W,
                               w=0.1 * W, color=DataTheme.snake_logo, option='above')

        WidgetPixel.str_middle(master=self, s='SINGLE',
                               x=19 * W, y=6 * W, width=5 * W, height=2 * W,
                               w=0.14 * W, color=DataTheme.single_theme, option='above')

        WidgetPixel.str_middle(master=self, s='LEVEL MODE',
                               x=19 * W, y=9 * W, width=5 * W, height=2 * W,
                               w=0.14 * W, color=DataTheme.level_theme, option='above')

        WidgetPixel.logo_middle(self,
                                x=19 * W, y=12 * W, width=5 * W, height=2 * W,
                                w=0.2 * W, logo_info=DataLogo.logo_data, colors=DataTheme.mokey_logo_colors,
                                option='above')

        WidgetLight.W = self.W
        light1 = WidgetLight.light_display(self, x=18, y=11, width=7, height=0.8,
                                           light_width_range=[2, 2.5], idle_range=[5, 8])
        light2 = WidgetLight.light_display(self, x=19, y=8, width=5, height=0.7,
                                           light_width_range=[2, 2.5], idle_range=[4, 7])
        light3 = WidgetLight.light_display(self, x=20, y=5, width=3, height=0.6,
                                           light_width_range=[1.8, 2.2], idle_range=[3, 5])

        td = ThreadLight.Flash(light1 + light2 + light3)
        td.setDaemon(True)
        self.threads.append(td)


page_instance: Page


def init(master):
    global page_instance
    page_instance = Page(master=master)


def display():
    global page_instance
    page_instance.display()
