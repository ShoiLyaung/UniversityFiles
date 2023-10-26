//2.（3）
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

//2.（4）
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