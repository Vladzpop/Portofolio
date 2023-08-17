class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added:", task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    def complete_task(self, task_num):
        if 1 <= task_num <= len(self.tasks):
            completed_task = self.tasks.pop(task_num - 1)
            print("Completed task:", completed_task)
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Quit")

        choice = input("Select an option (1/2/3/4): ")

        if choice == "1":
            task = input("Enter a task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            todo_list.view_tasks()
            task_num = int(input("Enter the task number to mark as completed: "))
            todo_list.complete_task(task_num)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
