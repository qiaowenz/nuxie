students = []
def get_student_titlecase():
    students_titlecase=[]
    for student in students:
        students_titlecase=student["name"].title()
    return students_titlecase

def print_student_titlecase():
    students_titlecase=[]
    students_titlecase=get_student_titlecase()
    print(students_titlecase)

def add_student(name, student_id=332):
    student={"name":name, "student_id":student_id}
    students.append(student)

student_list = get_student_titlecase()
student_name = input("Enter student name:")
student_id = input("Enter student id:")

add_student(student_name, student_id)
print_student_titlecase()

