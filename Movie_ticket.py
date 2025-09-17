take=input("Enter the choice of seat \nClassic :- $200\nPremium :- $300\nRecliner :- $500\n").strip().lower()
print()
total=0

match take:
    case "classic":
        seat=int(input("Enter the number of seats: "))
        total=seat*200
    case "premium":
        seat=int(input("Enter the number of seats: "))
        total=seat*300
    case "recliner":
        seat=int(input("Enter the number of seats: "))
        total=seat*500
    case _:
        print("Invalid choice")
        exit() 


if 500<=total<1500:
    print("Add meal worth $200 for '2%' Discount")
    yes=input("Do you want to add it? (YES/NO):").strip().lower()
    if yes=="yes":
        total+=200
        print(f"Your total amount including meal is: ${total}")
    else:
        print(f"Your total bill is: ${total}")
elif total>=1500:
    print("Add meal worth $500 for '4%' Discount")
    yes=input("Do you want to add it? (YES/NO):").strip().lower()
    if yes=="yes":
        total+=500
        print(f"Your total amount including meal is: ${total}")
    else:
        print(f"Your total bill is: ${total}")
else:
    print(f"Your total bill is: ${total}")
