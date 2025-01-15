def display_menu():
    print("\nTo-Do List Options:")
    print("1. View To-Do List")
    print("2. Add Task.")
    print("3. Remove Task.")
    print("4. Mark Task as Done.")
    print("5. Exit.")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for idx, (task, done) in enumerate(tasks, 1):
            status = "Done" if done else "Not Done"
            print(f"{idx}. {task} [{status}]")

def add_task(tasks):
    task = input("\nEnter the task: ")
    tasks.append((task, False))
    print(f"Task '{task}' added to the list.")

def remove_task(tasks):
    try:
        view_tasks(tasks)
        task_number = int(input("\nEnter the number of the task to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task[0]}' removed from the list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_task_done(tasks):
    try:
        view_tasks(tasks)
        task_number = int(input("\nEnter the number of the task to mark as done: "))
        if 1 <= task_number <= len(tasks):
            task, _ = tasks[task_number - 1]
            tasks[task_number - 1] = (task, True)
            print(f"Task '{task}' marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            mark_task_done(tasks)
        elif choice == '5':
            print("Goodbye! Your tasks have been saved.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
