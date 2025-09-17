take=input("Enter the choice of seat \n Classic :-$200\n Premium :-$300 \n Recliner:-$500\n").strip().lower()
print()
total=0
match take :
    case "classic" :
        seat=int(input("Enter the no of seats "))
        total=seat*200
    case "premium":
        seat=int(input("Enter the no of seats "))
        total=seat*300
    case "recliner" :
        seat=int (input("Enter the no of seats "))
        total=seat*500
    case _:
        print("Invalid ")
        exit()
    
if(500<=total<=1500):
    print(f"Your total price is : {total}")
    print("Add meal worth $200 or '2%' Discount ")
    yes=(input("Do you want to add say (YES) or (NO) "))
    
    if(yes == "yes"):
        add=total
        print(f"Your total amount for {take} seats and meal is :\n for {seat} Seat :{total}\nAdded meal worth $200 :\nYour total is :{add} ")
    else:
        discount=total*0.02
        total=total-discount
        print(f'Your Total bill is {total}')
elif(total>=1500):
    print(f"Your total price is : {total}")
    print("Add meal worth $500 or '4%' Discount ")
    yes=(input("Do you want to add say (YES) or (NO) "))
   
    if(yes == "yes"):
        add=total
        print(f"Your total amount for {take} seats and meal is :\n for {seat} Seat :{total}\nAdded meal worth $200 :\nYour total is :{add} ")
    else:
        discount=total*0.02
        total=total-discount
        print(f'Your Total bill is{total}')
else:print(f"Your total price is : {total}")