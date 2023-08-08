print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip = bill * (percent / 100)
total = (tip + bill) / people
print(f"Each person should pay: ${round(total,2)}")
