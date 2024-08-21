print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_calc = bill * (1+ tip /100)
bill_perperson = tip_calc / people
final_amount = round(bill_perperson,2)
print(f"Each person have to pay ${final_amount}")
