class Student:
    school="OOPs"

    def __init__(self,mark1,mark2,mark3):
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3

    def average(self):
        return (self.mark1+self.mark2+self.mark3)/3

    def getMarks(self):
        print(f"marks1: {self.mark1}")

    def setMarks(self,mark1):
        self.mark1=mark1

    @classmethod
    def getSchool(cls):
        print(f"School: {cls.school}")

    @staticmethod
    def info():
        print("This is a Student Class in Python Module")

s1=Student(65,75,87)
s2=Student(87,83,67)

print(s2.average())
print(s1.getMarks())
print(Student.getSchool())
