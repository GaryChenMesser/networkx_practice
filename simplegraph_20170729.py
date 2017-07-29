#determine whether a graph is a simple or not
#this program hase no actual use but just a practice because Graph() doesn't allow multiple paths.
#we can still use it to test loop.

import networkx as nx

#G=nx.Graph()
MG=nx.MultiGraph()

MG.add_nodes_from([0,1,2,3,4,5,6,7,8])
MG.add_edges_from([(0,1,dict(route=100)),(0,1,dict(route=101)),(0,7),(1,2),(1,7),(2,3),(2,5),(2,8),(3,4),(3,5),(4,5),(5,6),(6,7),(6,8),(7,8)])

for a in MG.nodes():
    if MG.degree(a)>len(MG.neighbors(a)):
        simple=False
        print('This graph is not simple.')
        break
    if a==MG.nodes()[-1]:
        print('This graph is simple.')
