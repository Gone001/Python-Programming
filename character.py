
name =input("Enter the  name ")
print()
n=int(input("Enter 1 for capital words\nEnter 2 for small letters "))
match n:
    case 1 if n==1:
        print(name.upper())
    case 2 if n==2:
        print(name.lower())