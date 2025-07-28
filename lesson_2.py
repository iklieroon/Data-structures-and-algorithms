'''class Person:
    def __init__(self):
        self.__name1="Rohan"
        self.age1=13

P1=Person()
print(P1.__name1)'''

class Person1:
    def __init__(self,name,age):
        self._name=name
        self._age=age
    def get_age(self):
        return self._age
    def set_age(self,age):
        if age>0:
            self._age=age
        else:
            print("age must be positive")

P11=Person1("Raj",14)
print(P11.get_age())
P11.set_age(15)
print(P11.get_age())
P11.set_age(-15)
print(P11.get_age())