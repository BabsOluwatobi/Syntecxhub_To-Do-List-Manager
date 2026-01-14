import json
import os

FILE_NAME = "My_tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    print(" Task added successfully.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Not Done"
        print(f"{index}. {task['title']} - {status}")

def mark_task_done(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to mark as done: "))
        tasks[task_num - 1]["completed"] = True
        save_tasks(tasks)
        print(" Task marked as completed.")
    except (ValueError, IndexError):
        print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: "))
        removed = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f"🗑 Task '{removed['title']}' deleted.")
    except (ValueError, IndexError):
        print("Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST MANAGER ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye ")
            break
        else:
            print("Invalid option. Try again.")

main()
