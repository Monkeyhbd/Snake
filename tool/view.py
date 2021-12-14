import tkinter

christmas = [[19, 18, 'SaddleBrown'], [20, 18, 'SaddleBrown'], [21, 18, 'SaddleBrown'], [21, 17, 'SaddleBrown'],
             [20, 17, 'SaddleBrown'], [19, 17, 'SaddleBrown'], [19, 16, 'SaddleBrown'], [20, 16, 'SaddleBrown'],
             [21, 16, 'SaddleBrown'], [21, 15, 'SaddleBrown'], [20, 15, 'SaddleBrown'], [19, 15, 'SaddleBrown'],
             [19, 14, 'SaddleBrown'], [20, 14, 'SaddleBrown'], [21, 14, 'SaddleBrown'], [21, 13, 'SaddleBrown'],
             [20, 13, 'SaddleBrown'], [19, 13, 'SaddleBrown'], [15, 12, 'DarkGreen'], [16, 12, 'DarkGreen'],
             [17, 12, 'DarkGreen'], [18, 12, 'DarkGreen'], [19, 12, 'DarkGreen'], [20, 12, 'DarkGreen'],
             [21, 12, 'DarkGreen'], [22, 12, 'DarkGreen'], [23, 12, 'DarkGreen'], [24, 12, 'DarkGreen'],
             [25, 12, 'DarkGreen'], [24, 11, 'DarkGreen'], [23, 11, 'DarkGreen'], [22, 11, 'DarkGreen'],
             [21, 11, 'DarkGreen'], [20, 11, 'DarkGreen'], [19, 11, 'DarkGreen'], [18, 11, 'DarkGreen'],
             [17, 11, 'DarkGreen'], [16, 11, 'DarkGreen'], [17, 10, 'DarkGreen'], [18, 10, 'DarkGreen'],
             [19, 10, 'DarkGreen'], [20, 10, 'DarkGreen'], [21, 10, 'DarkGreen'], [22, 10, 'DarkGreen'],
             [23, 10, 'DarkGreen'], [24, 9, 'ForestGreen'], [23, 9, 'ForestGreen'], [22, 9, 'ForestGreen'],
             [21, 9, 'ForestGreen'], [20, 9, 'ForestGreen'], [19, 9, 'ForestGreen'], [18, 9, 'ForestGreen'],
             [17, 9, 'ForestGreen'], [16, 9, 'ForestGreen'], [17, 8, 'ForestGreen'], [18, 8, 'ForestGreen'],
             [19, 8, 'ForestGreen'], [20, 8, 'ForestGreen'], [21, 8, 'ForestGreen'], [22, 8, 'ForestGreen'],
             [23, 8, 'ForestGreen'], [22, 7, 'ForestGreen'], [21, 7, 'ForestGreen'], [20, 7, 'ForestGreen'],
             [19, 7, 'ForestGreen'], [18, 7, 'ForestGreen'], [17, 6, 'LimeGreen'], [18, 6, 'LimeGreen'],
             [19, 6, 'LimeGreen'], [20, 6, 'LimeGreen'], [21, 6, 'LimeGreen'], [22, 6, 'LimeGreen'],
             [23, 6, 'LimeGreen'], [22, 5, 'LimeGreen'], [21, 5, 'LimeGreen'], [20, 5, 'LimeGreen'],
             [19, 5, 'LimeGreen'], [18, 5, 'LimeGreen'], [19, 4, 'LimeGreen'], [20, 4, 'LimeGreen'],
             [21, 4, 'LimeGreen'], [22, 3, 'Lime'], [21, 3, 'Lime'], [20, 3, 'Lime'], [19, 3, 'Lime'],
             [18, 3, 'Lime'], [19, 2, 'Lime'], [20, 2, 'Lime'], [21, 2, 'Lime'], [20, 1, 'Lime'], [7, 3, 'Cyan'],
             [6, 4, 'Cyan'], [8, 5, 'Cyan'], [7, 6, 'Cyan'], [13, 1, 'Cyan'], [12, 2, 'Cyan'], [30, 1, 'Cyan'],
             [29, 2, 'Cyan'], [31, 4, 'Cyan'], [30, 5, 'Cyan'], [36, 2, 'Cyan'], [35, 3, 'Cyan'], [14, 4, 'Cyan'],
             [13, 5, 'Cyan'], [12, 7, 'Cyan'], [11, 8, 'Cyan'], [9, 8, 'Cyan'], [8, 9, 'Cyan'], [4, 2, 'Cyan'],
             [3, 3, 'Cyan'], [4, 4, 'Cyan'], [3, 5, 'Cyan'], [30, 8, 'Cyan'], [29, 9, 'Cyan'], [28, 6, 'Cyan'],
             [27, 7, 'Cyan'], [35, 7, 'Cyan'], [34, 8, 'Cyan'], [2, 8, 'Cyan'], [1, 9, 'Cyan'], [38, 4, 'Cyan'],
             [37, 5, 'Cyan'], [33, 6, 'Cyan'], [34, 5, 'Cyan'], [26, 3, 'Cyan'], [25, 4, 'Cyan'], [25, 0, 'Cyan'],
             [24, 1, 'Cyan'], [8, 1, 'Cyan'], [9, 0, 'Cyan'], [1, 2, 'Cyan'], [2, 1, 'Cyan'], [0, 6, 'Cyan'],
             [1, 5, 'Cyan'], [5, 8, 'Cyan'], [4, 9, 'Cyan'], [10, 5, 'Cyan'], [11, 4, 'Cyan'], [31, 11, 'Cyan'],
             [32, 10, 'Cyan'], [35, 11, 'Cyan'], [11, 10, 'Cyan'], [10, 11, 'Cyan'], [6, 10, 'Cyan'], [5, 11, 'Cyan'],
             [0, 12, 'Cyan'], [1, 11, 'Cyan'], [36, 10, 'Cyan'], [38, 9, 'Cyan'], [39, 8, 'Cyan'],
             [0, 19, 'OliveDrab'], [1, 19, 'OliveDrab'], [2, 19, 'OliveDrab'], [3, 19, 'OliveDrab'],
             [4, 19, 'OliveDrab'], [5, 19, 'OliveDrab'], [6, 19, 'OliveDrab'], [7, 19, 'OliveDrab'],
             [8, 19, 'OliveDrab'], [9, 19, 'OliveDrab'], [10, 19, 'OliveDrab'], [11, 19, 'OliveDrab'],
             [12, 19, 'OliveDrab'], [13, 19, 'OliveDrab'], [14, 19, 'OliveDrab'], [15, 19, 'OliveDrab'],
             [16, 19, 'OliveDrab'], [17, 19, 'OliveDrab'], [18, 19, 'OliveDrab'], [19, 19, 'OliveDrab'],
             [20, 19, 'OliveDrab'], [21, 19, 'OliveDrab'], [22, 19, 'OliveDrab'], [23, 19, 'OliveDrab'],
             [24, 19, 'OliveDrab'], [25, 19, 'OliveDrab'], [26, 19, 'OliveDrab'], [27, 19, 'OliveDrab'],
             [28, 19, 'OliveDrab'], [29, 19, 'OliveDrab'], [30, 19, 'OliveDrab'], [31, 19, 'OliveDrab'],
             [32, 19, 'OliveDrab'], [33, 19, 'OliveDrab'], [34, 19, 'OliveDrab'], [35, 19, 'OliveDrab'],
             [36, 19, 'OliveDrab'], [37, 19, 'OliveDrab'], [38, 19, 'OliveDrab'], [39, 19, 'OliveDrab'],
             [7, 17, 'SaddleBrown'], [7, 18, 'SaddleBrown'], [6, 14, 'DarkGreen'], [6, 13, 'DarkGreen'],
             [7, 13, 'DarkGreen'], [8, 13, 'DarkGreen'], [7, 12, 'DarkGreen'], [7, 14, 'ForestGreen'],
             [7, 15, 'ForestGreen'], [7, 16, 'SaddleBrown'], [8, 14, 'DarkGreen'], [8, 15, 'DarkGreen'],
             [6, 15, 'DarkGreen'], [9, 14, 'DarkGreen'], [5, 14, 'DarkGreen'], [39, 15, 'red'], [39, 16, 'red'],
             [39, 17, 'red'], [39, 18, 'red'], [38, 18, 'red'], [37, 18, 'red'], [36, 18, 'red'], [35, 18, 'red'],
             [34, 18, 'red'], [34, 17, 'red'], [33, 17, 'red'], [32, 17, 'red'], [31, 17, 'red'], [30, 17, 'red'],
             [29, 17, 'black'], [23, 17, 'blue'], [23, 18, 'blue'], [25, 18, 'blue'], [25, 17, 'blue'],
             [24, 17, 'blue'], [24, 16, 'DeepPink'], [24, 18, 'blue'], [23, 15, 'HotPink'], [25, 15, 'HotPink'],
             [13, 17, 'BlueViolet'], [13, 18, 'BlueViolet'], [14, 18, 'BlueViolet'], [14, 17, 'BlueViolet'],
             [12, 17, 'BlueViolet'], [12, 18, 'BlueViolet'], [15, 18, 'BlueViolet'], [15, 17, 'BlueViolet'],
             [15, 16, 'BlueViolet'], [14, 16, 'BlueViolet'], [13, 16, 'BlueViolet'], [12, 16, 'BlueViolet'],
             [13, 15, 'Crimson'], [14, 15, 'Crimson'], [12, 14, 'HotPink'], [15, 14, 'HotPink']]

