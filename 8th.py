'''
Write a function is_member()that takes a value
(i.e. a number, string, etc) x and a list of
values a, and returns True if x is a member of a,
False otherwise.(Note that this is exactly what
the in operator does, but for the sake of the
exercise you should pretend Python did not
have this operator.)
'''


def is_member(value,list_value):
#    for i in range(len(list_value)):
    for i in list_value:
        if value==i:
            return True
    return False

abc = [1,2,3,4]
print(is_member(9,abc))
print(is_member(11,abc))
