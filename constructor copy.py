class student:
    def __init__(self,name,cgpa,college):
        self.name=name
        self.cgpa=cgpa
        self.college=college
    def get_cgpa(self):
        return self.cgpa

stu1=student("Alice", 3.8, "XYZ University")
stu2=student("Bob", 3.9, "ABC University")
stu3=student("Charlie", 3.7, "DEF University")
print(f"student name={stu1.name}, student cgpa={stu1.get_cgpa()}, student college={stu1.college}")
print(f"student name={stu2.name}, student cgpa={stu2.get_cgpa()}, student college={stu2.college}")
print(f"student name={stu3.name}, student cgpa={stu3.get_cgpa()}, student college={stu3.college}")
