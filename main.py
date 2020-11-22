my_student = {
"name " : "tabish",
"grades": [10, 23, 50]

}

def average_sum(student):
   return sum(student['grades']) / len(student['grades'])

class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades
    def average(self):
        return sum(self.grades) / len(self.grades)

student_one = Student('tabish',[55,66,77,888])
student_two = Student('aziz' ,[44,55,66,77])    

print(student_two.name)
print(student_two.average())