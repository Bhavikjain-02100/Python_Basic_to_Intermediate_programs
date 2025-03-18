def longest_consecutive(ls):
    ls_set = set(ls)
    long_c=0
    print(ls_set)
    for i in ls_set:
        if i-1 not in ls_set:
            c_num= i
            count= 1
            while c_num+1 in ls_set:
                c_num+=1
                count+=1
            long_c=max(long_c, count)
    return long_c


input_list = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(input_list))
