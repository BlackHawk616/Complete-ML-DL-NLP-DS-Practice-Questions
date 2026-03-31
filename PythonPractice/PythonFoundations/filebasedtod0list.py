# #File-Based To-Do List
# Build a command-line to-do list application that allows users to add, view, and delete tasks, and stores all tasks in a file so they persist after the program exits.

def load_tasks(filename):
    try:
        with open(filename,'r') as file:
            tasks = [line.strip() for line in file.readlines()] # Traversing through each line in the file and stripping any leading/trailing whitespace characters, including the newline character.
    except FileNotFoundError:
        tasks = [] # Emppty list if the file does not exist
    return tasks

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + '\n') 

def add_task(filename):
    task = input("Enter a new task: ")
    tasks = load_tasks(filename)
    tasks.append(task)
    save_tasks(filename, tasks)
    print("Task added successfully!")

def view_tasks(filename):
    tasks = load_tasks(filename)
    if tasks:
        print("Your To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("Your To-Do List is empty.")

def delete_task(filename):
    tasks = load_tasks(filename)
    if tasks:
        view_tasks(filename)
        try:
            task_num = int(input("Enter the number of the task to delete : "))
            if 1<= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                save_tasks(filename, tasks)
                print(f"Task '{removed_task}' deleted successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    filename = "tasks.txt"
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_task(filename)
        elif choice == '2':
            view_tasks(filename)
        elif choice == '3':
            delete_task(filename)
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()