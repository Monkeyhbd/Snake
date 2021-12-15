import tkinter

import module.graphic.basic as GUIBasic
import module.data.graphic as DataGraphic


if __name__ == '__main__':
    lmy = tkinter.Tk()
    lmy.geometry('840x440')
    GUIBasic.graphic_display(lmy, DataGraphic.christmas, 20, 20, 20)
    lmy.mainloop()
