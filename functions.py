students = []
def get_student_titlecase():
    students_titlecase=[]
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase

def print_student_titlecase():
    students_titlecase=[]
    students_titlecase=get_student_titlecase()
    print(students_titlecase)

def add_student(name, student_id=332):
    student={"name":name, "student_id":student_id}
    students.append(student)

def read_file():
    try:
        f=open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Could not read the file")

def save_file(student):
    try:
        f=open("students.txt", "a")
        f.write(student+"\n")
        f.close()
    except Exception:
        print("Could not write to the file")




student_list = get_student_titlecase()
read_file()
print_student_titlecase()
exit()
student_name = input("Enter student name:")
student_id = input("Enter student id:")
add_student(student_name, student_id)
save_file(student_name)
print_student_titlecase()

