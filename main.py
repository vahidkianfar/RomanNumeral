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

print("Integer form of Roman Numeral is")
print(number("MIMXXX"))
