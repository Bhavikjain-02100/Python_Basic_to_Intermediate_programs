
class mammel:
    def whale(self):
        print("They are largest mammel")

class Aquatic:
    def whale(self):
        print("They are largest aquatic animals")
        print("When they die they give life to other creatures for more than 100 years")

class endangered:
    def animal(self,name):
        name.whale()



if __name__=="__main__":
    for i in mammel(),Aquatic:
        if hasattr(i,'whale'):
            i.whale()