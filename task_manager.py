from tkinter import *
import pickle

def add_task():
    task = task_entry.get()
    if task:
        task_manager.append(task)
        list_box.insert(END, task)
        task_entry.delete(0,END)

def remove():
    selected_item = list_box.curselection()
    for item in selected_item:
        list_box.delete(item)
        

def mark():
    selected_item = list_box.curselection()
    if selected_item:
        item = list_box.get(selected_item)
        if item.startswith("✅"):
            list_box.itemconfig(selected_item, fg ="black")
            list_box.delete(selected_item)
            list_box.insert(END, item[1:])

        else:
            list_box.itemconfig(selected_item, fg = "black")
            list_box.delete(selected_item)
            list_box.insert(END, "✅"+ item)

def save():
    with open('task_manager.pkl', 'wb') as f:
        pickle.dump(task_manager,f)

def load():
    try:
        with open('task_manager.pkl' ,'rb') as f:
            task_manager = pickle.loads(f.read())
    except FileNotFoundError:
        task_manager= []


    list_box.delete(0,END)
    for item in task_manager:
        list_box.insert(END, item)




app= Tk()
app.title("Task Manager")
app.geometry("720x480")
app.resizable(False,False)
app.config(bg="#242424")
task_manager= []

title = Label(app, text="Task Manager", font=("Consolas",18),bg="#242424", fg="#fff")
title.pack()

title = StringVar()
task_entry = Entry(app, width=34, textvariable= Text, font=("Consolas",12))
task_entry.pack()

add = Button(app, text="Add", width=5, font=("Consolas",12),command= add_task)
add.place(x=205, y= 110)

remove = Button(app, text="Remove", width=6, font=("Consolas",12),command= remove)
remove.place(x=450, y= 110)

mark = Button(app, text="Mark", width=12, font=("Consolas",12),command= mark)
mark.place(x=300, y= 130)

save = Button(app, text="Save", width=5, font=("Consolas",12), command= save)
save.place(x=205, y= 150)

load = Button(app, text="Load", width=5, font=("Consolas",12), command= load)
load.place(x=450, y= 150)

list_box = Listbox(app, height=15, width=45, font=("Consolas",12))
list_box.place(x= 170, y= 200)

app.mainloop()