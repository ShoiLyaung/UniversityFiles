#include <iostream>
#include <cstring>

using namespace std;

struct Edge {
    int u, v;
    int nextu, nextv;
    int weight;
    Edge() {}
    Edge(int u, int v, int nextu, int nextv, int weight) : u(u), v(v), nextu(nextu), nextv(nextv), weight(weight) {}
};

class Graph {
private:
    Edge* edges;
    int* head;
    bool *tags;
    int idx;
    int num_vertices;
    int num_edges;

public:
    Graph(int n, int m) : num_vertices(n), num_edges(m) {
        edges = new Edge[2 * num_edges];
        head = new int[num_vertices];
        tags = new bool[num_vertices];
        idx = 0;
        memset(head, -1, sizeof(int) * num_vertices);
        memset(tags, false, sizeof(bool) * num_vertices);
    }

    ~Graph() {
        delete[] edges;
        delete[] head;
        delete[] tags;
    }

    void add_edge(int u, int v, int weight) {
        edges[idx] = Edge(u, v, head[u], head[v], weight);
        head[u] = head[v] = idx++;
    }

    void print_graph() {
        for (int u = 0; u < num_vertices; u++) {
            cout << "Vertex " << u << ": ";
            for (int i = head[u]; i != -1; i = (u == edges[i].u ? edges[i].nextu : edges[i].nextv)) {
                int v = (u == edges[i].u ? edges[i].v : edges[i].u);
                cout << " " << v << " (" << edges[i].weight << ") ";
            }
            cout << endl;
        }
    }

    void has_simple_path(int n){
        
        for (int u = 0; u < num_vertices; u++) {
            memset(tags, false, sizeof(bool) * num_vertices);
            cout << "--------------------------------------" << endl;
            cout << u << endl;
            DFS(u,n);
            
            cout << endl;
        }
    }

    
    void DFS(int u,int n) {
        if (n==0) {
            cout << " 和 " << u << " 之间存在一条长度为n的简单路径" << endl;
            return;
        }
        else{
            tags[u] = true;
            for (int i = head[u]; i != -1; i = (u == edges[i].u ? edges[i].nextu : edges[i].nextv)) {
                int v = (u == edges[i].u ? edges[i].v : edges[i].u);
                if (!tags[v]) {
                    DFS(v,n-edges[i].weight);
                }
            }
            tags[u] = false;
        }
    }
};
