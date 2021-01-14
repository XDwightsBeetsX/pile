#ifndef STACK_H
#define STACK_H

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
class Stack {
private:
	int size;
	vector<Node<T>> elements;

public:
	Stack() {
		this->size = 0;
		this->elements = NULL;
	}

    void push(Node<T> node) {
        Node<T> first = this->elements[0];
        for (int i = this->size - 1; i > 0; i--)
        {
            this->elements[i] = this->elements[i-1];
        }
        this->elements[0] = node;
        this->size++;
    }

    Node<T> pop() {
        Node<T> first = this->elements[0];
        for (int i = 0; i < this->size - 1; i++)
        {
            this->elements[i] = this->elements[i+1];
        }
        this->elements[this->size] = NULL;
        this->size--;
        
        return first;
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
