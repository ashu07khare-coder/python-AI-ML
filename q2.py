sentence=input("Enter your sentence")
clean_sentence=sentence.lstrip()
s=0
l=0
u=0
for i in clean_sentence:
    if(i==" "):
        s+=1
    elif(i.isupper()):
        u+=1
    elif(i.islower()):
        l+=1
print("lowercase count=",l)  
print("Uppercase count=",u) 
print("total count=",l+u)  
print("total count exculding spaces=",(l+u)-s)  
            
