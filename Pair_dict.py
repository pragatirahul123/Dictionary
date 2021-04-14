n1=int(input("enter a any key : "))
list1=[1,2,3,4,5]
list1.append(n1)
list2=["mona","sona","neha","hina","zeha"]
print(list1)
i=0
d={}
while i<len(list2):
    d[list1[i]]=list2[i]
    i=i+1
print(d)
