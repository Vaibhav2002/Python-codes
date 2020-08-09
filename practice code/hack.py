import hashlib
import string
s=input("Enter hash form")
s.encode('utf-8')
g=open(indian-passwords,'r')
line = g.readline( )
wordlist = string.split(line)
for word in wordlist:
    if hashlib.md5(word).digest()==s:
        print(word)
