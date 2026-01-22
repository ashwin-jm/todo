print("To Do List Application")

print("1. Add a task")
print("2. Delete a task")   
print("3. View tasks")
print("4. Complete a task")
print("5. Exit")

user_choice = input("Enter your choice (1-5): ")

user_tasks = []

if user_choice == '1':
    task = input("Enter the task to add: ")
    user_tasks.append(task)
    print(f'Task "{task}" added.')

elif user_choice == '2':    
    task = input("Enter the task to delete: ")
    if task in user_tasks:
        user_tasks.remove(task)
        print(f'Task "{task}" deleted.')
    else:
        print(f'Task "{task}" not found.')

elif user_choice == '3':
    if user_tasks:
        print("Your tasks:")
        for task in user_tasks:
            print(f'- {task}')
    else:
        print("No tasks found.")

elif user_choice == '4':
    task = input("Enter the task to complete: ")
    if task in user_tasks:
        user_tasks.remove(task)
        print(f'Task "{task}" completed.')
    else:
        print(f'Task "{task}" not found.')

elif user_choice == '5':
    print("Exiting the application.")
