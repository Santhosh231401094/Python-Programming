def differenceSum(number):
    number_str = str(number)
    sum_even = 0
    sum_odd = 0
    
    for i in range(len(number_str)):
        digit = int(number_str[i])
        if i % 2 == 0:
            sum_even += digit
        else:
            sum_odd += digit
            
    return abs(sum_even - sum_odd)
