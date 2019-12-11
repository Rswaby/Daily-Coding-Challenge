'''
Stack using an Array

'''

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, element):
        self.stack.append(element)
    def pop(self):
        return self.stack.pop
    def peep(self):
        return self.stack[-1]