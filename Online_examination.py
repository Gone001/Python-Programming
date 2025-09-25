name =input("Enter you name :")
limit=50
nums={}
for var in ["Correct", "Incorrect", "Unattempted"]:
    while True:
        val = int(input(f"Enter the no of {var} (max {limit}): "))
        if val > limit:
            print(f"{var}={val} Not possible ! Remaining limit = {limit}")
            exit()
        else:
            nums[var] = val
            limit -= val
            break
        
correct=nums["Correct"]*4
incorrcet=nums["Incorrect"]*-1
unattempted=nums["Unattempted"]*0
print(f"{correct} for Correct ")
print(f"{incorrcet} for incorrect ")
total=correct+incorrcet+unattempted
print(f"Total marks :{total}")
if total>=180:
    print(f"Excellent {name}")
elif 120<=total<=179:
    print(f"Good {name}")
elif 60<total<=119:
    print(f"Avergae {name}")
else :print("Fail")
