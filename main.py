import re

def value(r):
    if r == 'I': return 1
    if r == 'V': return 5
    if r == 'X': return 10
    if r == 'L': return 50
    if r == 'C': return 100
    if r == 'D': return 500
    if r == 'M': return 1000
    return -1

def number(str):
    result = 0
    i = 0

    while i < len(str):
        s1 = value(str[i])
        if i + 1 < len(str):
            s2 = value(str[i + 1])
            if s1 >= s2:
                result = result + s1
                i = i + 1
            else:
                result = result + s2 - s1
                i = i + 2
        else:
            result = result + s1
            i = i + 1
    return result


def RumanNumeralValidation(userInput):
    return bool(re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", userInput))


print("Please enter a Roman Numeral: ")
userInput = input()
if RumanNumeralValidation(userInput):
    print("The number is: ", number(userInput))
else:
    print("Invalid Roman Numeral")
