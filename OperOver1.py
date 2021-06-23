from OperOver import *
flag=True
while flag:
    o1=Oper()
    o1.get_elements()
    o2=Oper()
    o2.get_elements()
    if len(o1.alist)==len(o2.alist):
        flag=False
        while True:
            print("*"*50)
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exit")
            print("*"*50)
            ch=int(input("Enter the choice: "))
            if ch==1:
                print(o1+o2)
            elif ch==2:
                print(o1-o2)
            elif ch==3:
                print(o1*o2)
            elif ch==4:
                print(o1//o2)
            elif ch==5:
                break
            else:
                print("Enter valid choice")
    else:
        print("***Enter lists of same length***")