#ifndef QUEUE_H
#define QUEUE_H

#include <iostream>
#include <vector>

using namespace std;


template <typename T>
class Node {
private:
	T data;
	Node<T> next;

public:
	Node(T data) {
		this->data = data;
		this->next = nullptr;
	}
};


template <typename T>
class Queue {
private:
	int size;
	vector<Node<T>> elements;

public:
	Queue() {
		this->size = 0;
		this->elements = NULL;
	}

    void enqueue(Node<T> node) {
        for (int i = this->size - 1; i > 0; i--)
        {
            this->elements[i+1] = this->elements[i];
        }
        this->elements[0] = node;
        this->size++;
    }

    Node<T> dequeue() {
        Node<T> last = this->elements[this->size - 1];
        this->elements[this->size - 1] = NULL;
        this->size--;
        return last;
    }

    void clear() {
        this->elements.clear();
        this->size = 0;
    }

    bool isEmpty() {
        return this->size == 0;
    }

    void show() {
        for (int i = 0; i < this->size; i++)
        {
            cout << this->elements[i] << " ";
        }
        cout << endl;
    }
};

#endif
