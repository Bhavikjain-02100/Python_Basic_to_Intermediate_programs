class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

    def show(self):
        print(f"name: {self.name}, roll: {self.roll}")

    class Laptop:
        def __init__(self):
            self.brand="Asus"
            self.cpu="Ryzen 7"
            self.ram="16GB"

        def config(self):
            print(f"brand: {self.brand},CPU: {self.cpu}, RAM: {self.ram}")

s1=Student("harsh",767)
s2=Student("shukla",6969)

s2.show()
l1=s1.Laptop()
l2=Student.Laptop()

l1.config()
l2.config()
print(type(l1))
print(type(l2))



