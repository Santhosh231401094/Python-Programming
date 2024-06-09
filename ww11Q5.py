def perform_division():
    try:
        num1 = input().strip()
        num2 = input().strip()
        
        if not num1 or not num2:
            raise ValueError("Empty input")
        
        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            raise ValueError("Non-numeric input provided.")
        
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide or modulo by zero.")
        
        division_result = num1 / num2
        print(division_result)
        
    except ValueError as ve:
        print(f"Error: {ve}")
    except ZeroDivisionError as zde:
        print(f"Error: {zde}")

# Call the function
perform_division()