christmas_tree = [[4, 17, 'SaddleBrown'], [5, 17, 'SaddleBrown'], [6, 17, 'SaddleBrown'], [6, 16, 'SaddleBrown'],
                  [5, 16, 'SaddleBrown'], [4, 16, 'SaddleBrown'], [4, 15, 'SaddleBrown'], [5, 15, 'SaddleBrown'],
                  [6, 15, 'SaddleBrown'], [6, 14, 'SaddleBrown'], [5, 14, 'SaddleBrown'], [4, 14, 'SaddleBrown'],
                  [4, 13, 'SaddleBrown'], [5, 13, 'SaddleBrown'], [6, 13, 'SaddleBrown'], [6, 12, 'SaddleBrown'],
                  [5, 12, 'SaddleBrown'], [4, 12, 'SaddleBrown'], [0, 11, 'DarkGreen'], [1, 11, 'DarkGreen'],
                  [2, 11, 'DarkGreen'], [3, 11, 'DarkGreen'], [4, 11, 'DarkGreen'], [5, 11, 'DarkGreen'],
                  [6, 11, 'DarkGreen'], [7, 11, 'DarkGreen'], [8, 11, 'DarkGreen'], [9, 11, 'DarkGreen'],
                  [10, 11, 'DarkGreen'], [9, 10, 'DarkGreen'], [8, 10, 'DarkGreen'], [7, 10, 'DarkGreen'],
                  [6, 10, 'DarkGreen'], [5, 10, 'DarkGreen'], [4, 10, 'DarkGreen'], [3, 10, 'DarkGreen'],
                  [2, 10, 'DarkGreen'], [1, 10, 'DarkGreen'], [2, 9, 'DarkGreen'], [3, 9, 'DarkGreen'],
                  [4, 9, 'DarkGreen'], [5, 9, 'DarkGreen'], [6, 9, 'DarkGreen'], [7, 9, 'DarkGreen'],
                  [8, 9, 'DarkGreen'], [9, 8, 'ForestGreen'], [8, 8, 'ForestGreen'], [7, 8, 'ForestGreen'],
                  [6, 8, 'ForestGreen'], [5, 8, 'ForestGreen'], [4, 8, 'ForestGreen'], [3, 8, 'ForestGreen'],
                  [2, 8, 'ForestGreen'], [1, 8, 'ForestGreen'], [2, 7, 'ForestGreen'], [3, 7, 'ForestGreen'],
                  [4, 7, 'ForestGreen'], [5, 7, 'ForestGreen'], [6, 7, 'ForestGreen'], [7, 7, 'ForestGreen'],
                  [8, 7, 'ForestGreen'], [7, 6, 'ForestGreen'], [6, 6, 'ForestGreen'], [5, 6, 'ForestGreen'],
                  [4, 6, 'ForestGreen'], [3, 6, 'ForestGreen'], [2, 5, 'LimeGreen'], [3, 5, 'LimeGreen'],
                  [4, 5, 'LimeGreen'], [5, 5, 'LimeGreen'], [6, 5, 'LimeGreen'], [7, 5, 'LimeGreen'],
                  [8, 5, 'LimeGreen'], [7, 4, 'LimeGreen'], [6, 4, 'LimeGreen'], [5, 4, 'LimeGreen'],
                  [4, 4, 'LimeGreen'], [3, 4, 'LimeGreen'], [4, 3, 'LimeGreen'], [5, 3, 'LimeGreen'],
                  [6, 3, 'LimeGreen'], [3, 2, 'Lime'], [4, 2, 'Lime'], [5, 2, 'Lime'], [6, 2, 'Lime'],
                  [7, 2, 'Lime'], [6, 1, 'Lime'], [5, 1, 'Lime'], [4, 1, 'Lime'], [5, 0, 'Lime']]


class Application(tkinter.Tk):
    def __init__(self, title, data, w):
        tkinter.Tk.__init__(self)
        self.title('Mokey View - ' + title)
        self.geometry('400x400')
        self.data = data
        self.w = w
        self.stage = None

    def display(self):
        self.stage = tkinter.Canvas(self)
        w = self.w
        max_x, max_y = 0, 0
        for unit in self.data:
            if unit[0] > max_x:
                max_x = unit[0]
            if unit[1] > max_y:
                max_y = unit[1]
            tkinter.Label(self.stage, bg=unit[2]).place(x=unit[0] * w, y=unit[1] * w, width=w, height=w)
        self.stage.place(x=0, y=0, width=(max_x+1) * w, height=(max_y+1) * w)
        self.geometry('{}x{}'.format((max_x+1) * w, (max_y+1) * w))


if __name__ == '__main__':
    lmy = Application('Christmas', christmas, 20)
    lmy.display()
    lmy2 = Application('Christmas Tree', christmas_tree, 20)
    lmy2.display()
    lmy.mainloop()
    lmy2.mainloop()
