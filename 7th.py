'''
Define a function is_palindrome()that recognizes
palindromes (i.e. words that look the same written
backwards). For example, is_palindrome("radar")
should return True
'''
'''
def is_palindrome(passed_string):
    return passed_string==passed_string[::-1]

print(is_palindrome("121"))
print(is_palindrome("aba"))
'''
def is_palindrome(passed_string):
 s1 = ""
 for i in passed_string:
        s1 = i + s1  
 return passed_string==s1
print(is_palindrome("12121"))
print(is_palindrome("abaa"))
