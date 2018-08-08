import tkinter as tk
from tkinter import simpledialog
from speedJenga import SpeedJenga
# import keyboard

def playSpeedJenga():
    # tk.messagebox.showinfo("Instructions", "Press the white button once for each player in the game. After that, press the green button to start the game. Press the red button to cancel")
    game = SpeedJenga()
    while True:
        continue


root = tk.Tk()
b = tk.Button(root, text="Play Speed Jenga", command = playSpeedJenga)

b.pack()
b.mainloop()
