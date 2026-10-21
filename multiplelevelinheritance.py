class employee:
    basic_salary=20_000
    start_time="9am"
    end_time="10 am"
class Adminstaff(employee):
    def __init__(self,name,role):
        self.name=name
        self.role=role
class accountant(Adminstaff):
    def __init__(self,name,role,salary):
        self.salary=salary
        super().__init__(name,role)
a1=accountant("Ayush","CA",50_000)
print(a1.role,a1.name,a1.salary)      

        