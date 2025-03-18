def char_count(s):
    dict={}
    for i in s:
        sam=s.count(i)
        dict[i]=sam
    print(dict)
strin=input("Enter a string:")
char_count(strin)
