def task_load():
    try:
        with open("tasks_file.txt","r") as file:
            return [line.strip() for line in file.readlines()]
    except:
        return[]
def done_taskload():
    try:
        with open("done_task.txt","r") as file:
            return [line.strip() for line in file.readlines()]
        print("Task marks as done!!")
    except:
        return[]
def save_tasks(tasks):
    with open("tasks_file.txt","w") as file:
        for task in tasks:
            file.write(task+"\n")

def done_task(tasks_done):
        with open("done_task.txt","w") as file:
            for task in tasks_done:
                file.write(task+"\n")
                
def show_tasks(tasks,tasks_done):
    if not tasks:
        print("No task added yet!")
    else:
        print("work to do!!!")
        for index,task in enumerate(tasks):
            print(f"{index+1}.[  ] .{task}")
    if not tasks_done:
        print("No task done yet")
    else:    
        print("Congratulations you done this works!!")
        for index1,task1 in enumerate(tasks_done):
            print(f"{index1+1}.[\u2713] .{task1}")
            


def main():
        print("Welcome to do list!!")
        print("1.Add a Tasks!")
        print("2.Show Tasks!!")
        print("3.Mark as done!!")
        print("4.delete a Tasks!!")
        print("5.Exit")
        while True:
            tasks=task_load()
            task1=done_taskload()
            ch=int(input("enter your choice::"))
            if ch==1:
                task=input("Enter the Task::")
                tasks.append(task)
                save_tasks(tasks)
                
            elif ch==2:
                show_tasks(tasks,task1)
                
            elif ch==3:
                show_tasks(tasks,task1)
                i=int(input("Enter the task number you want to mark done:")) - 1
                for index,task in enumerate(tasks):
                    if 0 <= index < len(tasks):
                        if i == index:
                            tasks.pop(i)
                            save_tasks(tasks)
                            task1.insert(i,task)
                            done_task(task1)
                            break
                    else:
                        print("Invalid task number.")               
            elif ch == 4:
                show_tasks(tasks,task1)
                idx = int(input("Enter task number to delete: ")) - 1
                if 0 <= idx < len(tasks):
                    tasks.pop(idx)
                    save_tasks(tasks)
                else:
                    print("Invalid task number.")
            elif ch==5:
                print("existing the program")
                break
            else:
                print("Invalid option.")

if __name__ == "__main__":
    main()
