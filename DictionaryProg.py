d={}
class Employee:

    def sal(self, name, addr, pan, basic, tds=0, ded=0):
        self.name=name
        self.addr=addr
        self.pan=pan
        self.basic=basic
        self.tds=tds
        self.ded=ded
        self.hra=int(1.15*self.basic)
        self.gross=self.basic+self.hra
        netsal=self.gross-(self.tds+self.ded)
        return netsal
    
    def accept(self):
        name=input("Enter emp_Name: ")
        addr=input("Enter emp_Address: ")
        pan=input("Enter emp_PAN_No: ")
        basic=int(input("Enter emp_Salary: "))
        tds=int(input("Enter emp_TDS: "))
        ded=int(input("Enter emp_Deduction: "))
        self.netsal=self.sal(name, addr, pan, basic, tds, ded)
    
    def disp(self):
        print("Name: ", self.name)
        print("Address: ", self.addr)
        print("PAN No.: ", self.pan)
        print("Basic Salary: ", self.basic)
        print("Net Salary: ", self.netsal)
    
    def search(self, name):
        for k,v in d.items():
            print(k)
            print(v)
            if k==name:
                print(v.__dict__)
                
while True:
    print("*"*50)
    print("1. Enter Employee Details:")
    print("2. Display")
    print("3. Update Dictionary")
    print("4. Search Employee")
    print("5. Exit")
    print("*"*50)
    ch=int(input("Enter a choice: "))
    print("*"*50)
    if ch==1:
        e=Employee()
        print(id(e))
        e.accept()
    elif ch==2:
        e.disp()
    elif ch==3:
        d.update({e.name:e})
        print(d)
    elif ch==4:
        e.search(input("Enter the name: "))
    elif ch==5:
        break
    else:
        print("Plz enter valid choice")
    print("*"*50)
