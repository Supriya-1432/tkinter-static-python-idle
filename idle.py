import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename,askopenfilename
import subprocess
import os

filepath=''

def set_file_path(path):
    global filepath
    filepath=path

def open_file():
    path=askopenfilename(filetypes=[("Python files","*.py")])
    output.delete('1.0',tk.END)
    with open(path,'r') as file:
        code=file.read()
        input.delete("1.0",tk.END)
        input.insert("1.0",code)
        set_file_path(path)
    return

def save_file():
    if filepath=='':
        path=asksaveasfilename(filetypes=[("Python files","*.py")])
    else:
        path=filepath
    output.delete('1.0',tk.END)
    with open(path,'w') as file:
        code=input.get('1.0',tk.END)
        file.write(code)
        set_file_path(path)
    return

def run_file():
    if filepath=='':
        messagebox.showerror(title="Python IDLE",message="Save your code")
    else:
        command=f'python {filepath}'
        process=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        o,e=process.communicate()
        output.insert("1.0",o)
        output.insert("1.0",e)
        return



root=tk.Tk()

root.title("Python IDLE")
root.geometry("1280x720")
root.config(bg="#323846")
root.resizable(False,False)

input=tk.Text(root,font=('Arial',10))
input.place(x=180,y=0,width=680,height=720)

output=tk.Text(root,font=('Arial',10),bg="#323846",fg="lightgreen")
output.place(x=860,y=0,width=420,height=720)

buttono=tk.Button(root,text="Open a .py file",font=('Arial',10),command=open_file)
buttono.place(x=30,y=30)
buttons=tk.Button(root,text="Save a .py file",font=('Arial',10),command=save_file)
buttons.place(x=30,y=145)
buttonr=tk.Button(root,text="Run a .py file",font=('Arial',10),command=run_file)
buttonr.place(x=30,y=260)


root.mainloop()