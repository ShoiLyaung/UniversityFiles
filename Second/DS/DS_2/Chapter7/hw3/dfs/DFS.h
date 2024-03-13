#ifndef __DFS_H__
#define __DFS_H__

#include "AdjMatrixUndirGraph.h"		// ����ͼ�ڽӾ���

template <class ElemType>
void DFSTraverse(const AdjMatrixUndirGraph<ElemType> &g, void (*Visit)(const ElemType &))
// ��ʼ����������ͼg
// ���������������ͼg����������ȱ���
{
	int v;
	for (v = 0; v < g.GetVexNum(); v++)
		g.SetTag(v, UNVISITED);// ��ÿ����������δ���ʱ�־

	for (v = 0; v < g.GetVexNum(); v++)
		
		if (g.GetTag(v) == UNVISITED)
			DFS(g, v , Visit);// ����δ���ʵĶ���v��ʼ��������������� 
}

template <class ElemType>
void DFS(const AdjMatrixUndirGraph<ElemType> &g, int v, void (*Visit)(const ElemType &))
// ��ʼ����������ͼg
// ����������Ӷ���v�������������������
{	
	ElemType e;	
	g.SetTag(v, VISITED);		// ���ö���v�ѷ��ʱ�־
	g.GetElem(v, e);			// ȡ����v������Ԫ��ֵ 
	Visit(e);					// ���ʶ���v
	for (int w = g.FirstAdjVex(v); w != -1; w = g.NextAdjVex(v, w))
		if (g.GetTag(w) == UNVISITED)
			DFS(g, w , Visit);	// ��v����δ���ʹ����ڽӶ���w��ʼ���������������
}
#endif
