class teachers:
    start_time="9 am"
    end_time="4 pm"
    def __init__(self,salary,subject):
        self.salary=salary
        self.subject=subject
class student:
    start_time="10 am"
    end_time="3 pm"
    def __init__(self,fees,subject):
        self.fees=fees
        self.subject=subject
class TA(teachers,student):
    def __init__(self,fees,subject,salary):
        super().__init__(salary,subject)
        self.fees=fees
ta1=TA(50_000,"python",20_000)
print(ta1.fees,ta1.subject,ta1.salary)       

