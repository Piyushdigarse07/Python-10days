def duplicate_letters(sentence):
    words = sentence.split()
    for word in words:
        if len(word) != len(set(word)):
            return True
    return False
sentence1 = "This is a sentence"
print(duplicate_letters(sentence1))

sentence2= "My name is Piyush"
print(duplicate_letters(sentence2))
