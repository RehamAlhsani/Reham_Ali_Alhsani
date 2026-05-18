Player1 = input("Enter Your choice : ")
Player2 = input("Enter Your choice : ")

if Player1 == Player2 :
    print("Tie")
else :
    if Player1 == "rock" :
        if Player2 == "scissors" :
            print("Player 1 wins")
        else :
            print("Player 2 wins")

    else :
        if Player1 == "paper" :
            if Player2 == "rock" :
                print("Player 1 wins")
            else :
                print("Player 2 wins")

        else :  
            if Player2 == "paper":
                print("Player 1 wins")
            else :
                print("Player 2 wins")