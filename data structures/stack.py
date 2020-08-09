import numpy as np


class stackClass:
    def __init__(self, max):
        self.max = max;
        self.a = np.array('i', max)
        self.top = -1

    def push(self, item):
        if self.top == self.max - 1:
            print("Stack overflow")
        else:
            self.a[self.top] = item
            self.top += 1

    def pop(self):
        if self.top == -1:
            return -99999
        else:
            item = self.a[self.top]
            self.top -= 1
            return item

    def display(self):
        print("Values are: ")
        if self.top == -1:
            print("Stack empty")
        else:
            for i in range(self.top):
                print(self.a[i], end=" ")

    def peek(self):
        if self.top == -1:
            print("Stcak empty")
        else:
            return self.a[self.top]
