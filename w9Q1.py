def checkUgly(n):
    if n <= 0:
        return "not ugly"  # Negative numbers and zero are not considered ugly
    for prime in [2, 3, 5]:
        while n % prime == 0:
            n /= prime
    if n == 1:
        return "ugly"
    else:
        return "not ugly"
