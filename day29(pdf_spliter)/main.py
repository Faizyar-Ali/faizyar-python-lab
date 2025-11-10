import sys, os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pdf_devider import pdfspliter

root = tk.Tk()
root.title("Split Here")
root.config(bg="#3e3e3e")
root.geometry("690x470")

icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")
if os.path.exists(icon_path):
    root.iconbitmap(icon_path)
else:
    print("⚠️ Icon file not found:", icon_path)
style = ttk.Style(root)
style.theme_use("clam")

menu = tk.Menu(root)
root.config(menu=menu)

def fyle():
      fi=filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
      entry.delete(0,tk.END)
      entry.insert(0,fi)
def folder():
    folder = filedialog.askdirectory()
    entry2.delete(0,tk.END)
    entry2.insert(0,folder)

def split():
    input_path=entry.get().strip()
    output_path=entry2.get().strip()
    starting_index=spin_box.get().strip()
    ending_index=spin_box1.get().strip()    
    reply=pdfspliter(input_path,output_path,starting_index,ending_index)
    if "⚠️" in reply or "Invalid" in reply:
        label2.config(text=reply, foreground="red", font=("", 10, "bold"))
    else:
        label2.config(text=reply, foreground="#00ff00", font=("", 10, "bold"))

    label2.after(2500, lambda: label2.config(text=""))


style.configure("label.TLabel", background="#3e3e3e", foreground="#ffffff", font=("", 23), cursor="arrow", anchor="center")
label = ttk.Label(master=root, text="PDF Splitter🧾", style="label.TLabel")
label.configure(anchor="center")
label.place(x=232, y=13, width=230, height=48)

label2 = ttk.Label(master=root, text="", style="label.TLabel")
label2.place(x=260, y=350)

style.configure("entry.TEntry", fieldbackground="#fff", foreground="#000", font=("TkMenuFont", 13))

entry = ttk.Entry(master=root, style="entry.TEntry")
entry.place(x=250, y=165, width=135, height=25)

entry2 = ttk.Entry(master=root, style="entry.TEntry")
entry2.place(x=250, y=195, width=135, height=25)

spin_box = tk.Spinbox(root, from_=0, to=100, increment=1, bg="#fff", fg="#000")
spin_box.place(x=273, y=232, width=70, height=30)

spin_box1 = tk.Spinbox(root, from_=0, to=100, increment=1, bg="#fff", fg="#000")
spin_box1.place(x=363, y=232, width=70, height=30)


style.configure("button.TButton", background="#4a9e2c", foreground="#000", font=("Arial", 15, "bold"))
style.map("button.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button = ttk.Button(master=root, text="Split", style="button.TButton",command=split)
button.place(x=291, y=285, width=120, height=45)

style.configure("button1.TButton", background="#E4E2E2", foreground="#000", font=("Arial", 6, "bold"))
style.map("button1.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button1 = ttk.Button(master=root, text="Browse", style="button1.TButton",command=fyle)
button1.place(x=394, y=165, width=50, height=26)

button1 = ttk.Button(master=root, text="Save to", style="button1.TButton",command=folder)
button1.place(x=394, y=195, width=50, height=26)

root.bind("<Return>", lambda event: split())
root.mainloop()