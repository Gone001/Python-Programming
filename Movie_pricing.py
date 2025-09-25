name=input("Enter you name :")
age=int(input("Enter your age :"))
movie_type=input("Enter the movie type\n 2D or 3D\n").strip().upper()
base_price=200
ticket=int(input("Enter the no of tickets :"))
discount=0
match  movie_type:
    case "3D":
        base_price+=100
    case "2D":
        pass
    case _:
        print("Not availabe")
        exit()
total_price = base_price * ticket
weekend=input("Day of the Show | Weekend or Weekday :").strip().upper()
if weekend=="WEEKEND":
    total_price+=ticket*50
#age validator 
if age<12:
    discount=0.5
elif 12<=age<=60:
    pass
else :
    discount=0.3
discounted=total_price*discount
print(f"Your discount {discounted:.2f}")
total=total_price*(1-discount)
print(f"Your Total price {total:.1f}")
    