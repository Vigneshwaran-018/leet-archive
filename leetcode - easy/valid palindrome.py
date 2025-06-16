
import string

s=" "

s=''.join(char for char in s if char not in string.punctuation and not char.isspace())

s=s.lower()

if s==s[::-1]:
    print("true")
