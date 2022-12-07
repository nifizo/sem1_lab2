import tkinter as tki
import sys
import os
from alarm_ui import AlarmUI


window = tki.Tk()

window.minsize(600, 395)
window.maxsize(600, 395)
window.title("Timer")

img = tki.PhotoImage(file='icons/mainicon.png')
window.tk.call('wm', 'iconphoto', window._w, img)

AlarmUI(window)

window.mainloop()
