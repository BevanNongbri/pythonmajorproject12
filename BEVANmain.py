import json

# Define a Task class to represent each task
class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __repr__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"Title: {self.title}, Description: {self.description}, Category: {self.category}, Status: {status}"

# Function to save tasks to a JSON file
def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump([task.__dict__ for task in tasks], f)

# Function to load tasks from a JSON file
def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return [Task(**data) for data in json.load(f)]
    except FileNotFoundError:
        return []

# Function to add a task
def add_task(tasks):
    title = input("Enter the task title: ")
    description = input("Enter the task description: ")
    category = input("Enter the task category (Work/Personal/Urgent): ")
    tasks.append(Task(title, description, category))
    print("Task added successfully!")

# Function to view tasks
def view_tasks(tasks):
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks available.")

# Function to mark a task as completed
def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        tasks[task_index].mark_completed()
        print(f"Task '{tasks[task_index].title}' marked as completed!")
    except (IndexError, ValueError):
        print("Invalid task number. Please try again.")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task.title}' deleted!")
    except (IndexError, ValueError):
        print("Invalid task number. Please try again.")

# Main application loop
def main():
    tasks = load_tasks()
    
    while True:
        print("\n=== To-Do List Menu ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
