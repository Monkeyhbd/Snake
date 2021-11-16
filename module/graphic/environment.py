import ctypes
import tkinter

from . import basic as GUIBasic

try:
    # 告诉 Windows 使用程序自身的dpi适配
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except AttributeError:
    pass

window = tkinter.Tk()
window.title('贪吃蛇')

width = window.winfo_screenwidth()
height = window.winfo_screenheight()

if height >= 2160:
    W = 90
elif height >= 1440:
    W = 50
elif height >= 1080:
    W = 40
else:
    W = 30

GUIBasic.W = W

window.geometry('+20+20')
window.geometry(str(int(42*W)) + 'x' + str(int(22*W)))
window.current_page = None
window.update()
