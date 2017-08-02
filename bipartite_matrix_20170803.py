#find components in the graph

import networkx as nx
import numpy.matlib as np

G=nx.Graph()

#enter the graph here
G.add_edges_from([('a',1),(1,2),(1,3),(2,4),(2,5),(3,6)])

#set every node attribute 'check' to -1
for a in G.nodes():
    G.node[a]['check']=-1

#adjacency matrix
store=G.edges()
ad_matrix=np.zeros([G.number_of_nodes(),G.number_of_nodes()])
#adjacency matrix--undirected
for a in range(G.number_of_edges()):
    ad_matrix.getA()[G.nodes().index(store[a][0])][G.nodes().index(store[a][1])]=1
    ad_matrix.getA()[G.nodes().index(store[a][1])][G.nodes().index(store[a][0])]=1

lap_matrix=ad_matrix

#check whether disconnected
Lap_matrix=lap_matrix**(G.number_of_nodes()+1)
count1=np.nonzero(Lap_matrix)
count2=np.nonzero(Lap_matrix*lap_matrix)
if len(count1[0])!=0 and len(count1[0])!=np.size(Lap_matrix) and (len(count1[0])+len(count2[0]))==np.size(Lap_matrix) and (count1[0][0],count1[1][0])!=(count2[0][0],count2[1][0]):
    print('This graph is bipartite.')
else:
    print('not yet')
print(lap_matrix)
print(Lap_matrix)
print(Lap_matrix*lap_matrix)
