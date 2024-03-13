#include "AdjListUndirGraph.h"

using namespace std;

int main() {
    Graph g(6, 11);

    g.add_edge(0, 1, 12);
    g.add_edge(0, 2, 3);
    g.add_edge(0, 4, 9);
    g.add_edge(0, 5, 10);

    g.add_edge(1, 4, 6);
    g.add_edge(1, 3, 2);

    g.add_edge(2, 3, 2);
    g.add_edge(2, 5, 6);

    g.add_edge(3, 4, 4);
    g.add_edge(3, 5, 7);

    g.add_edge(4, 5, 4);

    g.print_graph();

    // cout << "DFS traversal: ";
    // g.DFS(0);
    // cout << endl;
    
    int n=0;

    while(1){
        cout << "想要查询的路径长度为：";
        cin >> n;
        cout << endl;
        if(n==-1) break;
        else{
            g.has_simple_path(n);
            cout << endl;
        }
       
    }
    

    return 0;
}
