
class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self, other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        t=Student(m1,m2)
        return t

    def __gt__(self, other):
        g1=self.m1+other.m1
        g2=self.m2+other.m2
        if g1>g2:
            return "first number is greatest"
        else:
            return "second is greatest"

s1=Student(89,87)
s2=Student(75,87)

ans=s1+s2

print(ans.m1," ",ans.m2)