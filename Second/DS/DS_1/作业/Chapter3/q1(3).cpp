template <class ElemType>
void SeqList<ElemType>::Overkill() {
    ElemType first_x,rpt_x;
    for (int i = 1; i <= length; i++) {
        GetElem(i,first_x);                  //取出一个第一次出现的元素
        for (int j = i+1; j <= length; j++) {
            GetElem(j,rpt_x);              //在取出的元素后遍历
            if (rpt_x==first_x){
                DeleteElem(j,rpt_x);       //删除重复的元素
                j--;                            //被删除元素之后的元素依次左移一个位置，所以需要回到之前一个元素以继续遍历
            }
        }
    }
}
