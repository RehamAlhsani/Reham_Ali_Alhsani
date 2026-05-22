Balance = 1000

while True :

    print(" 1- Show Balance")
    print(" 2- Deposit")
    print(" 3- Withdraw")
    print(" 0- Exit")

    Choice = int(input("Enter Number : "))

    # Exit
    if Choice == 0 :
        print("Thank you for using the ATM .")
        break

    # Show Balance
    if Choice == 1 :
        print(f"Current Balance : {Balance} SAR")

    # Deposit
    elif Choice == 2 :
        while True :
            print("Deposit Amounts : 50, 100, 200, 500")
            print("Press 0 to cancel")

            Deposit = int(input("Enter Number : "))

            if Deposit == 0 :
                break

            elif Deposit in [50, 100, 200, 500] :
                Balance += Deposit

                print(f"Deposited {Deposit} SAR")
                print(f"New Balance : {Balance} SAR")
                break

            else :
                print("Invalid amount . Try again .")

    # Withdraw
    elif Choice == 3 :
        while True :
            print("Withdraw Amounts : 50, 100, 200, 500")
            print("Press 0 to cancel")

            Withdraw = int(input("Enter Number : ")) 

            if Withdraw == 0 :
                break

            elif Withdraw in [50, 100, 200, 500] :
                if Balance >= Withdraw :
                    Balance -= Withdraw

                    print(f"Withdrawn {Withdraw} SAR")
                    print(f"New Balance : {Balance} SAR")
                    break
                else :
                    print("Insufficient funds")
                    break

            else :
                print("Invalid amount . Try again .")

    else :
        print("Invalid option . Please try again .")