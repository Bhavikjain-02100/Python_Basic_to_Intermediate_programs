import ast

def dig_tra(matrix):
    temp_ls=[]
    rows=len(matrix)
    cols=len(matrix[0])

    for b in range(rows+cols-1):
        rs_ls = []
        if b<cols:
            i,j=0,b
        else:
            i,j=b-cols+1,cols-1
        while i<rows and j>=0:

            rs_ls.append(matrix[i][j])
            i+=1
            j-=1
        temp_ls.append(rs_ls)
    print(temp_ls)

data=ast.literal_eval(input(""))
dig_tra(data)