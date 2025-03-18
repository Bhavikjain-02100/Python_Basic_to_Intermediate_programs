#Caesar Cipher Problem: Acc to this each character of string has move by given shifts so "H" becomes "k"
def cae_ci(i_str,shift):
    str=i_str.upper()
    Arr="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res_str=""
    for i in range(len(str)):
        for j in range(len(Arr)):
            if str[i]==Arr[j]:
                res_str+=Arr[j+3]
    print(res_str)
cae_ci("Hello",3)
