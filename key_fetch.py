from turtle import TurtleGraphicsError
ts=1
dict={
    'bhavik':80,
    'harsh':95,
    'ravi':89,
    'jayant':89
}
find=89
for i,j in dict.items():
    if j!=find:
        ts=0
    else:
        ts=1
        print(i)
if ts==0:
    print("not found")