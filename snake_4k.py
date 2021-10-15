import tkinter
import ctypes

import module.graphic.basic as GUIBasic
GUIBasic.W = 90
import module.graphic.page as GUIPage

W = GUIBasic.W


# 告诉操作系统使用程序自身的dpi适配
ctypes.windll.shcore.SetProcessDpiAwareness(1)


if __name__ == '__main__':
    lmy = tkinter.Tk()
    lmy.title('贪吃蛇')
    lmy.geometry("+20+20")
    lmy.geometry(str(int(42*W)) + 'x' + str(int(22*W)))  # 11: 21
    lmy.current_page = None
    lmy.update()
    GUIPage.welcome_page(lmy)
    lmy.mainloop()
