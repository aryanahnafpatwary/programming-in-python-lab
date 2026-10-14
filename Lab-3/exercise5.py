m=int(input("Enter Marks: "))
if m<=100 and m>=0:
    if m>=90:
        print("A+")
    elif m>=85:
        print("A")
    elif m>=80:
        print("B+")
    elif m>=75:
        print("B")
    elif m>=70:
        print("C+")
    elif m>=65:
        print("C")
    elif m>=60:
        print("D+")
    elif m>=50:
        print("D")
    else:
        print("F")
else:
    print("Invalid Input")