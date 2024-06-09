initial_amount = float(input())
interest_rate = 4
years = [1, 2, 3]

for year in years:
    balance = initial_amount * ((1 + interest_rate / 100) ** year)
    print(f"Balance as of end of Year {year}: ${balance:.2f}.")
