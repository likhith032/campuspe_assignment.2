age = int(input("Enter age: "))
day = input("Enter day of week: ").strip().lower()
tickets = int(input("Enter number of tickets: "))

if age < 3:
    base_price = 0
    category = "Free"
elif age <= 12:
    base_price = 150
    category = "Child"
elif age <= 59:
    base_price = 300
    category = "Adult"
else:
    base_price = 200
    category = "Senior"

if day in ["friday", "saturday", "sunday"]:
    discount_rate = 0.20
else:
    discount_rate = 0

discount_amount = base_price * discount_rate
price_after_discount = base_price - discount_amount
total_amount = price_after_discount * tickets

print("\n====== TICKET BILL ======")
print("Category            :", category)
print("Base Price          : ₹", base_price)
print("Discount per Ticket : ₹", f"{discount_amount:.2f}")
print("Price After Discount: ₹", f"{price_after_discount:.2f}")
print("Number of Tickets   :", tickets)
print("Total Amount        : ₹", f"{total_amount:.2f}")
print("==========================")