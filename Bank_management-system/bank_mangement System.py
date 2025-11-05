class Bank_account:
    def __init__(self,acc_number,holder_name,balance):
        self.acc_number=acc_number
        self.holder_name=holder_name
        self.balance=balance
        
    def deposit(self,amount):
        if amount<0:
            print("invaild input")
        else:
            self.balance+=amount
            print(f"{amount} added successfully.Balance {self.balance}")
            
    def withdrawn(self,amount):
        if amount<0:
            print("invaild amount")
        elif amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount
            print(f"Withdrawn successfully .Balance {self.balance}")
    
    def account_info(self):
        print("Account information ____")
        print(f"Account number : {self.acc_number}")
        print(f"Account holder name : {self.holder_name}")
        print(f"Balance::  {self.balance}")
        
accont1=Bank_account(1234567544567,"Suman Hazra",5000)
accont1.account_info()
accont1.deposit(80000)
accont1.withdrawn(2000)
accont1.account_info()