birth_year = int(input("Enter your birth year: "))
current_year = 2026  
age = current_year - birth_year
age_months = age * 12
age_days = age * 365
age_hours = age_days * 24
age_minutes = age_hours * 60
years_to_100 = 100 - age
print("\n------ AGE DETAILS ------")
print("Current Age:", age)
print("Age in Months:", age_months)
print("Age in Days (approx):", age_days)
print("Age in Hours:", age_hours)
print("Age in Minutes:", age_minutes)
print("Years until 100:", years_to_100)