import random as r

def generate_random():
    random=r.randint(1,100)
    attempts=0
    print("Lets Begin.....")
    
    while True:

        guess=int(input("Enter a number between 1 to 100::"))

        attempts=attempts+1
    
        if guess==random:
            print("Congratulation you won!!")
            print(f"You guessed it in {attempts} attempts.")
            save_attempt(attempts)
            break
        elif guess>100 or guess<0:
            print("please choose a number between 1 to 100")
        elif guess<random:
            print("Too Low!!!.Try Again...")
        elif guess>random:
            print("Too High!!.Try Again...")
            
def attempt_load():
    try:
        with open("attempt.txt","r") as file:
            return [line.strip() for line in file.readlines()]
    except:
        return[]
def save_attempt(attempts):
    attempts=str(attempts)
    with open("attempt.txt","a") as file:
        for attempt in attempts:
            file.write(attempt+"\n")
def show_attempts(attempts):
    if not attempts:
        print("No highest rank")
    else:
        print("highest >>>>")
        for index,attempt in enumerate(attempts):
            print(f"{index+1}.{attempt}")        
    
    
def main():
    while True:
        attempts=attempt_load()
        print("welcome to gussing game !!")
        print("-----Menu-----")
        print("1.Start the game!!")
        print("2.Show the attempet!!!")
        print("3.Exit")
        ch=int(input("Enter your choice :::"))
        if ch==1:
                attempts=0
                generate_random()
                
        elif ch==2:
                show_attempts(attempts)
        elif ch==3:
                print("Exiting the program")
                break
        else:
                print("Invaild choice !!")
                
            
if __name__=="__main__":
    main()