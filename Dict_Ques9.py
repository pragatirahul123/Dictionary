text="MISSISSIPPI"
new = []
index=0
while index<len(text):
    new.append(text[index])
    index=index+1
#print(new)
int=0
new1=[]
while int<len(new):
    count=0
    bar=[]
    jar=0
    while jar < len(new):
        if new[int]==new[jar]:
            count=count+1
        jar=jar+1
    bar.append(new[int])
    bar.append(count)
    int=int+1
    if bar not in new1:
        new1.append(bar)
#print(new1)
var=new1
char=dict(var)
print(char)



