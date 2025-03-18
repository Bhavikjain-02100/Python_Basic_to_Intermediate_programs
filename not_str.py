def not_str(a):
    if(len(a)>3):
        if(a[0:2]=="Not"):
            print(a)
        else:
            print("Not "+a)
    else:
        print("Not "+a)
string_u=input("Enter a string:")
not_str(string_u)
