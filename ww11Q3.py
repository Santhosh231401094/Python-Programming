def perform_operations():
    try:
        num1 = input().strip()
        num2 = input().strip()
        
        if not num1 or not num2:
            raise ValueError("Empty input")
        
        # Attempt to convert inputs to float
        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("Error: Non-numeric input provided.")
            return
        
        # Perform division and modulo
        try:
            division_result = num1 / num2
            modulo_result =round( num1 % num2)
            print(f"Division result: {division_result}")
            print(f"Modulo result: {modulo_result}")
        except ZeroDivisionError:
            print("Error: Cannot divide or modulo by zero.")
        
    except ValueError as ve:
        print(f"Error: {ve}")

# Call the function
perform_operations()

