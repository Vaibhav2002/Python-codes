s=input()
print("Palindrome" if bool(s.index(s[::-1])+1) else "not palindrome")