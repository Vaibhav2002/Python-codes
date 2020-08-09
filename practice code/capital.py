from termcolor import colored

s = input("Enter string")
a = list(s.split())
for i in a:
    print(colored(i.capitalize(), 'red'), end=" ")
