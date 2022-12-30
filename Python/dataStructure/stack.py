class Stack:
    def __init__(self):
        self._data = []

    def push(self, data):
        self._data.append(data)

    def pop(self):
        return self._data.pop()

    def size(self):
        return len(self._data)

    def empty(self):
        if (len(self._data)) == 0:
            return 1
        else:
            return 0
    
    def top(self):
        return self._data[-1]