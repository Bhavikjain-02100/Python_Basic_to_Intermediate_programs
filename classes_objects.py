class Person:
    name="Bhavik"
    age=22
    def __init__(self,n):
        self.n=n

    def getDetails(self):
        return "get details: " ,self.n, self.age

    def getN(self):
        print("getN: ",self.n)

pOne=Person("Suresh")
pTwo=Person("Shukla")

print(pOne.getDetails())
pTwo.getN()

# class is data structure which holds a value but reference is refer that location to which has value
