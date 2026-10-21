class store:
    store_name="Picart"
    count=0
    def __init__(self,name,price):
        self.price=price
        self.name=name
        store.count+=1
    def get_info_(self):
        print(f"the Price of {self.name} is {self.price}")    
    @classmethod
    def count_method(cls):
        print(f"Total number of products added={cls.count}")   
        
    @staticmethod
    def discount(name,price,discount):
        final_price=price-((price*discount)/100)        
        print(f"final price of {name} is {final_price}")
p1=store("phone",40_000)  
p2=store("laptop",80_000)    
p3=store("tablet",50_000) 
p4=store("Charger",2_000)
print(store)
store.count_method()
p1.discount(p1.name,40_000,10)
p4.discount(p4.name,2000,20)
store.count_method()
store.get_info_(p2)



            