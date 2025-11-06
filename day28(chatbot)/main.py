import tkinter as tk
from tkinter import scrolledtext
from chat_model import chat
from image_model_backend import fetch_url
import threading
import requests
from datetime import datetime
from io import BytesIO
from PIL import Image, ImageTk
import sys
import json
import os   


#python -m day28_gui_chatbot.frontend.main

root=tk.Tk()
root.title("Gemini Chatbot")
root.geometry("600x500")
root.minsize(width=550, height=390)
tk.Label(root,text="👷🏽 Welcome to Chatgpt 🤖").pack(pady=10)
images = []
icon_path = os.path.join(os.path.dirname(__file__), "alien.ico")
if os.path.exists(icon_path):
    root.iconbitmap(icon_path)
else:
    print("⚠️ Icon file not found:", icon_path)
chat_area=scrolledtext.ScrolledText(root,wrap=tk.WORD,width=45,height=16 ,state='disable',font="Segoe")
chat_area.configure(bg="#252526", fg="white", insertbackground="white")
chat_area.pack()
root.configure(bg='#2e2e2e')

chat_area.tag_configure('user', justify='right', foreground='cyan')

entry_field=tk.Entry(root,width=60,highlightthickness=2,highlightcolor='black',bd=0)
entry_field.focus_set()
entry_field.pack(pady=5)

def save_history(subject,content):
    now=datetime.now()
    current = now.strftime("%Y-%m-%d %H:%M:%S")
    path=r"D:\faizyar-python-lab\chatbot\history.json"
    meta={
            "By": subject,
            "message":content,
            "On Time":current
        }
    if not os.path.exists(path) or os.stat(path).st_size==0:
        with open(path,"w") as f:
            json.dump([],f)
    print(subject,content,meta)

    with open(path,"r") as f:
           data=json.load(f)

    data.append(meta)

    with open(path,"w") as his:
           json.dump(data,his,indent=4)

def send_message():
    user_input=entry_field.get().strip()
    if not user_input:
        return
    chat_area.config(state='normal')
    chat_area.insert(tk.END,f"\n{user_input}👷🏽 \n",'user')
    save_history("User",user_input)
    chat_area.config(state='disable')
    chat_area.yview(tk.END)
    entry_field.delete(0,tk.END)
    entry_field.config(state='disabled')
    def backgroud_task():
          if user_input.startswith("img"):
             prompt=user_input[5:]
             ai_img= fetch_url(prompt)
             if ai_img.startswith("Error"):
                chat_area.config(state='normal')
                chat_area.insert(tk.END,f"🤖:{ai_img}\n")
                save_history("img_bot",ai_img)     
                chat_area.config(state='disable')
                entry_field.config(state='normal')
                return
             try:
                  print(ai_img)
                  response = requests.get(ai_img,timeout=10)
                  response.raise_for_status()
                  img_data = response.content
                  image = Image.open(BytesIO(img_data))
                  image = image.resize((300, 200))
                  tk_image = ImageTk.PhotoImage(image)
                  images.append(tk_image)
                  chat_area.config(state='normal')
                  chat_area.insert(tk.END,f"🤖: \n")
                  chat_area.image_create(tk.END,image=tk_image)
                  save_history("img_bot",ai_img)  
                  chat_area.insert(tk.END,"\n")
                  chat_area.config(state="disable")
                  chat_area.yview(tk.END)
                  entry_field.config(state='normal')

             except Exception as e:
                 chat_area.insert(tk.END,f"🤖: ❌ Error: {str(e)}")
                 entry_field.config(state='normal')
          else:
               ai_reply=chat(user_input)
               chat_area.config(state='normal')
               chat_area.insert(tk.END,f"🤖: {ai_reply}\n")
               save_history("chat_bot",ai_reply)     
               chat_area.config(state='disable')
               chat_area.yview(tk.END)
               entry_field.config(state='normal')
    threading.Thread(target=backgroud_task).start()

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)
tk.Label(root,text="Use ' img <prompt> for image generation'",bg="#2e2e2e", fg="white",justify="right").pack(pady=40,padx=30)

root.bind('<Return>', lambda event: send_message())

root.mainloop()

