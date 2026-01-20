class Customer:
    def __init__(self,name,password,balance=0):
        self.name=name
        self.password=password
        self.balance=balance
        self.c_history=[]
    
    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} has deposited.\nNew balance:{self.balance}")
        self.c_history.append((f"{amount} has deposited."))

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"{amount} has withdrawed.\nNew balance:{self.balance}")
        else:
            print("insufficient funds")

    def showBalance(self):
        print(f"Balance:{self.balance}")

    def show_history(self):
        for i in self.c_history:
            print(i)

class Bank:
    def __init__(self):
        self.customers={}
    
    def add_customer(self,cid,name,pswrd):
        if cid in self.customers:
            print("already exists")
        else:
            self.customers[cid]=Customer(name,pswrd)
            print("The customer has been added.")

    def login(self,cid,pswrd):
        if cid not in self.customers:
            print("no account")
            return None
        else:
            if self.customers[cid].password==pswrd: 
                return self.customers[cid] #customer
            else:
                print("wrong password")
                return None
                
customers=Bank()

while 1:
    print("1: become a customer\n2: log in\n3: exit")
    choice=int(input("choice: "))

    if choice==1:
        cid=int(input("id: "))
        name=input("name: ")
        password=int(input("set password: "))
        customers.add_customer(cid,name,password)

    elif choice==2:
        cid=int(input("id: "))
        password=int(input("password: "))
        customer=customers.login(cid,password)
        while 1:
            choice=int(input("1: deposit money\n2: withdraw money\n3: show balance\n4: show history\n5: exit"))
        
            if choice==1:
                amount=int(input("enter quantity: "))
                customer.deposit(amount)
        
            elif choice==2:
                amount=int(input("enter quantity: "))
                customer.withdraw(amount)
        
            elif choice==3:
                customer.showBalance()
        
            elif choice==4:
                customer.show_history()
            
            elif choice==5:
                print("main menu")
                break
    elif choice==3:
        print("exit")
        break

