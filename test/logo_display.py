import tkinter

import module.graphic.logo as GUILogo
import module.parameter.color as ParameterColor

W = 20


if __name__ == '__main__':
    lmy = tkinter.Tk()
    lmy.geometry('800x400')

    logo_display_canvas = tkinter.Canvas(lmy, bg='white')
    logo_display_canvas.place(x=0, y=0, width=38 * W, height=6 * W)
    GUILogo.logo_display(logo_display_canvas, 0, 0, W, ParameterColor.mokey_logo_colors)

    logo_flash_canvas = tkinter.Canvas(lmy, bg='white')
    logo_flash_canvas.place(x=0, y=7 * W, width=38 * W, height=6 * W)
    GUILogo.logo_flash(logo_flash_canvas, 0, 0, W, ParameterColor.mokey_logo_colors, 0.03)

    lmy.mainloop()
