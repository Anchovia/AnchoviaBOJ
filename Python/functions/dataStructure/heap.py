class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def get_min(self):
        if len(self.heap) > 0:
            return self.heap[0]
        
    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        elif len(self.heap) == 1:
            return self.heap.pop()
        else:
            min_value = self.heap[0]
            self.heap[0] = self.heap.pop()
            self.heapify_down(0)
            return min_value
        
    def heapify_down(self, i):
        while self.left_child(i) < len(self.heap):
            min_child = self.left_child(i)
            if self.right_child(i) < len(self.heap) and self.heap[self.right_child(i)] < self.heap[min_child]:
                min_child = self.right_child(i)
            if self.heap[i] > self.heap[min_child]:
                self.heap[i], self.heap[min_child] = self.heap[min_child], self.heap[i]
                i = min_child
            else:
                break