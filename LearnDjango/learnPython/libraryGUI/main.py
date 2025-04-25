# GUI graphical user interface

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# INIT
window = tk.Tk()
window.configure(bg = "black")
window.geometry("300x200")
window.resizable(False,False)
window.title("Percobaan GUI Python")

# Variable dan fungsi
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

def btnClick():
    print(NAMA_BELAKANG.get())
    pesan = f"Hallo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, Pintar"
    showinfo(title="Coba", message=pesan)

# frame input
inputFrame = ttk.Frame(window)
# penempatan grid, pack, place
# pack mengurut dari atas ke bawah
inputFrame.pack(padx=10,pady=10,fill="x",expand=True)

# komponen-komponen
# 1. label nama depan
firstName = ttk.Label(inputFrame, text="First Name:")
firstName.pack(fill="x",expand=True)
# 2. Entry nama depan
firstNameEntry = ttk.Entry(inputFrame,textvariable=NAMA_DEPAN)
firstNameEntry.pack(fill="x",expand=True)

# nama belakang
lastName = ttk.Label(inputFrame, text="Last Name :")
lastName.pack(fill="x",expand=True)
# entry nama belakang
lastNameEntry = ttk.Entry(inputFrame,textvariable=NAMA_BELAKANG)
lastNameEntry.pack(fill="x",expand=True)

# button
submitButton = ttk.Button(inputFrame, text = "submit", command=btnClick)
submitButton.pack(padx=10,pady=10,fill="x",expand=True)

window.mainloop()