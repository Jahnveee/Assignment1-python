#Write a python program that removes all punctuation from a given string
def remove_punctuation(s):
    result = ""
    for char in s:
        if char.isalnum() or char.isspace():
            result += char
    return result

s = 'Hello!! I am JAHNVEE_Srivastava!!'
print(remove_punctuation(s))