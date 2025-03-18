def tic_pr(a):
    price=0
    if(a<=12):
        price=price+5
    elif(a>12 and a<=64):
        price=price+12
    else:
        price=price+7
    print(f"The ticket price: ${price}")
age=int(input("Enter the age of person:"))
tic_pr(age)
