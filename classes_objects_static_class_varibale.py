class Car:
    wheels=4

    def __init__(self):
        self.mil=10
        self.brand="Toyota"

c1=Car()
c2=Car()
c1.mil=20
print(f"C1\nmil: {c1.mil},wheels: {c1.wheels},brand: {c1.brand}")
Car.wheels=6
print(f"\nC2:\nmil: {c2.mil},wheels: {c2.wheels},brand: {c2.brand}")
