def char_count(f,s):
    dict_a={}
    dict_b={}
    for i in f:
        fir=f.count(i)
        dict_a[i]=fir
    print(dict_a)
    for j in s:
        sec=s.count(j)
        dict_b[j]=sec
    print(dict_b)
    comp_a=dict_a.items()
    comp_b=dict_b.items()
    len_a=len(f)
    len_b=len(s)
    if comp_a==comp_b and len_a==len_b:
        print("anagram")
    else:
        print("not")
strin=input("Enter a string:")
strin_2=input("Enter a second:")

char_count(strin,strin_2)
