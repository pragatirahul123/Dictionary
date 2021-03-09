1.Difference between dict.items() and dict.iteritems() in Python?

Ans:
    dict.items(): returns a copy of the dictionary’s list in the form of (key, value) tuple pairs, which is a (Python v3.x) version, and exists in (Python v2.x) version.
    dict.iteritems(): returns an iterator of the dictionary’s list in the form of (key, value) tuple pairs. which is a (Python v2.x) version and got omitted in (Python v3.x) version.




Q2. Python program to print the dictionary in a table format?
my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}  
for var in zip(*([i] + (j)  
        for i, j in my_dict.items())): 
      
    print(*var, " ")



Q3. How to find length of dictionary values?
dict = {'Name': 'Manni', 'Age': 7, 'Class': 'First'}
print ( len (dict))


Q6. Split dictionary keys and values into separate lists?
Ans: var = {'a' : 'akshat', 'b' : 'bhuvan', 'c': 'chandan'} 
keys = var.keys() 
values = var.values() 
print ("keys : ", str(keys)) 
print ("values : ", str(values)) 


Q7. Convert a set into a dictionary?
Ans:
list_keys = {1,2,3,4}
#print(type(list_keys))
new_dict = dict.fromkeys(list_keys,'Mon')
print(new_dict)
print(type(new_dict))


Q8. Get key with maximum value in Dictionary?
a_dictionary = {"a": 1, "b": 27, "c": 23,"d":7}

max_key = max(a_dictionary, key=a_dictionary.get)
print(max_key)

# values=a_dictionary.values()
# max_value=max(values)
# print(max_value)


10.Remove spaces from dictionary keys?
student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
student_dict = {x.translate({32: None}): y for x, y in student_list.items()}
print("New dictionary: ",student_dict)


 



	
