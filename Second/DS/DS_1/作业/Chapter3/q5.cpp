template <class ElemType>
Status LinkList<ElemType>::DeleteElem(int i, ElemType &e)
// 操作结果：删除单链表的第i个位置的元素, 并用e返回其值,
//	i的取值范围为1≤i≤length,
//	i合法时函数返回SUCCESS,否则函数返回RANGE_ERROR
{
	if (i < 1 || i > length)		
		return RANGE_ERROR;   // i范围错		 
 	else {
        Node<ElemType> *p = head, *q;
        //头结点处理/////////////////////////////////////////////////////////////////////
        if (i == 1) {//删除头结点
            q=head;
            head=head->next;
        }else{
            ////////////////////////////////////////////////////////////////////////////
            int count;
            for (count = 1; count < i; count++)
                p = p->next;	      // p指向第i-1个结点
            q = p->next;	      // q指向第i个结点
            p->next = q->next;	  // 删除结点
        }
		e = q->data;		  // 用e返回被删结点元素值	
		length--;			  // 删除成功后元素个数减1 
		delete q;			  // 释放被删结点
		return SUCCESS;
	}
}

template <class ElemType>
Status LinkList<ElemType>::InsertElem(int i, const ElemType &e)
// 操作结果：在单链表的第i个位置前插入元素e
//	i的取值范围为1≤i≤length+1
//	i合法时返回SUCCESS, 否则函数返回RANGE_ERROR
{
	if (i < 1 || i > length+1)
		return RANGE_ERROR;   			 
 	else	{
		Node<ElemType> *p = head, *q;
        //头结点处理/////////////////////////////////////////////////////////////////////
        if(i==1){//插入头结点
            q = new Node<ElemType>(e,head);
            head=q;
        }else{
            ////////////////////////////////////////////////////////////////////////////
            int count;
            for (count = 1; count < i; count++)
                p = p->next;	                    // p指向第i-1个结点
            q = new Node<ElemType>(e, p->next); // 生成新结点q
            assert(q);                          // 申请结点失败，终止程序运行
            p->next = q;				        // 将q插入到链表中
        }
		length++;							// 插入成功后，单链表长度加1 
		return SUCCESS;
	}
}