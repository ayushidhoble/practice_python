'''
Write a function filter_long_words()that takes
a list of words and an integer
n and returns the list of words that are longer than n
'''


def filter_long_words(list,n):
    i = []
    for x in list:
        if len(x) > n:
            i.append(x)
    return i

ab = ['abc','defgh','pqrstuvw','','abdghaatafd']
print(filter_long_words(ab,8))
