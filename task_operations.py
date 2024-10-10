def load_task():
    tasks=[]
    try:
        with open('task.txt','r') as file:
            tasks=[line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("No file found!! starting with an empty list file")
    return tasks    

def save_task(tasks):
    with open('task.txt','w') as file:
        for task in tasks:
            file.write(task + '\n')

def add_task(tasks,task):
    tasks.append(task)
    print(f"task {task} added successfully!!")

def remove_task(tasks,task):
    try:
        tasks.remove(task)
        print(f"task{task} removes successfully!!")
    except ValueError:
        print("task not found!!")

def view_task(tasks):
    if not tasks: 
        print("task not found!!")
    else:
        print(tasks)    
                           
