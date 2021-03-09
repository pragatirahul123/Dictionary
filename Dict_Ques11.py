my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }

new=[]
for i in dict.values():
    new.append(i)

i=0
max=0
second=0
third=0
while i<len(new): 
    if new[i]>max: 
        second=max
        max=new[i] 
    elif new[i]>second:
        max != new[i]
        second=new[i]
    
    elif new[i]>third:
        second != new[i]
        third = new[i]
    i=i+1
print("first", max,"second",second)

