class Employee:
    raise_amt=1.04
    def __init__(self,firstname=None,lastname=None,id=0,pay=0):
        self.firstname=firstname
        self.lastname=lastname
        self.id=id
        self.pay=pay
    def accept(self):
        self.firstname=input("enter the name")
        self.lastname=input("enter the name")
        self.id=int(input("enter the id "))
        self.pay=int(input("enter pay "))
    def raise_amt1(self):
        self.pay=int(self.pay*self.raise_amt)
    def display(self):
        print(self.firstname)
        print(self.lastname)
        print(self.id)
        print(self.pay)
class manager(Employee):
    raise_amt=2.04
    def raise_amt1(self):
        self.pay=int(self.pay*self.raise_amt)
class developer(Employee):
    raise_amt=1.22
    def raise_amt1(self):
        self.pay=int(self.pay*self.raise_amt)
while True:
    print("1.create manager \n2.create developer \n3.display manager \n4.display developer \n5raise manager \n6.raise developer \n")
    ch=int(input("enter ur choice "))
    if ch==1:
        e1=manager()
        e1.accept()
    elif ch==2:
        e2=developer()
        e2.accept()
    elif ch==3:
        e1.display()
    elif ch==4:
        e2.display()
    elif ch==5:
        e1.raise_amt1()
    elif ch==6:
        e2.raise_amt1()