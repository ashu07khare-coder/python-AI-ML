class motorbike:
    colour="black"
    wheels="2"
    @classmethod
    def get_engine_type(cls):
       print(f"Engine type={cls.get_engine_type}")
       
    def __init__(self,engine,tank):
     self.engine=engine
     self.tank=tank
bike1=motorbike("150cc","50L")
bike2=motorbike("200cc","100L")
# print(bike1.engine,bike1.tank)
# print(bike2.engine,bike2.tank)
