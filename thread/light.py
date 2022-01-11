import _tkinter
import threading
import time
import random
import tkinter

from data import theme as DataTheme


class Flash(threading.Thread):
    def __init__(self, lights: list[tkinter.Label]):
        threading.Thread.__init__(self)
        self.lights = lights

    def run(self):
        colors = DataTheme.light_colors
        num_of_color = len(colors)

        while True:
            try:
                for light in self.lights:
                    light['bg'] = colors[random.randint(0, num_of_color - 1)]
                time.sleep(1)
            except _tkinter.TclError:
                break


def light_thread_create(light_obj_list):
    colors = DataTheme.light_colors
    num_of_color = len(colors)

    def md():
        while True:
            try:
                for light in light_obj_list:
                    light['bg'] = colors[random.randint(0, num_of_color - 1)]
                time.sleep(1)
            except _tkinter.TclError:
                break

    light_thread = threading.Thread()
    light_thread.run = md
    light_thread.setDaemon(True)
    light_thread.start()
