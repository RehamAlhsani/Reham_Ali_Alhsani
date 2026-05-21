Inventory = {"laptop": 5, "mouse": 10, "keyboard": 0}

Orders = [
    ("laptop", 2),
    ("mouse", 15),
    ("keyboard", 1),
    ("monitor", 3),
]

for Product , Quantity in Orders :
    match Product :
        case Prod if Prod not in Inventory :
            print(f"{Prod} : not in inventory")

        case Prod if Inventory[Prod] >= Quantity :
            Inventory[Prod] -= Quantity
            print(f"{Prod} : shipped {Quantity} , {Inventory[Prod]} left")

        case Prod :
            print(f"{Prod} : only {Inventory[Prod]} in stock , cannot ship {Quantity}")