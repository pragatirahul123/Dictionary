dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
dic4 = {}

for index in (dic1,dic2,dic3):
    dic4.update(index)
print(dic4)




**********************************************************************************



dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
dic4 = {}

for index in (dic1,dic2,dic3):
    for j in index.keys():
        dic4[j]= dic4.get(j,0)+ index[j]
print(dic4)

