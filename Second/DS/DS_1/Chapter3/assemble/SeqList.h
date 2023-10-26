#ifndef __SQ_LIST_H__
#define __SQ_LIST_H__
#include "Assistance.h"	// 辅助软件包

// 顺序表模板类的申明 
template <class ElemType>
class SeqList 
{
protected:
// 顺序表的数据成员
	int length;					// 顺序表的当前长度 
	int maxLength;				// 顺序表的最大容量
	ElemType *elems;			// 元素存储空间的首地址 

public:
// 顺序表的函数成员
	SeqList(int size = DEFAULT_SIZE);	// 构造一个空表 
	SeqList(ElemType v[], int n, int size = DEFAULT_SIZE);	// 根据数组v的内容构造顺序表 
	virtual ~SeqList();			// 析构函数
	int GetLength() const;		// 取顺序表长度			 
	bool IsEmpty() const;		// 判断顺序表是否为空
	void Clear();				// 将顺序表清空
	void Traverse(void (*Visit)(const ElemType &)) const;	// 遍历顺序表
	int LocateElem(const ElemType &e) const;	// 元素定位，求指定元素在顺序表中的位置
	Status GetElem(int i, ElemType &e) const;	// 取顺序表中第i个元素的值	
	Status SetElem(int i, const ElemType &e);	// 修改顺序表中第i个元素的值
	Status DeleteElem(int i, ElemType &e);      // 删除顺序表中第i个元素		
	Status InsertElem(int i, const ElemType &e); // 在顺序表第i个位置插入元素
 	Status InsertElem(const ElemType &e);        // 在顺序表表尾插入元素
	SeqList(const SeqList<ElemType> &sa);        // 复制构造函数
	SeqList<ElemType> &operator =(const SeqList<ElemType> &sa); // 赋值语句重载

    SeqList<ElemType>& Merge(const SeqList<ElemType>& s1,const SeqList<ElemType>& s2);//merge
    void Exclude(const ElemType& s,const ElemType& t);//删除(s,t)区间内的元素
};


// 顺序表函数成员的实现部分

template <class ElemType>
SeqList<ElemType>::SeqList(int size)
// 操作结果：构造一个最大容量为size的空顺序表
{
	elems = new ElemType[size];		    // 申请存储空间
	assert(elems);                      // 申请存储空间失败，程序终止 
	maxLength = size;					// 设置顺序表的最大容量
	length = 0;							// 空线性表的长度为0
}

template <class ElemType>
SeqList<ElemType>::SeqList(ElemType v[], int n, int size)
// 操作结果：根据数组v中的内容构造顺序表
{
	elems = new ElemType[size];		    // 申请存储空间
	assert(elems);                      // 申请存储空间失败，程序终止 
	maxLength = size;					// 设置顺序表的最大容量
	length = n;							// 顺序表的当前长度为n 
	for (int i = 0; i < length; i++)	// 将数组v中的元素依次存放到elems数组中 
		elems[i] = v[i]; 
}
 
template <class ElemType>
SeqList<ElemType>::~SeqList()
// 功能：回收顺序表的存储空间 
{
	delete []elems;						// 释放存储空间
}

template <class ElemType>
int SeqList<ElemType>::GetLength() const
// 功能：返回顺序表中元素个数
{
	return length;
}

template <class ElemType>
bool SeqList<ElemType>::IsEmpty() const
// 功能：如顺序表为空，则返回true，否则返回false
{
	return length == 0;
}

template <class ElemType>
void SeqList<ElemType>::Clear()
// 功能：清空顺序表
{
	length = 0;
}

template <class ElemType>
void SeqList<ElemType>::Traverse(void (*visit)(const ElemType &)) const
// 功能：依次对顺序表的每个元素调用函数(*visit)进行访问 
{
	for (int i = 0; i < length; i++)
		(*visit)(elems[i]);
}

template <class ElemType>
int SeqList<ElemType>::LocateElem(const ElemType &e) const
// 功能：求元素e在顺序表中的序号,如果顺序表中不存在元素e则返回0
{
	int i = 0;
    while (i < length && elems[i] != e)
         i++;	
    return i < length ? i+1 : 0;
}

template <class ElemType>
Status SeqList<ElemType>::GetElem(int i, ElemType &e) const
// 功能：当顺序表存在第i个元素时，用e返回其值，函数返回ENTRY_FOUND,否则函数返回NOT_PRESENT
{
	if(i < 1 || i > length)
		return NOT_PRESENT;	// 返回元素不存在
	else	{
		e = elems[i - 1];
		return ENTRY_FOUND;	// 元素存在
	}
}

template <class ElemType>
Status SeqList<ElemType>::SetElem(int i, const ElemType &e)
// 功能：将顺序表的第i个位置的元素赋值为e。i的取值范围为1≤i≤length,i合法时函数返回SUCCESS,否则函数返回RANGE_ERROR
{
	if (i < 1 || i > length)
		return RANGE_ERROR;	// 返回位置错
	else	{
		elems[i - 1] = e;
		return SUCCESS;		// 返回修改成功
	}
}

