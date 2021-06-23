m1=[]
m2=[]
m3=[]
r=int(input("Enter no of rows: "))
c=int(input("Enter no of cols: "))
print("Enter Matrix1 elements: ")
for i in range(0,r):
    list1=[]
    for j in range(0,c):
        list1.append(int(input("Enter element: ")))
    m1.append(list1)
for i in m1:
    for j in i:
        print(j,end="\t")
    print()
print("Enter Matrix2 elements: ")
for i in range(0,r):
    list1=[]
    for j in range(0,c):
        list1.append(int(input("Enter element: ")))
    m2.append(list1)
for i in m2:
    for j in i:
        print(j,end="\t")
    print()
for i in range(0,r):
    l1=m1[i]
    l2=m2[i]
    l3=[]
    for j in range(0,c):
        l3.append(l1[j]+l2[j])
    m3.append(l3)
print("The sum is:")
for i in m3:
    for j in i:
        print(j,end="\t")
    print()
