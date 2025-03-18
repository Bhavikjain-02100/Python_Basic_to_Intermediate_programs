class Cars:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        print(f"Brand: {self.brand}, Model: {self.model}")

    def __del__(self):
        print("The objects are about to be destroyed")

car1=Cars("Toyota","Hillux")
del car1