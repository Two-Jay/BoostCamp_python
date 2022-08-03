class my_stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        return self.stack.pop() if len(self.stack) > 0 else None
    
    def peek(self):
        return self.stack[-1] if len(self.stack) > 0 else None