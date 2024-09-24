def find_consecutive(s):

    char1 = None
    for char in s:
        if char == char1:
            return char
        char1 = char
    return None
s1 = "12345673338910111213141516171820212223"
result = find_consecutive(s1)
print(result)
