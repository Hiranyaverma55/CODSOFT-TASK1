import tkinter as tk
from tkinter import messagebox

class TodoList:
    
    def __init__(List, root):
        List.root = root
        List.root.title("To-Do List")

           
        List.frame = tk.Frame(root, bg='#7C00FE')
        List.frame.pack(pady=30, padx=30)

       
        List.task_entry = tk.Entry(List.frame, width=50, fg='#021526',bg='#D1E9F6', font=('Times New Roman', 12))
        List.task_entry.pack(pady=20)

        
        List.add_button = tk.Button(List.frame, text="Add Task", command=List.add_task, bg='#F57D1F', fg='#ffffff', font=('Times New Roman', 12))
        List.add_button.pack(pady=20)

        

        List.update_button = tk.Button(List.frame, text="Update Task", command=List.update_task, bg='#C63C51', fg='#ffffff', font=('Times New Roman', 12))
        List.update_button.pack(pady=20)
       

        List.delete_button = tk.Button(List.frame, text="Delete Task", command=List.delete_task, bg='#6EACDA', fg='#ffffff', font=('Times New Roman', 12))
        List.delete_button.pack(pady=20)
        

        List.tasks_listbox = tk.Listbox(List.frame, width=50, height=10, bg='#ffffff', fg='#000000', font=('Arial', 12))
        List.tasks_listbox.pack(pady=20)
        
    def add_task(List):
        task = List.task_entry.get()
        if task:
            List.tasks_listbox.insert(tk.END, task)
            List.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Enter a task")

    def update_task(List):
        selected_task_index = List.tasks_listbox.curselection()
        if selected_task_index:
            new_task = List.task_entry.get()
            if new_task:
                List.tasks_listbox.delete(selected_task_index)
                List.tasks_listbox.insert(selected_task_index, new_task)
                List.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Enter a task")
        else:
            messagebox.showwarning("Warning", "Select a task to update")

    def delete_task(List):
        selected_task_index = List.tasks_listbox.curselection()
        if selected_task_index:
            List.tasks_listbox.delete(selected_task_index)
        else:
            messagebox.showwarning("Warning", "Select a task to delete")



if __name__ == "__main__":
    root = tk.Tk()
    app = TodoList(root)
    root.mainloop()



