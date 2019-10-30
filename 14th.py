'''
Write a function find_longest_word()that takes a
list of words and returns the
length of the longest one
'''

def find_longest_one(lst):
    e = []
    for i in lst:
        e.append(len(i))
        e.sort()
        return e[-1]
ab = ['abc','defgh','pqrstuvw','']
print(find_longest_one(ab))
 


