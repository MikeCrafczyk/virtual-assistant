import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox, Label, Button

# import load
# import seting
# import pyttsx3
# import AI_pdf_word_txt


# Główne okno
root = tk.Tk()
root.title("Wirtualny Asystent")
root.geometry("800x600")
root.config(background="dark green")


# Funkcja otwierająca nowe okno
def openNewWindow():
    newWindow = tk.Toplevel(root)
    newWindow.title("Ustawienia")
    newWindow.geometry("400x300")
    Label(newWindow, text="Ustawienia").pack()


# Funkcja wysyłania wiadomości
def send_message():
    message = message_entry.get()
    if message:
        message_history.config(state=tk.NORMAL)
        message_history.insert(tk.END, f"You: {message}\n")
        message_history.config(state=tk.DISABLED)
        message_entry.delete(0, tk.END)


# Lista modeli
choices = ["model 1", "model 2", "model 3", "model 4"]
mlist_label = tk.Label(root, text="Lista modeli")
mlist_dropdown = Combobox(root, values=choices)

# Przycisk "ładowanie"
btn1 = Button(root, text="ładowanie")

# Przycisk "tryby"
btn2 = Button(root, text="tryby")

# Przycisk "ustawienia"
btn3 = Button(root, text="seting", command=openNewWindow)

# Przycisk "exit"
btn4 = Button(root, text="exit", command=root.quit)

# Historia wiadomości
message_history = tk.Text(root, wrap=tk.WORD, width=60, height=20)
message_history.config(state=tk.DISABLED)

# Pole wprowadzania wiadomości
message_entry = tk.Entry(root, width=50)

# Przycisk wysyłania
send_button = tk.Button(root, text="Send", command=send_message)

# Pozycjonowanie elementów
mlist_label.place(x=10, y=10)
mlist_dropdown.place(x=10, y=40)
btn1.place(x=10, y=80, height=30, width=100)
btn2.place(x=10, y=120, height=30, width=100)
btn3.place(x=10, y=160, height=30, width=100)
btn4.place(x=10, y=200, height=30, width=100)

# Pozycjonowanie elementów czatu
message_history.place(x=200, y=10, width=580, height=450)
message_entry.place(x=200, y=470, width=500, height=30)
send_button.place(x=710, y=470, height=30, width=70)

# Rozpoczęcie pętli głównej
root.mainloop()
