sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
sub4 = float(input("Enter marks for Subject 4: "))
sub5 = float(input("Enter marks for Subject 5: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5

if percentage >= 90:
    grade = "A+ (Outstanding)"
elif percentage >= 80:
    grade = "A (Excellent)"
elif percentage >= 70:
    grade = "B (Good)"
elif percentage >= 60:
    grade = "C (Average)"
elif percentage >= 50:
    grade = "D (Pass)"
else:
    grade = "F (Fail)"

if sub1 >= 40 and sub2 >= 40 and sub3 >= 40 and sub4 >= 40 and sub5 >= 40:
    result = "Pass"
else:
    result = "Fail"

print("\n========== RESULT SUMMARY ==========")
print("Marks Obtained")
print("------------------------------------")
print("Subject 1 :", sub1)
print("Subject 2 :", sub2)
print("Subject 3 :", sub3)
print("Subject 4 :", sub4)
print("Subject 5 :", sub5)
print("------------------------------------")
print("Total      :", total, "/ 500")
print("Percentage :", f"{percentage:.2f}%")
print("Grade      :", grade)
print("Result     :", result)
print("====================================")