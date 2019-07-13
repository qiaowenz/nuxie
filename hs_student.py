students=[]
class Student:
    school_name="Springhill Elementary"
    def __init__(self, name, student_id=332):
        #student = {"name": name, "student_id": student_id}
        self.name = name
        self.student_id=student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name

#xx=Student('Richard')
#print(xx)
#print(Student.school_name)
class HighschoolStudent(Student):
    school_name = "SpringHill Highschool"

    def get_school_name(self):
        return "This is a high school student"
    
    def get_name_capitalize(self):
        original_value=super().get_name_capitalize()
        return original_value +  " HS"


James=HighschoolStudent("James")
print(James.get_name_capitalize())