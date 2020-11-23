"""
Tests for data_gen/stats
"""
import numpy as np
from src.data_structs import LinkedList as LL

# TODO test all methods

def test_LinkedList_insertLast():
    correct = True
    ll = LL.LinkedList()
    test_size = 100
    compare = [i for i in range(1, test_size + 1)]
    for i in range(1, test_size + 1):
        ll.insertLast(i)
    
    curr = ll.head
    cnt = 0
    while curr.next_node is not None:
        if curr.data != compare[cnt]:
            correct = False
        curr = curr.next_node
        cnt += 1
    if curr.data != compare[cnt]:
        correct = False
    
    assert correct
