class Car:
    def __init__(self,b,m):
        self.b=b
        self.m=m
    def engine(self):
        print(f"{self.b} {self.m} Has a good engine")

C1=Car("Toyota","Camry")
C2=Car("BMW","3 Series")
print(C1.b)
print(C1.m)
print(C2.b)
print(C2.m)
C1.engine()