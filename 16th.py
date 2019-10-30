'''Write a program that maps a list of words into a list
of integers representing
the lengths of the correponding words'''


def length_of_list(lst):
    length = []
    for i in lst:
        length.append(len(i))
    return length
lst = ['abc', 'abcde', 'hello world','pyhton']
print(length_of_list(lst))
