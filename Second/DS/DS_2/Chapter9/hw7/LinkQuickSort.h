#include<iostream>

using namespace std;

#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
    Node* prev;
    Node(): prev(nullptr), next(nullptr) {} // 构造函数
    Node(int x): data(x), prev(nullptr), next(nullptr) {} // 构造函数
};

class DoublyLinkedList {
private:
    Node* head;
public:
    DoublyLinkedList() {
        head = new Node();
    }

    void insert(int x) { // 在链表尾部插入一个新结点
        Node* p = head;
        while (p->next) p = p->next; // 找到链表尾结点
        Node* q = new Node(x); // 创建一个新结点
        p->next = q; // 将新结点插入到尾部
        q->prev = p; // 更新新结点的前指针
    }

    void print() {
        Node* temp = head->next;

        while (temp != nullptr) {
            cout << temp->data << " ";
            temp = temp->next;
        }
    }

    void quickSort() {
        Node* tail = head;
        while (tail->next) tail = tail->next;
        
        quickSort(head->next, tail);
    }

private:
    void quickSort(Node* left, Node* right) {
        if (right != nullptr && left != right && left != right->next) {
            Node* pivot = partition(left, right);

            cout << endl;
            cout << "以" << pivot->data << "为枢取元素";
            cout << endl;
            print();
            cout << endl;
            
            quickSort(left, pivot->prev);
            quickSort(pivot->next, right);
            

        }
    }

    Node* partition(Node*& left, Node*& right) {
        int pivot = right->data;    // 取枢轴元素 
        Node* i = left->prev;

        for (Node* j = left; j != right; j = j->next) {
            if (j->data <= pivot) {
                i = i->next;
                if(i==left) left=j;
                swap(i, j);
                
            }
        }
        i = i->next;
        if(i==left) left=right;
        swap(i, right);

        return i;
    }

    // void swap(Node*& a, Node*& b) {
    //     int temp = a->data;
    //     a->data = b->data;
    //     b->data = temp;
    // }

    void swap(Node*& a, Node*& b) {
        if (a == b) return;
        if (a->next == b) { // a 和 b 相邻
            a->prev->next = b;
            if(b->next){    // b 不是尾结点
                b->next->prev = a;
                a->next = b->next;
                b->prev = a->prev;
                a->prev = b;
                b->next = a;
            }
            else{           // b 是尾结点
                b->prev = a->prev;
                a->prev = b;
                a->next = nullptr;
                b->next = a;
            }
        } else if (b->next == a) {  // a 和 b 相邻
            swap(b, a);
        } else {            // a 和 b 不相邻
            Node* temp = a->prev;
            a->prev = b->prev;
            b->prev = temp;

            temp = a->next;
            a->next = b->next;
            b->next = temp;

            if (a->prev) {
                a->prev->next = a;
            }
            if (a->next) {
                a->next->prev = a;
            }
            if (b->prev) {
                b->prev->next = b;
            }
            if (b->next) {
                b->next->prev = b;
            }
        }
        Node* temp = a; // 交换 a 和 b
        a = b;
        b = temp;
    }
};

