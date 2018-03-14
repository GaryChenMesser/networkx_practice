# networkx_practice

I will put the codes I practice for networkx here.

## Description
* someproperties_20170725_a.py
  * In this file, I try to compute some properties of a connected graph without the using of the helping function in networkx, like the shortest path between any two nodes of the graph with the aid of BSF algorithm. Other properties like the number of the shortest path of any two nodes, the diameter of the graph, and the average path are shown in this file.
For a deeper look, you can refer to [this](https://networkx.github.io/documentation/networkx-1.10/examples/basic/properties.html)

* findcomponent_20170726.py
  * This program shows how to divide disconnected components of a graph into separate subgraphs using BFS algorithm.  

* complexity_20170728.py
  * This program computes the number of spanning trees of a graph, which is also called complexity based on Kirchhoff's Matrix-tree Theorem.

* simplegraph_20170729.py
  * This program shows a simple example to detect whether a graph is simple.

* bipartite_20170729.py
  * This program displays a way to determine if a graph is bipartite or not.

* someproperties_20170731.py
  * This program is an update of someproperties_20170725_a.py, which expands the limit of node name. In the original version, node name must be  increasing integers start from 0; in this update, node name can be any distinct number(integer or floating) or string or something else that's allowed for node name in NetworkX.

* bipartite_20170802.py
  * This program is totally the same as bipartite_20170729.py except the restriction on the node name.

* findcomponent_matrix_20170802.py
  * This program solves the same issue that findcomponent_20170726.py solved but with matrix computation.

* bipartite_matrix_20170803.py
  * This program solves the same issue that bipartite_20170729.py solved but with matrix computation.
