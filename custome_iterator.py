
class Topten:
    def __init__(self,stop):
        self.num=1
        self.stop=stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.num<=self.stop:
            val=self.num
            self.num+=1
            return val
        else:
            raise 

n=Topten(10)

for i in n:
    print(n)