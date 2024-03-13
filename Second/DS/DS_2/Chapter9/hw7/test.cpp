#include "LinkQuickSort.h"
#include <cstdlib> // 包含 rand() 和 srand() 函数
#include <ctime> // 包含 time() 函数

using namespace std;

int main() {
    DoublyLinkedList list;

    // // 生成随机测试数据
    // // 设置随机数种子
    // srand(time(0));
    // const int testDataSize = 10;
    // for (int i = 0; i < testDataSize; ++i) {
    //     int randomData = rand() % 100; // 生成 0-99 之间的随机数
    //     list.insert(randomData);
    // }

    // //测试一个数据
    // list.insert(65);

    // //测试两个数据
    // list.insert(65);
    // list.insert(56);

    // list.insert(56);
    // list.insert(65);

    //测试多个数据
    list.insert(65);
    list.insert(56);
    list.insert(-75);
    list.insert(13);
    list.insert(0);
    list.insert(27);
    list.insert(1298);
    list.insert(-97);
    list.insert(21);
    list.insert(37);


    cout << "Original List: \t" << endl;
    list.print();

    list.quickSort();

    cout << "\nSorted List: \t";
    list.print();

    return 0;
}
