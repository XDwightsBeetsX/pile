"""
Python implementation of a linked list
"""

# TODO unit test
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next_node = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insertFirst(self, new_data):
        node = Node(data=new_data)
        if self.head is None:
            self.head = node
        else:
            node.next_node = self.head
            self.head = node
        self.size += 1
    
    def insertAt(self, new_data, index):
        if index > self.size:
            raise Exception(f"[ERROR] cannot insert Node at index {index} in LinkedList with size {self.size}")
        elif index == 0:
            self.insertFirst(new_data)
        else:
            node = Node(data=new_data)
            curr = self.head
            ctr = 1
            while curr.next_node is not None and ctr < index:
                curr = curr.next_node
                ctr += 1
            node.next_node = curr.next_node
            curr.next_node = node
            self.size += 1
    
    def insertLast(self, new_data):
        node = Node(data=new_data)
        curr = self.head
        if curr.next_node is None:
            curr.next_node = node
        else:
            while curr.next_node is not None:
                curr = curr.next_node
            curr.next_node = node
        self.size += 1
    
    def remove(self, data_key):
        curr = self.head
        if self.size == 0:
            raise Exception("[ERROR] cannot remove() from LinkedList with size 0")
        else:
            while curr.next_node.data is not data_key:
                curr = curr.next_node
            if curr.next_node.data is data_key:
                curr.next_node = curr.next_node.next_node
                self.size -= 1
            else:
                raise Exception(f"[ERROR] could not find {data_key} in LinkedList to remove()")  
    
    def union(self, linkedlist):
        if self.size == 0:
            self.head = linkedlist.head
        else:
            curr = self.head
            while curr.next_node is not None:
                curr = curr.next_node
            curr.next_node = linkedlist.head
    
    def print(self):
        curr = self.head
        print(f"[LL s={self.size}]:", end=" ")
        while curr is not None:
            print(f"{curr.data}", end=" ")
            curr = curr.next_node
        print("")
