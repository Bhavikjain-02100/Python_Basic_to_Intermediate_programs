def vowel(n):
    count=0
    vowel="aeiouAEIOU"
    for i in n:
        if i in vowel:
            count+=1
            print(i,end=",")
    print(" :",count)
strin=input("Enter a string:")
vowel(strin)