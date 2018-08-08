import tkinter as tk
from tkinter import simpledialog
from speedJenga import SpeedJenga

def playSpeedJenga():
    game = SpeedJenga()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
speedJengaButton = tk.Button(frame, text= "Speed Jenga", fg="red", command=lambda: SpeedJenga())
speedJengaButton.pack(side = tk.LEFT)

randomizedJengaButton = tk.Button(frame, text = "Randomized Speed Jenga", fg="red")
randomizedJengaButton.pack(side = tk.RIGHT)
#playJenga()
tk.mainloop()
