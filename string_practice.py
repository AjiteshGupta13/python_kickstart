str = "I like this program very much"
str2 = str.split(" ")
str3 = " "
for item in str2:
    str3 = item+" "+ str3

#print(str3)


def rev_sentence():
    str1 = "I like books"
    rev = ""
    list = str1.split()
    length = len(list) - 1
    while length >= 0:
        rev += list[length]+" "
        length-=1
    print(rev)

rev_sentence()



bound_by = "[[]]"
tag_name = "tag"
var1 = bound_by[0:2]
var2 = bound_by[2:4]
var3 = var1 + tag_name + var2
print(var3)
