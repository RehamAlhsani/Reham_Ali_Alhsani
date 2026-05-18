Age = int(input("Enter Your Age : "))
Day = input("Enter The Day : ")

if Age < 12 :
    Price = 20
else :
    if Age <= 17 :
        Price = 35
    else :
        if Age <= 59 :
            Price = 50
        else :
            Price = 25

if Day == "Tuesday" :
    Price = Price - 10
    if Price < 10 :
        Price = 10
        
print(f"{Price} SAR")