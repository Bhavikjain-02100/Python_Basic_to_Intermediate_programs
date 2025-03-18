def patt(n):
    spaces=3
    start=1
    for i in range(0,n):
        c=1
        for k in range(0,spaces):
            print(" ",end=" ")
        for j in range(0,start):
            print(c,end=" ") 
            if(j<int(start/2)):
                c+=1
            else:
                c-=1
           
        print(" ")
        if i<3:
            spaces-=1
            start+=2
        else:
            spaces+=1
            start-=2
        
patt(7)
                
                
        
