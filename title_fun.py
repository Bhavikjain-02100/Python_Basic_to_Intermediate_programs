def tit(stri):
    new_str=""
    for i in range(0,(len(stri))+1):
        if i==0:
            up=(stri[i].upper())
            new_str+=up
        elif stri[i]==" ":
            new_str+=" "
            up=(stri[i+1]).upper()
            new_str+=up

        else:
            new_str+=stri[i+1]
    print(new_str)
tit("python is progra lan")
