class Car:
    def __init__(self,b,m):
        self.b=b
        self.m=m
    def engine(self):
        print(f"{self.b} {self.m} has a good engine")

C1=Car("Toyota","Camry")
C2=Car("BMW","3 Series")
print(C1.b)
print(C1.m)
print(C2.b)
print(C2.m)
C1.engine

#Homework

class Pupil:
    def __init__(self,name,age,merits):
        self.name=name
        self.age=age
        self.merits=merits
    def grades(self):
        print(f"{self.name} has good grades")

P1=Pupil("Rohan","13","24")
print(P1.name,P1.age,P1.merits)
P1.grades()
P2=Pupil("Raj","14","2")
print(P2.name,P2.age,P2.merits)