template <class ElemType>
Status SeqList<ElemType>::DeleteElem(int i, ElemType &e)
// 功能：删除顺序表第i个位置的元素, 并前用e返回其值。i的的取值范围为1≤i≤length,i合法时函数返回SUCCESS,否则函数返回RANGE_ERROR
{
	if (i < 1 || i > length)		
		return RANGE_ERROR;      // 返回位置错
	else	{
		e = elems[i - 1];	     // 用e返回被删除元素的值
		for (int j = i; j < length; j++)// 被删除元素之后的元素依次左移一个位置 
			elems[j-1] = elems[j]; 
		length--;				// 删除后顺序表元素个数减1
		return SUCCESS;	        // 返回删除成功
	}
}

template <class ElemType>
Status SeqList<ElemType>::InsertElem(int i, const ElemType &e)
// 功能：在顺序表的第i个位置插入元素e,i的的取值范围为1≤i≤Length()+1。 
//	如顺序表已满,则返回OVER_FLOW,
//	如i合法, 则返回SUCCESS, 否则函数返回RANGE_ERROR
{
	if (length == maxLength)
		return OVER_FLOW;	            	// 顺序表已满,返回OVER_FLOW
	else if (i < 1 || i > length + 1)		// i范围错,返回位置错
		return RANGE_ERROR;
	else	{
		for (int j = length; j >= i; j--)  // 插入位置之后的元素右移
			elems[j] = elems[j - 1]; 
		elems[i - 1] = e;	               // 将e赋值到顺序表i位置	
   		length++;				           // 插入后元素个数加1
     	return SUCCESS;			           // 返回插入成功
	}
}

template <class ElemType>
Status SeqList<ElemType>::InsertElem(const ElemType &e)
// 功能：在顺序表的表尾插入元素e,并则返回SUCCESS，如顺序表已满,则返回OVER_FLOW
{
	if (length==maxLength)		// 顺序表已满返回OVER_FLOW
		return OVER_FLOW;	
	else	{
		elems[length] = e;	    // 将元素e插入到表尾	
   		length++;				// 插入后，顺序表元素个数加1
     	return SUCCESS;			// 返回插入成功
	}
}

template <class ElemType>
SeqList<ElemType>::SeqList(const SeqList<ElemType> &sa)
// 功能：复制构造函数，由顺序表sa构造新顺序表
{
	int saLength = sa.GetLength();	// 取顺序表sa的长度
	ElemType e;

	maxLength = sa.maxLength;		// 取顺序表的最大容量
	elems = new ElemType[maxLength];// 分配存储空间
	assert(elems);                  // 分配存储空间失败 
	length = 0;					    // 空顺序表元素个数为0

	for (int i = 1; i <= saLength; i++)	{
		sa.getElem(i, e);		    // 取出顺序表sa中第i个元素
		insertElem(e);			    // 将e插入到当前顺序表的表尾 
	}
}

template <class ElemType>
SeqList<ElemType> &SeqList<ElemType>::operator =(const SeqList<ElemType> &sa)
// 功能：赋值语句重载，将顺序表sa赋值给当前顺序表
{
	if (&sa != this)	{
		int saLength = sa.GetLength();	// 取顺序表sa的长度
		ElemType e;

        maxLength = sa.maxLength;		// 取顺序表的最大容量
        delete []elems;                 // 释放顺序表原来的存储空间
        elems = new ElemType[maxLength];// 分配存储空间
	    assert(elems);                  // 分配存储空间失败 
        length = 0;						// 空顺序表元素个数为0
        for (int i = 1; i <= saLength; i++)	{
			sa.getElem(i, e);	        // 取出顺序表sa中第i个元素
			insert(e);		            // 将e插入到当前顺序表的表尾
		}
	}
	return *this;
}

template<class ElemType>
SeqList<ElemType> &SeqList<ElemType>::Merge(const SeqList<ElemType> &s1, const SeqList<ElemType> &s2) {
    int length_s1=s1.GetLength();
    int length_s2=s2.GetLength();
    maxLength=s1.maxLength+s2.maxLength;
    elems=new ElemType[maxLength];
    assert(elems);
    length=0;
    //通过归并算法将两个序列合一
    ElemType e1,e2;
    int i=1,j=1;
    s1.GetElem(i,e1);
    s2.GetElem(j,e2);
    while (i<=length_s1&&j<=length_s2){
        if(e1<e2){
            elems[length++]=e1;
            s1.GetElem(++i,e1);
        }
        else{
          elems[length++]=e2;
          s2.GetElem(++j,e2);
        }
    }
        while(i<=length_s1){
            elems[length++]=e1;
            s1.GetElem(++i,e1);
        }
        while(j<=length_s2){
            elems[length++]=e2;
            s2.GetElem(++j,e2);
        }
    return *this;
}

template<class ElemType>
void SeqList<ElemType>::Exclude(const ElemType &s, const ElemType &t) {
    if(length<=0||s>=t){
        std::cerr<<"顺序表为空或区间为空"<<endl;
        return;
    }
    ElemType e;
    for(int i=0;i<length;i++){
        if(elems[i]<s||elems[i]>t){
            continue;
        } else{
            DeleteElem(i,e) ;
            i--;//删除后剩下的所有元素向左移1单位，所以计数器也要回退1
        }
    }
}

#endif
