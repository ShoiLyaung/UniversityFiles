#include <iostream>

using namespace std;

// 定义平衡二叉树结点类
class AVLNode {
public:
    int data; // 数据域
    int bf; // 平衡因子
    AVLNode* left; // 左子结点
    AVLNode* right; // 右子结点

    // 构造函数
    AVLNode(int d) {
        data = d;
        bf = 0;
        left = nullptr;
        right = nullptr;
    }
};

// 定义平衡二叉树类
class AVLTree {
private:
    AVLNode* root; // 根结点

    // 左旋转函数
    void leftRotate(AVLNode*& p) {
        AVLNode* rc = p->right; // 右子结点
        p->right = rc->left; // 右子结点的左子树变为p的右子树
        rc->left = p; // p变为右子结点的左子结点
        p = rc; // 更新p为右子结点
    }

    // 右旋转函数
    void rightRotate(AVLNode*& p) {
        AVLNode* lc = p->left; // 左子结点
        p->left = lc->right; // 左子结点的右子树变为p的左子树
        lc->right = p; // p变为左子结点的右子结点
        p = lc; // 更新p为左子结点
    }

    // 左平衡函数
    void leftBalance(AVLNode*& p) {
        AVLNode* lc = p->left; // 左子结点
        switch (lc->bf) {
            case 1: // 新插入的结点在左子结点的左子树上，需要进行单右旋转
                rightRotate(p);
                p->bf = 0;
                lc->bf = 0;
                break;
            case -1: // 新插入的结点在左子结点的右子树上，需要进行双旋转（先左后右）
                AVLNode* rd = lc->right; // 左子结点的右子结点
                leftRotate(lc);
                rightRotate(p);
                switch (rd->bf) { // 调整平衡因子
                    case 1:
                        p->bf = -1;
                        lc->bf = 0;
                        break;
                    case 0:
                        p->bf = 0;
                        lc->bf = 0;
                        break;
                    case -1:
                        p->bf = 0;
                        lc->bf = 1;
                        break;
                }
                rd->bf = 0;
                break;
        }
    }

    // 右平衡函数
    void rightBalance(AVLNode*& p) {
        AVLNode* rc = p->right; // 右子结点
        switch (rc->bf) {
            case -1: // 新插入的结点在右子结点的右子树上，需要进行单左旋转
                leftRotate(p);
                p->bf = 0;
                rc->bf = 0;
                break;
            case 1: // 新插入的结点在右子结点的左子树上，需要进行双旋转（先右后左）
                AVLNode* ld = rc->left; // 右子结点的左子结点
                rightRotate(rc);
                leftRotate(p);
                switch (ld->bf) { // 调整平衡因子
                    case -1:
                        p->bf = 1;
                        rc->bf = 0;
                        break;
                    case 0:
                        p->bf = 0;
                        rc->bf = 0;
                        break;
                    case 1:
                        p->bf = 0;
                        rc->bf = -1;
                        break;
                }
                ld->bf = 0;
                break;
        }
    }

    // 插入函数
    bool insert(AVLNode*& p, int x, bool& taller) {
        if (p == nullptr) { // 空树，直接插入
            p = new AVLNode(x);
            taller = true; // 树高度增加
            return true;
        }
        else {
            if (x == p->data) { // 已存在相同的结点，不插入
                taller = false; // 树高度不变
                return false;
            }
            else if (x < p->data) { // 插入到左子树
                if (!insert(p->left, x, taller)) { // 递归插入
                    return false;
                }
                if (taller) { // 左子树高度增加，需要调整平衡因子
                    switch (p->bf) {
                        case 1: // 原本左子树比右子树高，需要进行左平衡处理
                            leftBalance(p);
                            taller = false; // 树高度不变
                            break;
                        case 0: // 原本左右子树等高，现在左子树比右子树高
                            p->bf = 1;
                            taller = true; // 树高度增加
                            break;
                        case -1: // 原本右子树比左子树高，现在左右子树等高
                            p->bf = 0;
                            taller = false; // 树高度不变
                            break;
                    }
                }
            }
            else { // 插入到右子树
                if (!insert(p->right, x, taller)) { // 递归插入
                    return false;
                }
                if (taller) { // 右子树高度增加，需要调整平衡因子
                    switch (p->bf) {
                        case 1: // 原本左子树比右子树高，现在左右子树等高
                            p->bf = 0;
                            taller = false; // 树高度不变
                            break;
                        case 0: // 原本左右子树等高，现在右子树比左子树高
                            p->bf = -1;
                            taller = true; // 树高度增加
                            break;
                        case -1: // 原本右子树比左子树高，需要进行右平衡处理
                            rightBalance(p);
                            taller = false; // 树高度不变
                            break;
                    }
                }
            }
        }
        return true;
    }

    // 求平衡二叉树的高度函数（利用平衡因子）
    int getHeight(AVLNode* p) {
        if (p == nullptr) { // 空结点，返回0
            return 0;
        }
        else {
            int leftHeight = getHeight(p->left); // 左子树的高度
            int rightHeight = getHeight(p->right); // 右子树的高度

            if (p->bf == 1) { // 如果结点的平衡因子为1，说明左子树比右子树高1
                return leftHeight + 1; 
            }
            else  // 如果结点的平衡因子为-1，说明右子树比左子树高1
                return rightHeight + 1;
            
             // 如果结点的平衡因子为0，说明左右子树等高
                // return rightHeight + 1; 
            
        }
    }

    // 中序遍历函数（用于测试）
    void inOrder(AVLNode* p) {
        if (p != nullptr) {
            inOrder(p->left); // 遍历左子树
            cout << p->data << "(" << p->bf << ") "; // 输出结点数据和平衡因子
            inOrder(p->right); // 遍历右子树
        }
    }

public:
    // 构造函数
    AVLTree() {
        root = nullptr;
    }

    // 插入函数（对外接口）
    bool insert(int x) {
        bool taller = false; // 标记树是否增高
        return insert(root, x, taller); // 调用私有插入函数
    }

    // 求平衡二叉树的高度函数（对外接口）
    int getHeight() {
        return getHeight(root); // 调用私有求高度函数
    }

    // 中序遍历函数（对外接口，用于测试）
    void inOrder() {
        inOrder(root); // 调用私有中序遍历函数
        cout << endl;
    }
};
