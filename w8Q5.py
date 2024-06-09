def compute_student_statistics(student_dict):
    highest_avg_score = -1
    highest_assignment_marks = -1
    lowest_lab_marks = float('inf')
    lowest_avg_score = float('inf')
    students_with_highest_avg_score = []
    students_with_lowest_avg_score = []
    students_with_highest_assignment_marks = []
    students_with_lowest_lab_marks = []

    for student, marks in student_dict.items():
        total_marks = sum(marks)
        num_subjects = len(marks)
        avg_score = total_marks / num_subjects

        if avg_score > highest_avg_score:
            highest_avg_score = avg_score
            students_with_highest_avg_score = [student]
        elif avg_score == highest_avg_score:
            students_with_highest_avg_score.append(student)

        if avg_score < lowest_avg_score:
            lowest_avg_score = avg_score
            students_with_lowest_avg_score = [student]
        elif avg_score == lowest_avg_score:
            students_with_lowest_avg_score.append(student)

        if marks[1] > highest_assignment_marks:
            highest_assignment_marks = marks[1]
            students_with_highest_assignment_marks = [student]
        elif marks[1] == highest_assignment_marks:
            students_with_highest_assignment_marks.append(student)
        if marks[2] < lowest_lab_marks:
            lowest_lab_marks = marks[2]
            students_with_lowest_lab_marks = [student]
        elif marks[2] == lowest_lab_marks:
            students_with_lowest_lab_marks.append(student)

    return (students_with_highest_avg_score, students_with_highest_assignment_marks,
            students_with_lowest_lab_marks, students_with_lowest_avg_score)


# Input the number of students
num_students = int(input())

# Initialize student dictionary
student_dict = {}

# Input student details
for _ in range(num_students):
    student_details = input().split()
    name = student_details[0]
    marks = list(map(int, student_details[1:]))
    student_dict[name] = marks

# Compute statistics
stats = compute_student_statistics(student_dict)

# Output results
print(' '.join(sorted(stats[0])))
print(' '.join(sorted(stats[1])))
print(' '.join(sorted(stats[2])))
print(' '.join(sorted(stats[3])))
