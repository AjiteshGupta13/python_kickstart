def converting(word):
    wordconvert = ""
    for char in word:
        if char.islower():
            wordconvert += char.upper()
        else:
            wordconvert += char.lower()
    return wordconvert




word = input("Write a word: ")

print(converting(word))


str1 = input("Enter a sentence: ")

list1 = str1.split()
print("All words:", list1)

wordsnoletter = [word for word in list1 if any(not char.isalvm pha() for char in word)]

print("Words with non-alphabet characters:", wordsnoletter)
