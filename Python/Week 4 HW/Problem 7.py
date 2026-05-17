Age = int(input("Enter Your Age : "))
Job = input("Do You have a Job : ")
Monthly_Income = int(input("Enter Monthly Income : "))

if Age < 21 or Age > 65 :
    print("Rejected: age not eligible")
else :
    if Job == "no" :
        print("Rejected: no job")
    else :
        if Monthly_Income >= 5000 :
            print("Approved")
        else :
            if Monthly_Income >= 3000 :
                print("Approved with conditions")
            else :
                print("Rejected: low income")