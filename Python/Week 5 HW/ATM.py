Balance = 200

print(" 1- Check balance") 
print(" 2- Deposit 100 SAR") 
print(" 3- Withdraw 50 SAR") 
print(" 4- Exit")

Choice = int(input("Enter Number : "))

match Choice :
    case 1 :
        print("Current Balance : " , Balance )
    case 2 :
        Balance+= 100
        print("New balance : " , Balance  )

    case 3 :
        if Balance >= 50 :
            Balance -= 50
            print("New balance:", Balance , "SAR")
        else:
            print("Insufficient funds")
    case 4 :
        print("Goodbye!")
    case _ :
        print("Invalid choice")