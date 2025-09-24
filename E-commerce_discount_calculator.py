dict={"Regular":{"Pant":600,"Shirt":800,"Shoe":1000},# Dictionary for already  fixed price and products 
    "Premium":{"Pant":1000,"Shirt":3000,"Shoe":3000},
    "Vip":{"Pant":2000,"Shirt":6000,"Shoe":10000},}

# print all the products with categry and prize

print("Available products and their categories\n")
for category,item  in dict.items():                  # for each loop to print the category in dictionary 
    print(f"\n {category}\n")                  
    for product ,price in item.items():               # for each loop to print the items and their prize in dictionary 
        print(f"{product.capitalize()}: Rs{price}")


# user input or choice for category 
take=input("Enter the Product category :").strip().capitalize()  
if take not in dict:                                            # validator
    print("Sorry this product Category is not available :")
    exit()  # Restart the choice if incorrect 
    
# user input for product
choice=input("Enter the product:").strip().capitalize() 
if (choice not in dict[take]):                          # validator 
    print(f"Sorry this product is not availabe in :{take} ")
    exit() # Restart the choice if incorrect 

total=dict[take][choice]
print(f"Total Amount :{total} ")
discount=0

# match case to provide discount 
match take :
    case "Regular":
        if (total<500):
            discount=0.05
        else:
            discount=0.10
        
    case "Premium":
        if(total<1000):
            discount=0.15
        else:
            discount=0.20
            
    case "Vip":
        discount=0.25
    case _:
        print("Invalid Category")
        exit()
print(f"Your  Base discount is {total*discount:.2f}")

# paymet method

method=input("Payment method | 'Cash' or 'Online':").strip().capitalize()  
if method=="Online":
    print("Congratultions you got '5%' discount on online purchase :")
    discount+=0.05
elif method!="Cash":
    print("This payment method is not availabe :")
final_amount=total*(1-discount)
print(f"Your final amount is {final_amount:.2f}:")
        