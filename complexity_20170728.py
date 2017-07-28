#compute the complexity of a graph
#i.e. compute the number of spanning trees of a graph
#base on Kirchhoff's Matrix-tree Theorem

import networkx as nx
import numpy.matlib as np
from numpy import linalg as lin

G=nx.Graph()

#enter the graph
G.add_nodes_from([0,1,2,3])
G.add_edges_from([(0,1),(1,2),(2,3),(0,2),(1,3)])

#initialize a zero matrix called matrix
matrix=np.zeros((G.number_of_nodes(),G.number_of_nodes()))

#------------------------------adjacency matrix-----------------------------
store=G.edges()
ad_matrix=matrix.copy()
#adjacency matrix--undirected
for a in range (G.number_of_edges()):
    ad_matrix.getA()[(store[a][0])][(store[a][1])]=1
    ad_matrix.getA()[(store[a][1])][(store[a][0])]=1
print('adjacency matrix:','\n',ad_matrix)
'''
#adjacency matrix--directed
for a in range (G.number_of_edges()):
    matrix[store[i][0]][store[i][1]]=1

'''
#degree matrix
deg_matrix=matrix.copy()
for a in range(G.number_of_nodes()):
    deg_matrix.getA()[a][a]=G.degree(a)
#laplacian matrix
lap_matrix=deg_matrix.copy()-ad_matrix.copy()

lap_matrix=np.delete(lap_matrix,0,0)
lap_matrix=np.delete(lap_matrix,0,1)

complexity=lin.det(lap_matrix)

print('complexity=',complexity)
