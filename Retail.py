while True:
    take = input(
        "Choose the brand you want to purchase \n"
        "Woodland :- 20% Discount\n"
        "Levis :- 30% Discount\n"
        "Veromoda :- 35% Discount\n"
        "US-Polo :- 40% Discount\n"
    ).strip().upper()

    total = 0

    match take:
        # Woodland
        case "WOODLAND":
            add = input("Enter the product : \nPant : Rs 1000\nShirt : Rs 2000\nShoes : Rs 5000\n").strip().upper()
            quantity = int(input(f"Enter the no of {add} you want to buy: "))
            if add == "PANT":
                total = quantity * (1000 * 0.8)  # 20% off
            elif add == "SHIRT":
                total = quantity * (2000 * 0.8)
            elif add == "SHOES":
                total = quantity * (5000 * 0.8)
            else:
                print("Not Available")
                continue  # restart loop
            break  #  valid choice, exit loop

        # Levis
        case "LEVIS":
            add = input("Enter the product : \nPant : Rs 1000\nShirt : Rs 2000\nShoes : Rs 5000\n").strip().upper()
            quantity = int(input(f"Enter the no of {add} you want to buy: "))
            if add == "PANT":
                total = quantity * (1000 * 0.7)  # 30% off
            elif add == "SHIRT":
                total = quantity * (2000 * 0.7)
            elif add == "SHOES":
                total = quantity * (5000 * 0.7)
            else:
                print("Not Available")
                continue
            break

        # Veromoda
        case "VEROMODA":
            add = input("Enter the product : \nPant : Rs 1000\nShirt : Rs 2000\nShoes : Rs 5000\n").strip().upper()
            quantity = int(input(f"Enter the no of {add} you want to buy: "))
            if add == "PANT":
                total = quantity * (1000 * 0.65)  # 35% off
            elif add == "SHIRT":
                total = quantity * (2000 * 0.65)
            elif add == "SHOES":
                total = quantity * (5000 * 0.65)
            else:
                print("Not Available")
                continue
            break

        # US-Polo
        case "US-POLO":
            add = input("Enter the product : \nPant : Rs 1000\nShirt : Rs 2000\nShoes : Rs 5000\n").strip().upper()
            quantity = int(input(f"Enter the no of {add} you want to buy: "))
            if add == "PANT":
                total = quantity * (1000 * 0.6)  # 40% off
            elif add == "SHIRT":
                total = quantity * (2000 * 0.6)
            elif add == "SHOES":
                total = quantity * (5000 * 0.6)
            else:
                print("Not Available")
                continue
            break

        case _:
            print("Invalid brand, please try again.\n")
            continue  # ask again

#  After loop ends (valid brand + product chosen)
if total >= 5000:
    print("You got a Gift Voucher worth Rs 500 ")
    total -= 500

print(f"\nYour total bill is Rs {total:.2f}")
