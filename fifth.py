def sum(num):
    total = 0
    for x in num:
        total = total + x
    return total

def multiply(num):
    total = 1
    for x in num:
        total = total * x
    return total

print(sum([1,2,3,4]))
print(multiply([1,2,3,4]))
