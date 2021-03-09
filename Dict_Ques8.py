index=1
new1=[]
new2=[]
while index<=10:
    user1=input("enter a name : ")
    user2=int(input("enter marks : "))
    new2.append(user1)
    new1.append(user2)
    index=index+1
    
aar=dict(zip(new2,new1))
print(aar)
