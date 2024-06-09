def is_prime_digit(digit):
    return digit in [2, 3, 5, 7]

def christmasDiscount(orderValue):
    discount = 0
    for digit in str(orderValue):
        if is_prime_digit(int(digit)):
            discount += int(digit)
    return discount
