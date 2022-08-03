class my_queue:
    def __init__(self):
        self.queue = []

    def push(self, data):
        self.queue.append(data)

    def pop(self):
        return self.queue.pop(0) if len(self.queue) > 0 else None

    def peek(self):
        return self.queue[0] if len(self.queue) > 0 else None