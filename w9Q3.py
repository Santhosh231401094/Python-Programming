def productDigits(n):
    total_sum = 0
    product = 1
    size = len(str(n))
    while n > 0:
        if size % 2 == 0:
            product *= n % 10
        else:
            total_sum += n % 10
        n = n // 10
        size -= 1
    if total_sum == 0:
        return False
    if product % total_sum == 0:
        return True
    return False
