#ifndef LINKEDLIST_H
#define LINKEDLIST_H

#include <iostream>

using namespace std;


template <typename T>
class Node {
private:
	T data;
	Node<T> next;

public:
	Node(T data, Node<T> node) {
		this->data = data;
		this->next = nullptr;
	}
};


template <typename T>
class LinkedList {
private:
	Node<T> head;
	int size;

public:
	LinkedList() {
		this->head = nullptr;
		this->size = 0;
	}

    int length() {
		return this->size;
	}

	void insert(Node<T> node) {
		Node<T> curr = this->head;
		while (curr.next != nullptr) {
			curr = curr->next;
		}
		curr.next = &node;

		this->size++;
	}

    Node<T> remove(Node<T> node) {
        Node<T> curr = this->head;
        return curr;
    }

    void push(Node<T> node) {
        Node<T> curr = this->head;
    }

    Node<T> pop() {
        Node<T> curr = this->head;
        return curr;
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
