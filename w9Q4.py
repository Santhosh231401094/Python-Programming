def automorphic(num):
    if num < 0:
        return "Invalid input"
    
    square = num ** 2
    num_str = str(num)
    square_str = str(square)
    
    if square_str.endswith(num_str):
        return "Automorphic"
    else:
        return "Not Automorphic"
