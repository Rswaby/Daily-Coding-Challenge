class MaxStack:
    def __init__(self):
        self.stack = []
        self.maxvalues = []
    

    def push(self, val):
        self.stack.append(val)

        if self.maxvalues:
            self.maxvalues.append(max(val,self.maxvalues[-1]))
        else:
            self.maxvalues.append(val)
    def pop(self):
        if self.maxvalues:
            self.maxvalues.pop()
        
        return self.stack.pop()