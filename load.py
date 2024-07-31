from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import time
import tkinter as tk

root = Tk()

root.title("seting")
root.geometry("600x600")
# root.config(background="dark green")

# okno plików

# pasek przewijania


# okno postępu
""" def start_progress():
    progress.start()
    for i in range(101):
        time.sleep(0.05)
        progress["value"] = i
        root.update_idletasks()
    progress.stop()
 """

root = tk.Tk()
progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=20)

start_button = tk.Button(root, text="Start Progress", command=start_progress)
start_button.pack(pady=10)

root.mainloop()  # zapętlenia akji
