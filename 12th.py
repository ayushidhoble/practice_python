'''
The function max()from exercise 1) and the function
max_of_three()from exercise 2) will only work for
two and three numbers, respectively. But
suppose we have a much larger number of numbers,
or suppose we cannot tell in advance how many
they are? Write a function max_in_list()that takes a
list of numbers and returns the largest one
'''


lst = [] 
   
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    ele = int(input()) 
    lst.append(ele)
print(lst) 
def maximum(lst):
    lst.sort()
    return lst[-1]
print(maximum(lst))
