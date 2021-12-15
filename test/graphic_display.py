import tkinter

import module.graphic.basic as GUIBasic
import module.data.graphic as DataGraphic


if __name__ == '__main__':
    lmy = tkinter.Tk()
    lmy.geometry('840x440')
    rtn = GUIBasic.graphic_display2(lmy, DataGraphic.christmas, 20, 20, 20)
    print(len(rtn), rtn)
    lmy.mainloop()
