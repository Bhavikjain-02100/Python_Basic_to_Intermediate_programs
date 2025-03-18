def login(u,p):
    username_def="Devil02100"
    password_def="12345678"
    if(u==username_def and p==password_def):
        print("Access Granted")
    else:
        print("Access Denied")
username=input("Enter the username:")
password=input("Enter the password:")
login(username,password)
