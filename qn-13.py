count = int(input("How many numbers? "))

total = 0
maximum = None
minimum = None

for i in range(1, count + 1):
    num = float(input(f"Enter number {i}: "))
    
    total += num
    
    if maximum is None or num > maximum:
        maximum = num
        
    if minimum is None or num < minimum:
        minimum = num

average = total / count

print("\n===== RESULT =====")
print("Sum     :", total)
print("Average :", average)
print("Maximum :", maximum)
print("Minimum :", minimum)
