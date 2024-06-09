def calculate_average_marks():
    import sys
    input = sys.stdin.read
    
    # Read all input lines
    data = input().strip().split('\n')
    
    # Number of students
    N = int(data[0].strip())
    
    # Column headers
    headers = data[1].strip().split()
    
    # Find the index of the 'MARKS' column
    marks_index = headers.index("MARKS")
    
    # Initialize sum of marks
    total_marks = 0
    
    # Read each student's data and accumulate marks
    for i in range(2, 2 + N):
        student_data = data[i].strip().split()
        marks = int(student_data[marks_index])
        total_marks += marks
    
    # Calculate the average marks
    average_marks = total_marks / N
    
    # Print the result formatted to two decimal places
    print(f"{average_marks:.2f}")

# Call the function to execute
calculate_average_marks()
