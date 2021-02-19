"""
Stack data structure implementing list
"""

class Stack(object):
    def __init__(self):
        self.size = 0
        self.elements = []
    
    def push(self, element):
        self.elements.append(element)
        self.size += 1
    
    def pop(self):
        e = self.elements[self.size - 1]
        self.elements.remove(e)
        self.size -= 1
        return e
    
    def show(self):
        for e in self.elements:
            print(f"{e}", end=" ")
        print()
