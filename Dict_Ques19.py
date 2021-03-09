my_dict = {}
my_dict[(1,2,4)] = 8
my_dict[(4,2,1)] = 10
my_dict[(1,2)] = 12

sum = 0
for index in my_dict:
    sum=sum+my_dict[index]

print (sum)
print(my_dict) 




#output:
#30
#{(1, 2, 4): 8, (4, 2, 1): 10, (1, 2): 12}
