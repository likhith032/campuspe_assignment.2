a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("\nResults:")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} ^ {b} = {a ** b}")
print(f"{a} * {b} = {a * b}")
if b != 0:
    print(f"{a} / {b} = {a / b:.2f}")
else:
    print("Division by zero is not allowed")
    if b != 0:
        print(f"{a} % {b} = {a % b}")
    else:
        print("Modulus not possible (division by zero)")