class Student:
    def __init__(self,name=None,usn=None,age=None):
        self.name=name
        self.usn=usn
        self.age=age
    def getdata(self):
        self.name=input("Enter the name: ")
        self.usn=input("Enter the usn: ")
        self.age=int(input("Enter the age: "))
    def display(self):
        print(self.name)
        print(self.usn)
        print(self.age)
class UG(Student):
    def __init__(self,sem=None,fee=None,stipend=None):
        super().__init__(self)
        self.sem=sem
        self.fee=fee
        self.stipend=stipend
    def ugdata(self):
        self.getdata()
        self.sem=int(input("enter the sem"))
        self.fee=int(input("enter the fee"))
        self.stipend=int(input("enter the stipend"))
    def ugdisplay(self):
        self.display()
        print(self.sem)
        print(self.fee)
        print(self.stipend)
class PG(Student):
    def __init__(self,sem=None,fee=None,stipend=None):
        super().__init__(self)
        self.sem=sem
        self.fee=fee
        self.stipend=stipend
    def pgdata(self):
        self.getdata()
        self.sem=int(input("enter the sem"))
        self.fee=int(input("enter the fee"))
        self.stipend=int(input("enter the stipend"))
    def pgdisplay(self):
        self.display()
        print(self.sem)
        print(self.fee)
        print(self.stipend)
while True:
    print("1. create ug\n2. create pg\n3. display ug data\n 4. display pg data ")
    ch=int(input("enter the choice"))
    if ch==1:
        s1=UG()
        s1.ugdata()
    elif ch==2:
        s2=PG()
        s2.pgdata()
    elif ch==3:
        s1.ugdisplay()
    elif ch==4:
        s2.pgdisplay()
    else:
        print("invalid choice")
        break