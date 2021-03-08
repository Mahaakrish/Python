while True:
    print("*"*50)
    print("1. Upper")
    print("2. Lower")
    print("3. Concat")
    print("4. Extract")
    print("5. Reverse")
    print("6. Length")
    print("7. Range slice")
    print("8. Split")
    print("9. In")
    print("10. Not In")
    print("*"*50)
    ch=int(input("Enter a choice: "))
    if ch==1:
        a=input("Enter a string: ")
        print(a.upper())
    elif ch==2:
        a=input("Enter a string: ")
        print(a.lower())
    elif ch==3:
        a=input("Enter string A: ")
        b=input("Enter string B: ")
        c=a+b
        print(c)
    elif ch==4:
        a=input("Enter a string: ")
        n=int(input("Enter the position: "))
        print(a[n])
    elif ch==5:
        a=input("Enter a string: ")
        b=a[::-1]
        print(b)
    elif ch==6:
        a=input("Enter a string: ")
        print(len(a))
    elif ch==7:
        a=input("Enter a string: ")
        st=int(input("Enter starting point: "))
        en=int(input("Enter ending point: "))
        print(a[st:en])
    elif ch==8:
        a=input("Enter a sentence: ")
        b=a.split()
        print(b)
    elif ch==9:
        a=input("Enter a string: ")
        b=input("Enter a character: ")
        c=b in a
        print(b, " in ", a, c)
    elif ch==10:
        a=input("Enter a string: ")
        b=input("Enter a character: ")
        c=b not in a
        print(b, " not-in ", a, c)
    else:
        print("Invalid choice")
    print("*"*50)