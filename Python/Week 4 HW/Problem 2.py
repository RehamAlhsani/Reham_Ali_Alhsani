Year = int(input("Enter Year : "))

if Year % 4 == 0 :
    if Year % 100 == 0 :
        if Year % 400 == 0 :
            print("Leap Year")
        else :
            print("Not a Leap Year")
    else :
        print("Leap Year")
else :
    print("Not a Leap Year")