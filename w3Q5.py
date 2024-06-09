year = int(input())
animals = ['Rat', 'Ox', 'Tiger', 'Hare', 'Dragon', 'Snake', 'Horse', 'Sheep', 'Monkey', 'Rooster', 'Dog', 'Pig']
print(f"{year} is the year of the {animals[(year - 4) % 12]}.")


