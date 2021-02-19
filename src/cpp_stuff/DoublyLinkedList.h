#ifndef DOUBLYLINKEDLIST_H
#define DOUBLYLINKEDLIST_H

#include <iostream>

using namespace std;


template <typename T>
class Node {
private:
	T data;
	Node next;
    Node prev;

public:
    Node() {
        this->next = nullptr;
        this->prev = nullptr;
    }
	Node(T data) {
		this->data = data;
		this->next = nullptr;
        this->prev = nullptr;
	}
};


template <typename T>
class DoublyLinkedList {
private:
	Node<T> head;
    Node<T> tail;
	int size;

public:
	DoublyLinkedList() {
		this->head = nullptr;
        this->tail = nullptr;
		this->size = 0;
	}

    int length() {
		return this->size;
	}

	void push(Node<T> node) {
        if (this->size == 0){
            this->head = &node;
            this->tail = &node;
        }
        else{
            this->tail.prev.next = &node;
            node.prev = &(this->tail.prev);
            node.next = this->tail;
            this->tail.prev = &node;
        }
		this->size++;
	}

    Node<T> pop() {
        Node<T> curr = this->head;
        return curr;
    }

    void insert(Node<T> node) {
        Node<T> curr = this->head;
    }

    void remove(Node<T> node) {
        Node<T> curr = this->head;
    }

	void show() {
		Node<T> curr = this->head;
		while (curr.next != nullptr) {
			cout << curr.data << " ";
			curr = curr.next;
		}
		cout << endl;
	}
};

#endif
