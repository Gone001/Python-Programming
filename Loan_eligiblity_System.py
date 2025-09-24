name=input("Enter the name of the Person :")
eligible=None
eligible1=None
eligible2=None
eligible3=None
age=int(input(f"Enter the age of the {name} :"))
if(21<=age<=60):
    eligible=True
else:eligible=False

monthly_income=int(input(f"Enter the monthly income  of the {name} :"))
if(monthly_income>=25000):
    eligible1=True
else:eligible1=False

loan=input("Do you have any existing loan : YES or NO ").strip().upper()
if(loan=="YES"):
    Existing_loan=int((input(f"Enter the existing loan amount of the {name}")))
    if(Existing_loan<=0.50*monthly_income):
        eligible2=True
    else:eligible2=False
else:print("OK")
CIBS=int(input("Enter the CIBIL score :"))
if(CIBS>=700):
    eligible3=True
else:eligible=False
print()
if(eligible and eligible1 and eligible2 and eligible3):
    print("You are eligible for the loan")
else:print("You are not eligible ")