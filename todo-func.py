def show_menu():
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Complete Task")
    print("5. Exit")
    choice = input("Choose an option (1-5): ")
    return choice

def add_task(task_list):
    task = input("Enter the task to add: ")
    task_list.append(task)
    print(f'Task "{task}" added.')

def view_tasks(task_list):
    if not task_list:
        print("No tasks in the list.")
    else:
        for task in task_list:
            print(f'- {task}')

def remove_task(task_list):
    if not task_list:
        print("No tasks to remove.")
    else:
        view_tasks(task_list)
        found = False
        task_to_delete = input("Enter the task to delete: ").lower()
        for task in task_list:
            if task.lower() == task_to_delete:
                task_list.remove(task)
                print(f'Task "{task}" deleted.')
                found = True
                break
        if not found:
            print(f'Task "{task_to_delete}" not found.')

def complete_task(task_list):
    if not task_list:
        print("No tasks to remove.")
    else:
        view_tasks(task_list)
        found = False
        task_to_complete = input("Enter the task to complete: ").lower()
        for task in task_list:
            if task.lower() == task_to_complete:
                task_list.remove(task)
                print(f'Task "{task}" completed.')
                found = True
                break
        if not found:
            print(f'Task "{task_to_complete}" not found.')

def main():
    print("To Do Application")
    user_tasks = []

    while True:
        user_choice = show_menu()

        if user_choice == '1':
            add_task(user_tasks)
        elif user_choice == '2':
            view_tasks(user_tasks)  
        elif user_choice == '3':
            remove_task(user_tasks)
        elif user_choice == '4':
            complete_task(user_tasks)
        elif user_choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()