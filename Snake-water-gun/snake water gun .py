import random 

    


# snake=1
# water=2
# gun=3
while True:
    p=random.randint(1,3)
    guess=int(input("enter your choice  || 1  for snake|| 2 for water || 3 for gun  ::"))
            
            
    if guess==p:
        print("its a draw")
    elif guess==1 and p==2:
        print(" you win ")
    elif guess==2 and p==3:
        print("you win ")
    elif guess==3 and p==1:
        print("you win  ")
    elif p==1 and guess==2:
        print(" you lost ")
    elif p==2 and guess==3:
        print("you lost")
    elif p==3 and guess==1:
        print("you lost ")
    else:
        print("invaild syntax")

