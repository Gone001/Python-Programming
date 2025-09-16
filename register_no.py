reg_no = int(input("Enter your registration number (1-61): "))

if reg_no < 1 or reg_no > 61:
    print("Invalid registration number! Please enter between 1 and 61.")
else:
    if 1 <= reg_no <= 10:
        row = 1
    elif 11 <= reg_no <= 20:
        row = 2
    elif 21 <= reg_no <= 30:
        row = 3
    elif 31 <= reg_no <= 40:
        row = 4
    elif 41 <= reg_no <= 50:
        row = 5
    else:
        row = 6
    print(f"Registration No {reg_no} is assigned to Row {row}")


reg_no= int(input("Enter your registration number (1-61): "))

match reg_no:
    case n if 1<=n <=10:
        row =1
    case n if 11<=n<=20:
        row=2
    case n if 21<=n<=30:
        row=3
    case n if 31<=n<=40:
        row=4
    case n if 41<=n<=50:
        row=5
    case n if 51<=n<=60:
        row=6
print(f"Registration no {reg_no} is assigned to row {row}")