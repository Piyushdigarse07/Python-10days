def func_gen(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        

        else:
            result += char

    return result

encoded_string = func_gen("Piyush Digarse", 3)
print(encoded_string)  
