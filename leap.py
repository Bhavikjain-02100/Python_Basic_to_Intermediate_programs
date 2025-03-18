def leap(y):
    if((y%4==0)or(y%4!=0 or y%100==0)):
        print("yes")
    else:
        print("no")
year=int(input("Enter the year:"))
leap(year)
