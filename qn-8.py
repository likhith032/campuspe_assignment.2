year = int(input("Enter a year: "))

if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    result = "Leap Year"
    
    if year % 400 == 0:
        reason = "Divisible by 400"
    elif year % 100 == 0:
        reason = "Divisible by 100 but also satisfies leap year rule"
    else:
        reason = "Divisible by 4 but not divisible by 100"
else:
    result = "NOT a Leap Year"
    
    if year % 4 != 0:
        reason = "Not divisible by 4"
    elif year % 100 == 0 and year % 400 != 0:
        reason = "Divisible by 100 but not divisible by 400"
    else:
        reason = "Does not satisfy leap year conditions"

print("\n=== LEAP YEAR CHECK RESULT ===")
print("Year   :", year)
print("Status :", result)
print("Reason :", reason)