from termcolor import colored
import math as m
p=float(input(colored("Enter principal amount",'green')))
r=float(input(colored("Enter rate of interest",'red')))
t=int(input(colored("Enter time",'blue')))
print(p*m.pow(1+r/100,t))
