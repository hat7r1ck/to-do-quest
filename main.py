import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.root.configure(bg="#1e1e1e")  # Set background color

        self.tasks = []

        self.task_entry = tk.Entry(root, font=("Helvetica", 14), bg="#2e2e2e", fg="white")
        self.task_entry.pack(pady=10)
        self.task_entry.bind("<Return>", self.add_task)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, font=("Helvetica", 12), bg="#428bca", fg="white")
        self.add_button.pack(pady=5)

        self.task_list = tk.Listbox(root, height=10, width=50, font=("Helvetica", 12), bg="#2e2e2e", fg="white")
        self.task_list.pack(pady=10)

        self.complete_button = tk.Button(root, text="Complete Task", command=self.complete_task, font=("Helvetica", 12), bg="#5cb85c", fg="white")
        self.complete_button.pack(pady=5)

        self.completed_tasks = []
        self.points = 0
        self.level = 1

        self.completed_tasks_label = tk.Label(root, text="Completed Tasks:", font=("Helvetica", 14), bg="#1e1e1e", fg="white")
        self.completed_tasks_label.pack()

        self.completed_tasks_list = tk.Listbox(root, height=5, width=50, font=("Helvetica", 12), bg="#2e2e2e", fg="white")
        self.completed_tasks_list.pack(pady=5)

        self.points_label = tk.Label(root, text=f"Points: {self.points}", font=("Helvetica", 14), bg="#1e1e1e", fg="white")
        self.points_label.pack()

        self.level_label = tk.Label(root, text=f"Level: {self.level}", font=("Helvetica", 14), bg="#1e1e1e", fg="white")
        self.level_label.pack()

        self.progress_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate", maximum=100)
        self.progress_bar.pack(pady=5)

        self.update_progress_bar()

    def add_task(self, event=None):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def complete_task(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.tasks[index]["completed"] = True
            self.completed_tasks.append(self.tasks[index]["task"])
            self.completed_tasks_list.insert(tk.END, self.tasks[index]["task"])
            self.update_points()
            self.update_level()
            self.update_progress_bar()
            self.task_list.delete(index)
            self.tasks.pop(index)

    def update_points(self):
        self.points += 10
        self.points_label.config(text=f"Points: {self.points}")

    def update_level(self):
        while self.points >= self.level * 50:
            self.points -= self.level * 50
            self.level += 1
            self.level_label.config(text=f"Level: {self.level}")
            self.progress_bar["value"] = 0  # Reset progress bar to zero

    def update_progress_bar(self):
        max_points = self.level * 50
        progress = min(100, (self.points / max_points) * 100)
        self.progress_bar["value"] = progress

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
