take=input("choose the brand you want to purchase \n Woodland:-'20%' Discount\n Levis:-'30%' Discount\n Veromoda:-'35%' Discount\n Us-polo:-'40%' Discount\n").strip().lower().upper()
total=0
print()
match take:
    #Woodland
    case "Woodland": 
        add=input("Enter the product : \n Pant :Rs 1000\nShirt:Rs 2000\n Shoes:Rs 5000").strip().lower().upper()
        quantiity=int(f"Enter the no of {add} you wnat to buy :")
        if(add=="Pant"):
            total=quantiity*1000
        elif add=="Shirt":
            total=quantiity*2000
        elif add=="Shoe":
            total=quantiity*5000
        else:print("Not Available")
        # Levis
    case "Levis": 
        add=input("Enter the product : \n Pant :Rs 1000\nShirt:Rs 2000\n Shoes:Rs 5000").strip().lower()
        quantiity=int(f"Enter the no of {add} you wnat to buy :")
        if(add=="Pant"):
            total=quantiity*800
        elif add=="Shirt":
            total=quantiity*2500
        elif add=="Shoe":
            total=quantiity*10000
        else:print("Not Available")
        #Veromoda
    case "Veromoda": 
        add=input("Enter the product : \n Pant :Rs 1000\nShirt:Rs 2000\n Shoes:Rs 5000").strip().lower()
        quantiity=int(f"Enter the no of {add} you wnat to buy :")
        if(add=="Pant"):
            total=quantiity*900
        elif add=="Shirt":
            total=quantiity*3500
        elif add=="Shoe":
            total=quantiity*6000
        else:print("Not Available")
        #US-polo
    case "US-polo": 
        add=input("Enter the product : \n Pant :Rs 1000\nShirt:Rs 2000\n Shoes:Rs 5000").strip().lower()
        quantiity=int(f"Enter the no of {add} you wnat to buy :")
        if(add=="Pant"):
            total=quantiity*600
        elif add=="Shirt":
            total=quantiity*1500
        elif add=="Shoe":
            total=quantiity*7000
        else:print("Not Available")
    case _:
        print("Invalid")
        exit()
if(total>=5000):
    print("You Got a Gift Voucher worth Rs 500 ")
    total=total-500
    print(f"Your total bill is :\n for {add} :{total}")
else:print(f"Your total bill is {total}")