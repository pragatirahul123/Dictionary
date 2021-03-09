dict = {
    'a':50, 
    'b':58,
    'c': 56,
    'd':40,
    'e':100, 
    'f':20
    } 

new=[]
new1=[]
for i in dict.values():

    new.append(i)
for k in dict.keys():
    new1.append(k)
    
index=0
var=0
var1=0
while index<len(new):
    if new[index]>var:
        var=new[index]
        var1=new1[index]
    
    index=index+1
    a=[]
    a.append(var1)
#print(var)
print(a)

