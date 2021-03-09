test_list= [
      {"first":"1"},
      {"second": "2"},
      {"third": "1"}, 
      {"four": "5"},       
      {"five":"5"}, 
     {"six":"9"},
      {"seven":"7"}]


aar=set(i for dic in test_list for i in dic.values())
print(aar)
