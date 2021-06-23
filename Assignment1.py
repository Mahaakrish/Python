class Example:
    def __init__(self):
        self.a=int(input("Enter a number: "))
    def __add__(self,other):
        return self.a+other.a
    def sum(o1,o2):
        return o1.a+o2.a
e1=Example()
e2=Example()
print(e1+e2)
print(Example.sum(e1,e2))