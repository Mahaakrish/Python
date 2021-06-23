age=[]
n=int(input("Enter no of candidates: "))
for i in range(0,n):
    age.append(int(input("Enter age: ")))
x=map(lambda y:y>=18,age)
for i in list(x):
    if i==True:
        print("Eligible candidate")
    else:
        print("Ineligible candidate")
