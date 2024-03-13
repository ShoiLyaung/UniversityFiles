#include "AvlTree.h"

using namespace std;

int main() {
    AVLTree tree; // 创建一个平衡二叉树对象
    int arr[] = {10, 5, 15, 3, 7, 12, 18}; // 测试数据
    int n = sizeof(arr) / sizeof(arr[0]); // 数组长度

    for (int i = 0; i < n; i++) { // 循环插入数据
        tree.insert(arr[i]);
        cout << "After inserting " << arr[i] << ", the tree is: " << endl;
        tree.inOrder(); // 中序遍历输出树的结构
        cout << "The height of the tree is: " << tree.getHeight() << endl; // 输出树的高度
        cout << "--------------------------" << endl;
    }

    return 0;
}
    