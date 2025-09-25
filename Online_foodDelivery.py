name=input("Enter the name :")
delivery_charges=50
user_type=input("Choose the Category \n1.NORMAL \n2.GOLD \n3.PLATINUM \n").strip().upper()
discount=0
match user_type:
    case "NORMAL":
        pass
    case "GOLD":
        discount=0.2
    case "PLATINUM":
        discount=0.3
    case _:
        print("Invaid")
        exit()
distance=int(input("Enter the Distance :"))
if distance>5:
    extra_charge=(distance-5)*10
    delivery_charges+=extra_charge
    print(f"Extra delivery charges for {distance} km {delivery_charges}")
    
amount=int(input("Enter the amount :")) 
if amount>=1000:
    delivery_charges=0
    print("Free delivery")

total_before_discount=amount+delivery_charges
total_after_discount=total_before_discount*(1 - discount)

print(f"Total price (before discount): Rs {total_before_discount}")
print(f"Total bill after discount for {user_type} user: Rs {total_after_discount:.2f}")