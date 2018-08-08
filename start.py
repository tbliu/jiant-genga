import tkinter as tk
from tkinter import simpledialog
from speedJenga import SpeedJenga

root = tk.Tk()
frame = tk.Frame(root, width=768, height=576)
frame.pack()
speedJengaButton = tk.Button(frame, text= "Speed Jenga", font=("Helvetica", 18), height="30", width="30", command=lambda: SpeedJenga())
speedJengaButton.pack(side = tk.LEFT)

randomizedJengaButton = tk.Button(frame, text = "Randomized Speed Jenga", font=("Helvetica", 18), height="30", width="30")
randomizedJengaButton.pack(side = tk.RIGHT)
tk.mainloop()
