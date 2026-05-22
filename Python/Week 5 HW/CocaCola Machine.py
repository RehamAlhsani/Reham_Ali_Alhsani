Money = 50

while Money > 0 :
    try :
        Coin = int(input("Insert Coin : "))
    except ValueError :
        print("Please Insert a Valid Integer Coin")
        continue

    if Coin not in [5, 10, 25] :
        print(f"Coin Not Accepted . Returning {Coin} Cents")
        print(f"Amount Due : {Money}")
        continue

    Money -= Coin

    if Money > 0 :
        print(f"Amount Due : {Money}")

Change = abs(Money)
print(f"Change Owed : {Change}")