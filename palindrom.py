def is_palin(s):
    rev_str=s[::-1]
    print(rev_str)
    if rev_str==s:
         print("String is palindrome")
    else:
        print("String is not palindrome")
strin=input("Enter a string:")
is_palin(strin)
