import tkinter

import module.graphic.basic as GUIBasic
import module.graphic.page as GUIPage

W = GUIBasic.W


if __name__ == '__main__':
    lmy = tkinter.Tk()
    lmy.title('贪吃蛇')
    lmy.geometry('1260x660')
    lmy.current_page = None
    lmy.update()
    GUIPage.welcome_page(lmy)
    lmy.mainloop()
