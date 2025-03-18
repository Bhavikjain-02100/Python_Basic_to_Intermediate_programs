class Computer:
    def __init__(self):
        self.name="Bhavik"
        self.age=22

    def getDetails(self):
        return self.name, self.age

    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False

    def update(self):
        self.age=24
        return self.age,self.name

c1=Computer()
c2=Computer()

print(c1.getDetails())
print(c2.update())
if c1.compare(c2):
    print("They are same")
else:
    print("They are different")

