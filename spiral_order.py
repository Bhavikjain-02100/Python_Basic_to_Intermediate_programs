import ast

def spir_o(ls):
    temp_ls = []
    ma=len(ls)
    n=len(ls[0])
    top, bottom = 0, ma-1
    left, right = 0, n-1

    while top<=bottom and left<=right:
        for i in range(left, right+1):
            temp_ls.append(ls[top][i])
        top+=1

        for i in range(top, bottom+1):
            temp_ls.append(ls[i][right])
        right-=1

        if top<=bottom:
            for i in range(right, left-1, -1):
                temp_ls.append(ls[bottom][i])
            bottom-=1

        if left<=right:
            for i in range(bottom, top-1, -1):
                temp_ls.append(ls[i][left])
            left+=1

    print(temp_ls)

# Example usage
data=ast.literal_eval(input(""))
spir_o(data)
