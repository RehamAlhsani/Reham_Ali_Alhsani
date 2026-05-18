A = int(input("Enter First Side : "))
B = int(input("Enter Second Side : "))
C = int(input("Enter Third Side : "))

if A == B :
    if B == C :
        print("Equilateral")
    else :
        print("Isosceles")
else :
    if A == C :
        print("Isosceles")
    else :
        if B == C :
            print("Isosceles")
        else :
            print("Scalene")