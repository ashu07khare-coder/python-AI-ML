name=input("Enter your full name=")
name.strip()
name1=name.lower()
print(name1)
a=len(name)
if(a==0):
    print('name is empty')
else:
    print(name[0],name[(a-1)])    


