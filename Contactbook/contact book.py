class contacts:
    def __init__(self,name,number,email):
        self.name = name
        self.number = number
        self.email = email
    
    def __str__(self):
        return f"{self.name} || {self.number} || {self.email}"
    
class contactbook:
    def __init__(self):
        self.contactbook=[]
    def add_contact(self,name,number,email):
        Contacts=contacts(name,number,email)
        self.contactbook.append(Contacts)
        print("Contact Added Successfully ")
    def viewallcontacts(self):
        if not self.contactbook:
            print("No contact added yet")
        else:
            for contact in self.contactbook:
                print(contact)
    def deletecontact(self,name):
        for contact in self.contactbook:
            if contact.name.lower() == name.lower():
                self.contactbook.remove(contact)
                print("Contact deleted sucessfully!!")
            else :
                print("Contact not found !!!")
    def seacrch_contact(self,name):
        found=False
        for contact in self.contactbook:
            if contact.name.lower() == name.lower():
                print("Contact Found ")
                print(contact)
                found=True
                break
        if not found:
                print("Contact not found!!")


def main():
    book=contactbook()
    print("Welcome Contactbook!!")
    print("------Menu------")
    print("1.Add Contacts..")
    print("2.View all contacts....")
    print("3.Search Contacts...")
    print("4.Delete a contact...")
    print("5.Exit...")
    while True:
        ch=int(input("Enter your choice>>>"))
        if ch==1:
            while True:
                try:
                    name = input("Enter the Name :: ")
                    number = input("Enter the Contact Number :: ")
                    if not (number.isdigit() and len(number) == 10):
                        raise ValueError("Invalid number.")
                    email = input("Enter the Email id :: ")
                    if "@" not in email or "." not in email:
                        raise ValueError("Invalid email address.")
                    break 
                except ValueError as e:
                    print(f"Error: {e}. Please try again.")
            book.add_contact(name,number,email)
        elif ch==2:
            book.viewallcontacts()           
        elif ch==3:
            name=input("Enter the name you want to search :: ")
            book.seacrch_contact(name)
        elif ch==4:
            name=input("Enter the name you want to delete :: ")
            book.deletecontact(name)
        elif ch==5:
            print("Exiting from contact book")
            break
        
        else:
            print("Invaild choice . try again ")
            
if __name__=="__main__":
    main()