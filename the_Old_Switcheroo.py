import re
def encode(string):
    alphabet_low = list('abcdefghijklmnopqrstuvwxyz')
    alphabet_up = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    char_lst = list(string)
    new_string = ''
    for char in char_lst:
        if re.match(r"[a-z]", char):
            num = alphabet_low.index(char)
            new_string += str(num + 1)
        if re.match(r"[A-Z]", char):
            num = alphabet_up.index(char)
            new_string += str(num + 1)
        if re.match(r"[\W\[\]\d]", char):
            new_string += char
    return new_string


print(encode("this is my string"))
print(encode("Codewars is the best site in the world"))
print(encode("Tomorrow is going to be raining"))
print(encode(''))