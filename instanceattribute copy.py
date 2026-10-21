class mobile:
    storage_type="UFS 3.8"
    def __init__(self,RAM,storage_capacity):
        self.RAM=RAM
        self.storage_capacity=storage_capacity
    def get_info(self):#instance method
        print(f"RAM={self.RAM}, storage_capacity={self.storage_capacity},")    
m1=mobile("8gb","128gb")  
m2=mobile("12gb","256gb")
print(m1.RAM,m1.storage_type)
print(m2.RAM,m2.storage_type)
m1.get_info()
m2.get_info()
