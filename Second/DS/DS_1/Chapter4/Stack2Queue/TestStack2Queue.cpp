//
// Created by ShoiLyaung on 2022/12/13.
//
#include "Stack2Queue.h"

int  main(void)
{
    char c = '1';
    Stack2Queue<int> qa;
    int x;
    while (c != '0')
    {
        cout << endl << "1. 生成队列.";
        cout << endl << "2. 显示队列.";
        cout << endl << "3. 入队列.";
        cout << endl << "4. 出队列.";
        cout << endl << "5. 判空.";
        cout << endl << "0. 退出";
        cout << endl << "选择功能(0~5):";
        cin >> c;
        switch (c)
        {
            case '1':
//                qa.Clear();
                cout << endl << "输入e(e = 0时退出)";
                cin >> x;
                while (x != 0)	{
                    qa.EnQueue(x);
                    cin >> x;
                }
                break;
            case '2':
                cout << endl;
                qa.ShowQueue();
                break;
            case '3':
                cout << endl << "输入元素值:";
                cin >> x;
                if (qa.EnQueue(x) == OVER_FLOW)
                    cout << endl << "队列已满!";
                else
                    cout << endl << "入队成功.";
                break;
            case '4':
                if(qa.DelQueue(x)==SUCCESS)
                    cout << endl << "队头元素值为 " << x << " ." << endl;
                else
                    cout << endl << " 队列下溢 " << endl;
                break;
            case '5':
                if(!qa.IsEmpty()){
                    cout << endl << "队列不为空"  << endl;
                }
                else if(qa.IsEmpty()){
                    cout << endl << "队列为空"  << endl;
                }
                break;
        }
    }

    system("PAUSE");
    return 0;

}
