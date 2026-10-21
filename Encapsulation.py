class bankaccount:
    def __init__(self,name,account_id,balance,):
        self.name=name
        self._account_id=account_id #proetcted
        self.__balance=balance #private
    def get_balance(self):#getter
        return self.__balance
    def upadate_balance(self,new):
        self.__balance=new
        return self.__balance
    




a1=bankaccount("Ashutosh Khare",2345,"1Billion dollar")
a2=bankaccount("Sunidhi Khare",7898,"2 billion dollar")
print(a1.name,a1._account_id)
bankaccount.get_balance(a1)
a=bankaccount.get_balance(a2)
b=bankaccount.upadate_balance(a1,"3 billion dollars")
print(a,b)



