# Given marks of multiple students in different subjects, write a program to calculate each student’s total, average, highest score, and assign a grade.

def student_details():
    print("Welcome to student marks calculator: ")
    num_stds = int(input("Enter the number of students : "))
    students = []
    for i in range(num_stds):
        name = input(f"Enter the name of student {i + 1} : ")
        num_subs = int(input(f"Enter the number of subjects for {i + 1} : "))
        subjects = []
        for j in range(num_subs):
            sub_name = input(f"Enter the name of subject {j + 1} : ")
            marks = float(input(f"Enter the marks for {sub_name} : "))
            subjects.append((sub_name, marks))
        students.append((name, subjects))
    for student in students:
        name, subjects = student
        total = sum(marks for _, marks in subjects)
        average = total / len(subjects)
        highest_score = max(marks for _, marks in subjects)
        if average >= 90:
            grade = 'A'
        elif average >= 80:
            grade = 'B'
        elif average >= 70:
            grade = 'C'
        elif average >= 60:
            grade = 'D'
        else:
            grade = 'F'
        print(f"\n{name}'s Total: {total}, Average: {average:.2f}, Highest Score: {highest_score}, Grade: {grade}")

student_details()