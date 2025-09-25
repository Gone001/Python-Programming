name =input("Enter your name ")
physics=int(input("Enter the marks of Physics :"))
chemistry=int(input("Enter the marks of Chemistry :"))
maths =int(input("Enter the marks of Maths"))
total=physics+chemistry+maths
average =total/3
print(f"Your total marks : {total}")
print(f"Your Average marks : {average:.2f}")

# Admission criteia 
if average >= 70 and physics >= 60 and chemistry >= 60:
    if 60 <= maths < 90:
        print(f"Congratulations {name}, you are eligible for the admission.")
    elif maths >= 90:
        print(f"Congratulations {name}, you are eligible for the admission.\nYou have got Maths Special Quota.")
    else:  # maths < 60
        print(f"Your Maths marks are very low.\nYou are not eligible for the admission.")
else:
    # Check which subject is low
    if physics < 60:
        print(f"Your Physics marks are very low.\nYou are not eligible for the admission.")
    elif chemistry < 60:
        print(f"Your Chemistry marks are very low.\nYou are not eligible for the admission.")
    else:
        print(f"Your overall marks ({average:.2f}) are very low.\nYou are not eligible for the admission.")