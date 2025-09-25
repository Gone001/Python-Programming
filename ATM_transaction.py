import sys
Account_type=input("Account type \n1.Saving\n2.Current\n").strip().upper()
match Account_type:
    case "SAVING":
        print("You can only withdraw at a limit of Rs:25000")
        limit=25000
    case "CURRENT":
        print("You can only withdraw at a limit of Rs:50000")
        limit=50000
    case _:
        print('Invalid account type')
        sys.exit()
        
balance=int(input("Enter the Amount :"))
if(balance<=1000):
    print("Minimum balance reqired is Rs:1000")
    sys.exit()
Withdraw=int(input("Enter the withdrawl Amount :"))
if balance-Withdraw<1000:
    print("You cannot withdraw Minimum balance reuired Rs 1000")
    sys.exit()
if Withdraw>balance:
    print(f"Insufficient balance  {balance}")
    sys.exit()
if Withdraw>limit:
    print(f"You cannot withdraw more than {limit}")
    sys.exit()
    
weekend=input("WEEKEND or WEEKDAY").strip().upper()
if weekend=="WEEKEND":
    if balance - Withdraw - 50 < 1000:
        print("Cannot deduct weekend charge. Minimum balance violation")
        sys.exit()
    balance-=50
    print("Weekend charge RS 50")
balance-=Withdraw
print("YOU Withdrwal is Succeed")
print(f"Your balance {balance}")