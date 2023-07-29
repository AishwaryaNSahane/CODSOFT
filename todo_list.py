import tkinter as tk

def add_task():
    task = entry.get()
    if task.strip() != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def edit_task():
    try:
        index = listbox.curselection()[0]
        selected_task = listbox.get(index)
        entry.delete(0, tk.END)
        entry.insert(tk.END, selected_task)
        delete_task()
    except IndexError:
        pass

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:
        pass

root = tk.Tk()



header = tk.Frame(root, bg="green", padx=350, pady=50)
header.pack(fill=tk.X)

header_label = tk.Label(header, text="ToDo List", font=("Comic Sans MS", 36), bg="green", fg="black")
header_label.pack()


add_frame = tk.Frame(root)
add_frame.pack(pady=10)

add_label = tk.Label(add_frame, text="Add Items", font=("Arial", 14))
add_label.pack(side=tk.TOP)

entry = tk.Entry(add_frame, width=80)
entry.pack(side=tk.LEFT)

submit_button = tk.Button(add_frame, text="Submit", command=add_task,bg="black", fg="white")
submit_button.pack(side=tk.LEFT, padx=10)


tasks_label = tk.Label(root, text="Tasks", font=("Arial", 14))
tasks_label.pack()


listbox = tk.Listbox(root, width=80, height=5, selectbackground="lightgray")
listbox.pack()



delete_button = tk.Button(root, text="Delete", command=delete_task, bg="red", fg="white")
delete_button.pack(side=tk.RIGHT, padx=10)

edit_button = tk.Button(root, text="Edit", command=edit_task, bg="green", fg="white")
edit_button.pack(side=tk.RIGHT, padx=10)



root.mainloop()