class employee:
    basic_salary=30_000
    start_time="9 am"
    end_time="5 pm"
class teachers(employee):
    def __init__(self,subject,added_salary):
        self.subject=subject
        self.__added_salary=added_salary#private
    def get_info_salary(self):
        total_salary=(employee.basic_salary) + (self.__added_salary)
        print (total_salary)
        return total_salary
t1=teachers("python",40_000)   
print(t1.basic_salary,t1.start_time,t1.end_time)
teachers.get_info_salary(t1)


