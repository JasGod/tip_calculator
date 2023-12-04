import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))
bill_per_person = round((total_bill / number_of_people) + (total_bill / number_of_people) * (tip_percentage / 100), 2)
bill_per_person_dollar = locale.currency(bill_per_person, grouping=True)
print(f"Each person should pay: {bill_per_person_dollar}")