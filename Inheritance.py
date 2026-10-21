class family:
    mother="Manju Khare"
    father="Neeraj Khare"
    def __init__(self,name,pocket_money):
        self.name=name
        self.pocket_money=pocket_money
    def chane_pocketmoney(self,new_money):
        self.pocket_money=new_money
        

class ashu(family):
   def __init__(self,car_name):
       self.car_name=car_name
class sunidhi(family):
       def __init__(self,car_name):
           self.car_name=car_name
a=ashu("BMW")
b=ashu("Bugatti")           
c=sunidhi("Aston martin")
d=sunidhi("Ferrari")
print(c.car_name,c.mother,c.father)

