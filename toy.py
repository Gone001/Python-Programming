toy_category = input("Enter toy category (electronics, plastic, sports, robotics, battery, mechanical): ").lower()

if toy_category == "electronics":
    price = 1500
elif toy_category == "plastic":
    price = 300
elif toy_category == "sports":
    price = 700
elif toy_category == "robotics":
    price = 2500
elif toy_category == "battery":
    price = 1200
elif toy_category == "mechanical":
    price = 1000
else:
    price = None

if price:
    print(f"The price of {toy_category} toy is Rs: {price}")
else:
    print("Invalid category! Please enter a valid toy type.")
