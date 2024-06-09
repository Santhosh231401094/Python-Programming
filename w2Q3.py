meal_cost = float(input())
tax_amount = meal_cost * 0.05
tip_amount = meal_cost * 0.18
total_cost = meal_cost + tax_amount + tip_amount
print(f"The tax is {tax_amount:.2f} and the tip is {tip_amount:.2f}, making the total {total_cost:.2f}")
