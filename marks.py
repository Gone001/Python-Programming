sub1=float(input("Enter first subject marks: "))
sub2=float(input("Enter second subject marks: "))
sub3=float(input("Enter third subject marks: "))
sub4=float(input("Enter fourth subject marks: "))
sub5=float(input("Enter fifth subject marks: "))
total_marks = sub1 + sub2 + sub3 + sub4 + sub5
average_marks = total_marks / 5
print("Total Marks: ", total_marks)
print("Average Marks: ", int(average_marks))
if average_marks >= 90:
    print("Grade: A")
elif( average_marks >= 80):
    print("Grade: B")
elif( average_marks >= 70):
    print("Grade: C")
elif( average_marks >= 60):
    print("Grade: D")
elif( average_marks >= 50):
    print("Grade: E")
else:
    print("failed")