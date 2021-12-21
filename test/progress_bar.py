import tkinter

import module.graphic.progressBar as GUIProgressBar


if __name__ == '__main__':
    lmy = tkinter.Tk()
    lmy.geometry('400x400')
    progress_bar = GUIProgressBar.ProgressBar(lmy, x=20, y=20, width=200, height=20,
                                              color_sum='white', color_act='red')
    progress_bar.display()
    progress_bar.update(0.8)
    lmy.mainloop()
