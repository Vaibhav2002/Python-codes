import numpy as np

s = np.array([["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]])


def initialize():
    global s
    s = np.array([["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]])


def insert(ch, x, y):
    global s
    if s[x][y] != '-':
        print("Position already marked")
        exit()
    s[x][y] = ch


def check(ch):
    global s
    flag1 = False
    if s[0][0] == ch and s[0][1] == ch and s[0][2] == ch:
        flag1 = True
    elif s[1][0] == ch and s[1][1] == ch and s[1][2] == ch:
        flag1 = True
    elif s[2][0] == ch and s[2][1] == ch and s[2][2] == ch:
        flag1 = True
    elif s[0][0] == ch and s[1][0] == ch and s[2][0] == ch:
        flag1 = True
    elif s[0][1] == ch and s[1][1] == ch and s[2][1] == ch:
        flag1 = True
    elif s[0][2] == ch and s[1][2] == ch and s[2][2] == ch:
        flag1 = True
    elif s[0][0] == ch and s[1][1] == ch and s[2][2] == ch:
        flag1 = True
    elif s[0][2] == ch and s[1][1] == ch and s[2][0] == ch:
        flag1 = True
    return flag1


def display():
    global s
    for i in range(0, 3):
        for j in range(0, 3):
            print(s[i][j], end=" ")
        print()
