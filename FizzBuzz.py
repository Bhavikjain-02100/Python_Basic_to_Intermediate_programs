#Problem: Print 1 to 100 but for multiple of 3 and 5, print "Fizz" and "Buzz" respectively
for i in range(1,101):
    if i%3!=0 and i%5!=0:
        print(i)
    elif i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")