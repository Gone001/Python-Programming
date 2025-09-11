def add(num1):
    if(num1>0):
        if (num1%2==0):
            print("No is + even ")
        else:print("No is odd ")
    if(num1<0):
        if(num1%-2==0):
            print("No is - even ")
        else:
            print("No is - odd ")
num1=int (input("Enter the no "))
add(num1)