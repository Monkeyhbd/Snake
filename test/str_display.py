import tkinter

import module.graphic.basic as GUIBasic

if __name__ == '__main__':
    lmy = tkinter.Tk()
    lmy.geometry("600x400")
    lmy.update()
    GUIBasic.str_display(lmy, s="PYTHON", x=0, y=0, w=5, color='black')
    GUIBasic.str_display(lmy, s="C PLUS PLUS", x=0, y=50, w=5, color='black')
    GUIBasic.str_display(lmy, s="TKINTER", x=0, y=100, w=5, color='black')
    GUIBasic.str_display(lmy, s="HOU BING DE", x=0, y=150, w=5, color='black')
    GUIBasic.str_display(lmy, s="MOKEY FONT", x=0, y=200, w=5, color='black')
    GUIBasic.str_display(lmy, s="SNAKE 2", x=0, y=250, w=5, color='black')
    GUIBasic.str_display(lmy, s="MONKEYHBD", x=0, y=300, w=5, color='black')
    GUIBasic.str_display(lmy, s="0123456789", x=0, y=350, w=5, color='black')
    lmy.mainloop()
