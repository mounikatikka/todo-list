
# todo_list.py

tasks = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks):
            status = "✔" if task['done'] else "✘"
            print(f"{idx + 1}. [{status}] {task['title']}")

def add_task():
    title = input("Enter task title: ")
    tasks.append({'title': title, 'done': False})
    print("Task added!")

def mark_done():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]['done'] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            deleted = tasks.pop(task_num)
            print(f"Deleted task: {deleted['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
