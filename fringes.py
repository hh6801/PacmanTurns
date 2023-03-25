import queue

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


class Queue:
    def __init__(self):
        self.items = queue.Queue()

    def push(self, item):
        self.items.put(item)

    def pop(self):
        return self.items.get()

    def is_empty(self):
        return self.items.empty()


class PriorityQueue:
    def __init__(self):
        self.items = queue.PriorityQueue()

    def push(self, item, priority):
        self.items.put((priority, item))

    def pop(self):
        return self.items.get()[1]

    def is_empty(self):
        return self.items.empty()