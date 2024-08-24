import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        # Create a frame for the listbox and scrollbar
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(frame, width=50, height=10, bd=0, font=('arial', 12))
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        # Scrollbar for the listbox
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)

        # Entry box to add new tasks
        self.task_entry = tk.Entry(self.root, width=52)
        self.task_entry.pack(pady=10)

        # Button frame for the action buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        # Add Task button
        add_button = tk.Button(button_frame, text="Add Task", command=self.add_task)
        add_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Remove Task button
        remove_button = tk.Button(button_frame, text="Remove Task", command=self.remove_task)
        remove_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Update Task button
        update_button = tk.Button(button_frame, text="Update Task", command=self.update_task)
        update_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Mark as Done button
        mark_done_button = tk.Button(button_frame, text="Mark as Done", command=self.mark_as_done)
        mark_done_button.pack(side=tk.LEFT, padx=5, pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.task_listbox.delete(selected_task_index)
        else:
            messagebox.showwarning("Warning", "You must select a task to remove.")

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.task_entry.get()
            if task:
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, task)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a task to update.")
        else:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def mark_as_done(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.task_listbox.get(selected_task_index)
            self.task_listbox.delete(selected_task_index)
            self.task_listbox.insert(tk.END, task + " (Done)")
        else:
            messagebox.showwarning("Warning", "You must select a task to mark as done.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
