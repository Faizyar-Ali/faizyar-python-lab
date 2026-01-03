import tkinter as tk
from pathlib import Path
from tkinter import ttk,messagebox
from tkinter import filedialog
import os


root=tk.Tk()
root.title("Garbage Files Remover")
root.geometry("400x400")
icon_path=os.path.join(os.path.dirname(__file__),"clean-code.ico")
if os.path.exists(icon_path):
         root.iconbitmap(icon_path)
else:
     print(f"⚠️ Icon File Not Found : {icon_path}")    
 
#=======variables==========
path_Var=tk.StringVar()
delete_exe=tk.BooleanVar(value=True)
delete_temp=tk.BooleanVar(value=True)

def browse():
    folder=filedialog.askdirectory()
    if folder:
        path_Var.set(folder)
    listbox.delete(0,tk.END)
    for file in Path(folder).iterdir():
         if file.is_file():
              if delete_exe.get() and file.suffix=='.exe':
                    listbox.insert(tk.END,file.name)
              if delete_exe.get() and file.name.startswith("tempCodeRunnerFile"):
                   listbox.insert(tk.END,file.name)
def del_file():
    folder=path_Var.get()
    if not folder:
        messagebox.showerror("Error","Please select a Folder First")
        return
    delete=0
    for file in Path(folder).iterdir():
        try:
            if delete_exe.get() and file.suffix=='.exe':
                    file.unlink()
                    delete+=1
            if delete_temp.get() and file.name.startswith("tempCodeRunnerFile"):
                 file.unlink()
                 delete+=1
        except Exception as e:
            return f"Error , Failed to delete : {file} : Error = {e}"
    messagebox.showinfo("Done",f"Deleted {file} files")

label=tk.Label(text="Delete Garbage Files",font=("Helvetica",15))
label.pack(pady=10)

entry=ttk.Entry(root,textvariable=path_Var)
entry.pack(pady=5)

button=ttk.Button(text="Browse",command=browse)
button.pack()

ttk.Checkbutton(root,text="Delete .exe files",variable=delete_exe).pack(anchor="w",padx=40,pady=5)
ttk.Checkbutton(root,text="Delete .tempcoderunner files",variable=delete_temp).pack(anchor="w",padx=40)

listbox=tk.Listbox(root,width=40,height=10)
listbox.pack(pady=5)
ttk.Button(root,text="Delete",command=del_file).pack(pady=20)
root.mainloop()