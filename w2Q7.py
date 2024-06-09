age = int(input())
weight = int(input())

eligible = (age >= 18) * (weight > 40)

print(bool(eligible))
