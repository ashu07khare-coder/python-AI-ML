class students:
    def __init__(self,name,fees,private_id):
        self.name=name
        self._fees=fees#protected
        self.__priavte_id=private_id#private
    def get_info(self):#getter
        print(self.__priavte_id)
        return self.__priavte_id
        
    
    
    def update(self,new_fees):#update
        self._fees=new_fees
s1=students("Ashutosh",10_00000,2345)
s2=students("Suhani",20_000,2378)    
s3=students("Aman",30_000,2347)
print(s1.name,s1._fees)    
students.update(s1,7_00000)
print(s1._fees)
students.get_info(s1)
students.get_info(s2)
students.get_info(s3)


    