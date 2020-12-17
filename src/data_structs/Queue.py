"""
Queue data structure implementing list
"""

class Queue(object):
    def __init__(self):
        self.size = 0
        self.elements = []
    
    def enqueue(self, element):
        self.elements.append(None)
        self.size += 1
        sze = self.size
        for i in range(1, sze):
            self.elements[sze - i] = self.elements[sze - i - 1]
        self.elements[0] = element
    
    def dequeue(self):
        e = self.elements[self.size - 1]
        self.elements.remove(e)
        self.size -= 1
        return e
    
    def front(self):
        return self.elements[self.size - 1]
    
    def back(self):
        return self.elements[0]
    
    def show(self):
        for e in self.elements:
            print(f"{e}", end=" ")
        print()


q = Queue()

q.enqueue(1)
q.enqueue(5)
q.enqueue(10)
q.show()
print(f"f={q.front()}")
q.dequeue()
q.show()
