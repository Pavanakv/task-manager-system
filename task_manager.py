from task_operations import load_task, save_task, add_task, remove_task, view_task

def main():
    tasks = load_task()
    while True:
        print("\n1.Add Task \n2.Remove Task \n3.view Task \n4.Exit ")
    
        choice=input("Enter the choice:")

        if choice=='1':
            task=input("Enter the task:")
            add_task(tasks,task)
            save_task(tasks)

        elif choice == '2':
            task = input("Enter the task to remove: ")
            remove_task(tasks, task)
            save_task(tasks)

        elif choice == '3':
            view_task(tasks)

        elif choice == '4':
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")
        
main()        