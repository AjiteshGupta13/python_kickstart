




#module 5
string = "python"
length = len(string)
print(length)

string = "hello world"
uppercase = string.upper()
print(uppercase)

string = "hello world"
lowercase = string.lower()
print(lowercase)

string = " Learn Python "
space = string.strip()
print(space)

#idk 5

def contvowels():
    word = input("Enter a word: ")
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for char in word:
        if char in vowels:
            count += 1
        else:
            count += 0
    print("The number of vowels is:", count)

python = "python is fun"
new_python = string.replace(" ", "-")
print(new_python)

#idk 8

def reverse_string(word):
    result = ""
    i = len(word) - 1
    while i >= 0:
        result += word[i]
        i -= 1
    return result

text = "python"
print(reverse_string(text))

def reverse_string(word):
    result = ""
    i = len(word) - 1
    while i >= 0:
        result += word[i]
        i -= 1
    return result

sentence = "Python is fun"
word = sentence.split()

words = ["Python", "is", "fun"]
newword = " ".join(words)
print(newword)

# idk 12

string = "Python Programming"
start = 7
end = 18
string2 = string[start:end]
print(string2)

#idk 14 - 15

def capitalize_words(sentence):

    return sentence.title()
sentence = "python programming is fun"
output_sentence = capitalize_words(sentence)
print(output_sentence)


text = input("Enter something: ")
words = text.split()
reversed_words = [word[::-1] + 'h' for word in words]
output = " ".join(reversed_words)
print(output)


text = input("Enter a string: ")
if text.isdigit():
    print("The string contains digits only.")
else:
    print("The string does not contain digits only.")

string = "I love Java"
old_substring = "java"
new_substring = "python"
updated_string = string.replace(old_substring, new_substring)
print(updated_string)

for number in range(1, 31):
    if number % 4 == 0:
        print(number)




