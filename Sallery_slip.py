name=input("Enter the name of the employee :")
take=int(input(f"Enter the sallery of{name} :"))
HRA=0.20*take
DA=0.10*take
PF=0.12*take
Gross_sallery=take+HRA+DA
net_sallery=Gross_sallery-PF
print(f"House Rent Allowence  of {name} is {PF}")
print(f"Deraness allowance of  {name} is {PF}")
print(f"Pvoident fund of {name} is {PF}")
print(f"Gross sallery of {name} is {Gross_sallery}")
print(f"Net sallery of {name} is {net_sallery}")
if(net_sallery>=80000):
    print(f"{name} is a High Earner")
elif(50000<=net_sallery<=80000):
    print(f"{name} is a Mid Earner")
else:print(f"{name} is a low Earner")
