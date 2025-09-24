import sys
name=input("Enter the name of the Person :")
speedfine=0
fine=0
eligble=False
vechile=input("Enter the vechile category \n CAR \n Bike \n Truck ").strip().upper()
if(vechile=="CAR"):
    check=input("Did  you wear Seatbelt : YES or NO ").strip().upper()
    if(check=="NO"):
        fine+=1000
        eligble=True
        print(f"Fine added Rs {fine}")
    
elif(vechile=="BIKE"):
    check=input("Did  you wear healmet : YES or NO ").strip().upper()
    if(check=="NO"):
        fine+=1000
        eligble=True
        print(f"Fine added Rs {fine}")
elif(vechile=="TRUCK"):
    check=input("Did  you wear Seatbelt : YES or NO ").strip().upper()
    if(check=="NO"):
       fine+=1000
       eligble=True
       print(f"Fine added for Seatbelt Rs {fine}")
    
    truckspeed = int(input("Enter the speed of the truck: "))
    if truckspeed > 60:
        finespeed=3000
        eligible = True
        print(f"Speed Fine added Rs {finespeed}")
    total=fine+finespeed
    if eligible:
        print(f"Your total fine is Rs {total}")
    else:
        print("You have no chaalaan")
    sys.exit()
speed=int(input("Enter the speed of the vechile"))
if(speed>80): 
    speedfine=2000
    eligble=True
    print("speed fine Rs 2000")
total=fine+speedfine

if(eligble):
    
    print(f"Your total fine is {total}")
else:print("You have no chaalaan ")