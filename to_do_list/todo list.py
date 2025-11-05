to_do_list=[]
while True:
    print("Todolist Menu!")
    print("1.Add any work!")
    print("2.view any work!")
    print("3.delete any work!")
    print("4.exit") 
    choice=int(input("enter your choice : "))
    if choice==1:
            temp=input("enter the work you wanted to add :")
            to_do_list.append(temp)
            print("Added successfully!")
    elif choice==2:
        print("To_do List")
        for x,d in enumerate(to_do_list):
            print(f'{x+1}.{d}')
    elif choice==3:
        value_to_delete=int(input("Enter the index number to delete the task:  "))
        if value_to_delete>len(to_do_list):
            print("Invaid number")
        else:
            del to_do_list[value_to_delete-1]
            print("Task Deleted sucssfully")
    elif choice==4:
        print("Exiting from the todo list !")
        break
    else:
        print("Invaild choice!")
        print("please select between 1 to 4!")
            