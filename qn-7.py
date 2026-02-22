while True:
    print("\n====== TEMPERATURE CONVERTER ======")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    choice = input("Select an option (1-7): ")

    if choice == "1":
        c = float(input("Enter Celsius: "))
        print("Result:", (c * 9/5) + 32, "°F")

    elif choice == "2":
        f = float(input("Enter Fahrenheit: "))
        print("Result:", (f - 32) * 5/9, "°C")

    elif choice == "3":
        c = float(input("Enter Celsius: "))
        print("Result:", c + 273.15, "K")

    elif choice == "4":
        k = float(input("Enter Kelvin: "))
        print("Result:", k - 273.15, "°C")

    elif choice == "5":
        f = float(input("Enter Fahrenheit: "))
        print("Result:", (f - 32) * 5/9 + 273.15, "K")

    elif choice == "6":
        k = float(input("Enter Kelvin: "))
        print("Result:", (k - 273.15) * 9/5 + 32, "°F")

    elif choice == "7":
        print("Program Ended")
        break

    else:
        print("Invalid choice. Try again.")