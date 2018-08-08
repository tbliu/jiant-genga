import tkinter as tk

def playSpeedJenga():
    tk.messagebox.showinfo("Instructions", "Press the white button once for each player in the game. After that, press the green button to start the game. Press the red button to cancel")


root = tk.Tk()
b = tk.Button(root, text="Play Speed Jenga", command = playSpeedJenga)

b.pack()
b.mainloop()
