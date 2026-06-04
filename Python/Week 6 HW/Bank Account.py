class BankAccount :
    def __init__(self , owner , balance) :
        self.owner = owner
        self.balance = balance

    def deposit(self , amount) :
        self.balance += amount
        print("New balance :" , self.balance)

    def withdraw(self, amount) :
        self.balance -= amount
        print("New balance :" , self.balance)

    def show(self) :
        print(f"{self.owner} has {self.balance} SAR")

a = BankAccount("Reham", 1000)

a.deposit(500)
a.withdraw(300)
a.show()