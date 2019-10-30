'''Define a function reverse()that computes the reversal
of a string. For example, reverse("I am testing")
should return the string "gnitset ma I".
'''

'''def reverse(passed_string):
    return passed_string[::-1]

print(reverse("python"))'''

def reverse(input_str):
    s1 = ""
    for i in input_str:
        s1 = i + s1  
    return s1

string = "i am testing"
print(reverse(string))

