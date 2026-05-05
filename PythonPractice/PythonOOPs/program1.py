# Design a system using classes to manage student records with features to add, update, delete, and display students.
class Student:
    def __init__(self, name, age,grade):
        self.name = name
        self.age = age
        self.grade = grade
        
class StudentManagement:
    def __init__(self) -> None:
        self.students = []

    def add_student(self, name, age, grade):
        student = Student(name,age,grade)
        self.students.append(student)
    
    def update_Student(self, name, age=None, grade=None):
        for student in self.students:
            if student.name == name:
                if age is not None:
                    student.age = age
                if grade is not None:
                    student.grade = grade
                return
        print(f"Student with name {name} not found.")

    def delete_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                return
        print(f"Student with name {name} not found.")
    def display_students(self):
        for student in self.students:
            print(f"Name: {student.name}, Age: {student.age}, Grade: {student.grade}")

mangement = StudentManagement()
mangement.add_student("Alice",20,"A")
mangement.add_student("Bob", 21,"A+")
mangement.display_students()
mangement.update_Student("Alice", age = 21)
mangement.display_students()
mangement.delete_student("Bob")
mangement.display_students()

