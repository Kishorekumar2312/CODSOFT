import customtkinter as ctk 
from tkinter import messagebox
import datetime
import json
import os

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class TodoListApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Todo List App")
        self.geometry("500x600")
        self.tasks = []
        self.task_widgets = []
        self.data_file = "todo_data.json"
        self.create_widgets()
        self.load_tasks()

    def create_widgets(self):
        self.bg_canvas = ctk.CTkCanvas(self, highlightthickness=0)
        self.bg_canvas.pack(fill="both", expand=True)
        self.create_gradient(self.bg_canvas, 500, 600, ("#E4B10A", "#378DFD"))

        self.main_frame = ctk.CTkFrame(self, corner_radius=20, fg_color="white")
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.9)

        self.title_label = ctk.CTkLabel(self.main_frame, text="To do List", font=("Helvetica", 24, "bold"), text_color="#77B5F0")
        self.title_label.pack(pady=20)

        self.task_var = ctk.StringVar()
        self.task_entry = ctk.CTkEntry(self.main_frame, textvariable=self.task_var, font=("Helvetica", 16), width=300)
        self.task_entry.pack(pady=10)

        self.add_button = ctk.CTkButton(self.main_frame, text="Add Task", command=self.add_task, font=("Helvetica", 14), corner_radius=10, width=150)
        self.add_button.pack(pady=10)

        self.tasks_frame = ctk.CTkScrollableFrame(self.main_frame, width=380, height=250, fg_color="white", border_width=1, border_color="gray")
        self.tasks_frame.pack(pady=10)

        self.button_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.button_frame.pack(pady=10)

        self.complete_button = ctk.CTkButton(self.button_frame, text="Complete Task", command=self.complete_task, font=("Helvetica", 14), corner_radius=10, width=150)
        self.complete_button.grid(row=0, column=0, padx=5)

        self.remove_button = ctk.CTkButton(self.button_frame, text="Remove Completed", command=self.remove_completed, font=("Helvetica", 14), corner_radius=10, width=150)
        self.remove_button.grid(row=0, column=1, padx=5)

    def create_gradient(self, canvas, width, height, color):
        for i in range(height):
            ratio = i / height
            r = int((1 - ratio) * int(color[0][1:3], 16) + ratio * int(color[1][1:3], 16))
            g = int((1 - ratio) * int(color[0][3:5], 16) + ratio * int(color[1][3:5], 16))
            b = int((1 - ratio) * int(color[0][5:7], 16) + ratio * int(color[1][5:7], 16))
            color_code = f'#{r:02x}{g:02x}{b:02x}'
            canvas.create_line(0, i, width, i, fill=color_code)

    def add_task(self):
        task = self.task_var.get().strip()
        if task:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            task_with_time = f"{task} - {current_time}"
            checkbox = ctk.CTkCheckBox(self.tasks_frame, text=task_with_time, font=("Helvetica", 14))
            checkbox.pack(pady=5, padx=10, anchor="w")
            self.tasks.append({"task": task_with_time, "completed": False})
            self.task_widgets.append(checkbox)
            self.task_var.set("")
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def complete_task(self):
        completed_count = 0
        for task, widget in zip(self.tasks, self.task_widgets):
            if not task["completed"] and widget.get() == 1:
                task["completed"] = True
                widget.configure(text_color="green")
                widget.deselect()
                completed_count += 1

        if completed_count > 0:
            self.save_tasks()
            messagebox.showinfo("Info", f"{completed_count} task(s) marked as completed.")
        else:
            messagebox.showinfo("Info", "No uncompleted tasks selected.")

    def remove_completed(self):
        completed_tasks = [task for task, widget in zip(self.tasks, self.task_widgets) if widget.get() == 1]
        if completed_tasks:
            for task in completed_tasks:
                widget = self.task_widgets[self.tasks.index(task)]
                widget.destroy()
                self.task_widgets.remove(widget)
                self.tasks.remove(task)
            self.save_tasks()
        else:
            messagebox.showinfo("Info", "No tasks selected for removal.")

    def save_tasks(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.tasks, file)

    def load_tasks(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                self.tasks = json.load(file)

            for task in self.tasks:
                checkbox = ctk.CTkCheckBox(self.tasks_frame, text=task["task"], font=("Helvetica", 14))
                checkbox.pack(pady=5, padx=10, anchor="w")
                if task["completed"]:
                    checkbox.configure(text_color="green")
                self.task_widgets.append(checkbox)

    def on_closing(self):
        self.save_tasks()
        self.destroy()

if __name__ == "__main__":
    app = TodoListApp()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
