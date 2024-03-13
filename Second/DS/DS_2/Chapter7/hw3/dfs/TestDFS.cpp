#include "DFS.h"						// ͼ��������ȱ���

int main(void)
{
    try									// ��try��װ���ܳ����쳣�Ĵ���
	{
		char vexs[] = {'A', 'B', 'C', 'D', 'E', 'F' ,'G', 'H', 'I'};
		int m[9][9] = {
			{0, 1, 0, 1, 1, 0, 0, 0, 0},
			{1, 0, 1, 0, 1, 0, 0, 0, 0},
			{0, 1, 0, 0, 1, 0, 0, 0, 0},
			{1, 0, 0, 0, 0, 0, 1, 0, 0},
			{1, 1, 1, 0, 0, 1, 1, 0, 0},
			{0, 0, 0, 0, 1, 0, 0, 0, 1},
			{0, 0, 0, 1, 1, 0, 0, 1, 0},
			{0, 0, 0, 0, 0, 0, 1, 0, 0},
			{0, 0, 0, 0, 0, 1, 0, 0, 0}
		};
		int n = 9;

		AdjMatrixUndirGraph<char> g(vexs, n);

		for (int u = 0; u < n; u++)
		{	// �����ڽӾ������
			for (int v = u; v < n; v++)
			{	// �����ڽӾ���Ԫ�ص�ֵ
				if (m[u][v] == 1) g.InsertArc(u, v);
			}
		}

		cout << "ԭ��ͼ:" << endl;
		g.Display();						// ��ʾͼg
		cout << endl;
		system("PAUSE");				// ���ÿ⺯��system()

		cout << "������ȱ���:";
		DFSTraverse<char>(g, Write<char>);// <char>����ȷ������ģ�����
		cout << endl;
	}
	catch (Error err)					// ��׽�������쳣
	{
		err.Show();						// ��ʾ�쳣��Ϣ
	}

	system("PAUSE");					// ���ÿ⺯��system()
	return 0;							// ����ֵ0, ���ز���ϵͳ
}

