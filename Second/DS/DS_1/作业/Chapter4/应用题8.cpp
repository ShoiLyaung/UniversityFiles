void test(int &sum){
    int x;
    sum=0;          //sum初始化
    Stack<int> s;
    scanf(x);
    if(x==0)printf(sum);//只输入0，直接输出结果
    //输入不为0，将输入数据入栈
    while(x!=0){
        s.Push(x);
        scanf(x);
    }
    //出栈，按照输入相反的顺序累加
    while(!s.IsEmpty()){
        s.Pop(x);
        sum += x;
    }
    printf(sum);
}