dict =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}



total = 0
for var in dict:
    var = dict[var]
    count = len(var)
    total = total+ count

print(total)



