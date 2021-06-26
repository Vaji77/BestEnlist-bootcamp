# Checking a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)
import re

def string_contain(string):
    print("String:", string)
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)


print(string_contain("ABC123abc"))
print(string_contain("abd@$123"))


# Matching word containing ab
def match_word(word):
    print("Word:", word)
    pattern = '\w*ab\w*'
    if re.search(pattern, word):
        print("Match found")
    else:
        print("Match not found")


match_word("Python Internship")
match_word("bootcamp")


# Checking number at the end of a word/sentence
def check_num(string):
    print("String:", string)
    check = re.compile(r".*[0-9]$")
    if check.match(string):
        return "The string is ending with a number"
    else:
        return "The string is not ending with a number"


print(check_num('ASDFGH'))
print(check_num('QWERTY123'))
print(check_num('@345XYZ6'))


# Searching the numbers (0-9) of length between 1 to 3 in a string
str_1 = "The basket has 123 apples 12 oranges and 1 grapes"
print("String:", str_1)
result = re.finditer(r"([0-9]{1,3})", str_1)
print("Number of length 1 to 3")
for i in result:
    print(i.group(0))


# Matching a string that contains only uppercase letters
def string_match(string):
    print("String:", string)
    print(bool(re.match('^[A-Z]+$', string)))


string_match("Stay Home")
string_match("SAFE")
string_match("TODAY123")