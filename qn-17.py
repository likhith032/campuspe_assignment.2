value = input("Enter word/number: ")

original = value

lower_value = value.lower()

reversed_value = lower_value[::-1]
print("\nStep-by-step verification:")
print("Original:", original)
print("Lowercase:", lower_value)
print("Reversed:", reversed_value)

if lower_value == reversed_value:
    print("Result: PALINDROME")
else:
    print("Result: NOT A PALINDROME")