'''
Write a function find_longest_word()that takes a
list of words and returns the
length of the longest one
'''
def find_longest_word(lst):  
   e = []  
   for n in lst:  
        e.append((len(n),n))  
   e.sort()  
   return e[-1]  
  
print(find_longest_word(["pyhton", "ruby", "java"]))

