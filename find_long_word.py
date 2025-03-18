def find_long_word(s):
    dict={}
    for i in s:
        dict[i]=len(i)
    max_i=max(dict,key=dict.get)
    print(max_i)

lis=["apple","banana","pear"]
find_long_word(lis)