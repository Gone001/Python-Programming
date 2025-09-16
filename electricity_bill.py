units = int(input("Enter the total units of a month: "))

if units <= 100:
    bill = units * 2
elif 101 <= units <= 200:
    bill = units * 3
elif 201 <= units <= 299:
    bill = units * 4
else: 
    bill = units * 5

if bill >= 1000:
    discount = bill * 5 / 100
    final_bill = bill - discount
    print(f"Your Electricity bill for {units} units is Rs: {final_bill} (after 5% discount)")
else:
    print(f"Your Electricity bill for {units} units is Rs: {bill}")
