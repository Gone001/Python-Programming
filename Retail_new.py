brands={"WOODLAND":{"PANT":1200,"SHIRT":2200,"SHOES":5500},"LEVIS":{"PANT":1500,"SHIRT":2500,"SHOES":6000},"VEROMODA":{"PANT":1800,"SHIRT":2800,"SHOES":6500},"US-POLO":{"PANT":2000,"SHIRT":3000,"SHOES":7000}}
cart=[]
total=0
while True:
    take=input("Choose the brand you want to purchase (or type EXIT to stop)\nWoodland\nLevis\nVeromoda\nUS-Polo\nEXIT :- Finish shopping\n").strip().upper()
    if take=="EXIT":
        break
    if take not in brands:
        print("Invalid brand,try again.")
        continue
    print(f"Available products in {take}:")
    for product,price in brands[take].items():
        print(f"{product}:{price}")
    add=input("Enter the product:").strip().upper()
    if add not in brands[take]:
        print("Not available")
        continue
    
    quantity=int(input(f"Enter the no of {add} you want to buy:"))
    price=brands[take][add]
    item_total=price*quantity
    cart.append((take,add,quantity,price,item_total))
    total+=item_total
    print(f"Added {quantity} {add}(s) from {take} at Rs {price} each.Subtotal={item_total}")
    
if total>=10000:
    print("You got a Gift Voucher worth Rs 1000")
    total-=1000
elif total>=5000:
    print("You got a Gift Voucher worth Rs 500")
    total-=500
print("========== Final Bill ==========")
for brand,product,qty,unit_price,subtotal in cart:
    print(f"{brand}-{product} x {qty} @ Rs {unit_price}={subtotal}")
print("--------------------------------")
print(f"Grand Total:Rs {total}")
print("================================")
