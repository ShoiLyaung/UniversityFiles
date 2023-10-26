//
// Created by ShoiLyaung on 2022/12/13.
//

#ifndef DS_1_STACK2QUEUE_H
#define DS_1_STACK2QUEUE_H

#include "seq_stack/SeqStack.h"
#include "link_stack/LinkStack.h"

template<class ElemType>
class Stack2Queue{
protected:
    int front, rear;									 // 队头队尾指针
    int maxSize;										 // 队列容量
    //ElemType *elems;									 // 元素存储空间
    SeqStack<ElemType> *s1, *s2;                        //顺序栈模式
//    LinkStack<ElemType> *s1, *s2;                     //链式栈模式
public:
    Stack2Queue(int size = DEFAULT_SIZE);					 // 构造函数
    virtual ~Stack2Queue();								 // 析构函数
    void ShowQueue();
    Status EnQueue(const ElemType &e);
    Status DelQueue(ElemType &e);
    bool IsEmpty()const;
};

template<class ElemType>
Stack2Queue<ElemType>::Stack2Queue(int size)
// 操作结果：构造一个容量为size的空队列
{
    maxSize = size;							// 设置队列容量
    s1 = new SeqStack<ElemType>(maxSize);   // 分配元素存储空间//顺序栈模式
    s2 = new SeqStack<ElemType>(maxSize);   // 分配元素存储空间//顺序栈模式
//    s1 = new LinkStack<ElemType>;   // 分配元素存储空间//链式栈模式
//    s2 = new LinkStack<ElemType>;   // 分配元素存储空间//链式栈模式
    rear = front = 0;						// 初始化队头与队尾
}
template <class ElemType>
Stack2Queue<ElemType>::~Stack2Queue()
// 操作结果：销毁队列
{
    delete  s1;
    delete  s2;       // 释放元素存储空间
}
template<class ElemType>
void Stack2Queue<ElemType>::ShowQueue(){
    s1->Traverse(Write<ElemType>);
}
template<class ElemType>
Status Stack2Queue<ElemType>::EnQueue(const ElemType &e) {
    //判空
    if(s2->IsEmpty())
        return s1->Push(e);
    else if(!s2->IsEmpty()){
        //将s2元素倒回s1
        ElemType e_tmp;
        while(!s2->IsEmpty()){
            s2->Pop(e_tmp);
            s1->Push(e_tmp);
        }
        return s1->Push(e);
    }
}
template<class ElemType>
Status Stack2Queue<ElemType>::DelQueue(ElemType &e) {
    //判空
    if(s1->IsEmpty())
        return s2->Pop(e);
    if(!s1->IsEmpty()){
        ElemType e_tmp;
        //将s1中元素倒入s2
        while(!s1->IsEmpty()){
            s1->Pop(e_tmp);
            s2->Push(e_tmp);
        }
        //此时s1栈底的元素在s2的top，将其pop实现出队
        return s2->Pop(e);
        //将s2剩余元素倒回s1
//        while(!s2->IsEmpty()){
//            s2->Pop(e_tmp);
//            s1->Push(e_tmp);
//        }
//        return SUCCESS;
    }
    else
        return UNDER_FLOW;
}
template<class ElemType>
bool Stack2Queue<ElemType>::IsEmpty() const{
    //判空列操作与栈判空相同
    return (s1->IsEmpty()&&s2->IsEmpty());
}

#endif //DS_1_STACK2QUEUE_H
