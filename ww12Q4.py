def is_power_of_three(n):
    if n <= 0:
        return False
    while n % 2 == 0:
        n //= 2
    return n == 1
   
n = int(input())

if is_power_of_three(n):
    print("True")
else:
    print("False")
