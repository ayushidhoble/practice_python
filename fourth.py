def vowel(char):
    #vowel = ('a','e','i','o','u')
    #vowel = "aeiou"
    vowel ={'a':True, 'e':True, 'i':True, 'o':True, 'u':True}
    if char in vowel:
        return vowel[char]
    return False

print(vowel('a'))
print(vowel('b'))
