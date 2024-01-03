import os
import json

class ToDoList:
    def __init__(self, filename='todo_list.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        else:
            return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=2)

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{task}' added successfully.")

    def remove_task(self, task_index):
        try:
            task_index = int(task_index)
            if 1 <= task_index <= len(self.tasks):
                removed_task = self.tasks.pop(task_index - 1)
                self.save_tasks()
                print(f"Task '{removed_task}' removed successfully.")
            else:
                print("Invalid task index.")
        except ValueError:
            print("Invalid input. Please enter a valid task index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            new_task = input("Enter the task: ")
            todo_list.add_task(new_task)
        elif choice == '3':
            task_index = input("Enter the task index to remove: ")
            todo_list.remove_task(task_index)
        elif choice == '4':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
