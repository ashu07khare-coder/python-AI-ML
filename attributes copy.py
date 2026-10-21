class student:
    sub="python"
    college_name="Alta school of technology"
    h=6.67
    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa
        self.h=6.68
stu1=student("Ashu", 3.9)
stu2=student("Mohit",9.0) 
stu3=student("Arya",8.5)
print(student.college_name)
print(stu1.name,stu2.name,stu3.name)
print(stu1.college_name,student.college_name)
print(stu1.h,student.h)


