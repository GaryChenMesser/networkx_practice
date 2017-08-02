#find components in the graph

import networkx as nx
import numpy.matlib as np

G=nx.Graph()

#enter the graph here
#G.add_nodes_from([0,1,2,3,4,5,6,7,8])
#G.add_edges_from([(0,1),(0,7),(1,2),(1,7),(2,3),(2,5),(2,8),(3,4),(3,5),(4,5),(5,6),(6,7),(6,8),(7,8)])

G.add_nodes_from(['we','are','in','a','group','connect','with','each','other','how',' are','you',"I'm",'fine'])
G.add_edges_from([('we','are'),('are','in'),('in','a'),('a','group'),('are','a'),('connect','with'),('with','each'),('connect','each'),('each','other'),('how','you'),('how',' are'),(' are','you'),("I'm",'fine')])

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

lap_matrix=ad_matrix+np.identity(G.number_of_nodes())

#check whether disconnected
lap_matrix=lap_matrix**G.number_of_nodes()
count1=np.count_nonzero(lap_matrix)
count2=np.count_nonzero(lap_matrix*lap_matrix)
if count1!=0 and count1!=np.size(lap_matrix) and count1==count2:
    print('The graph is disconnected.')
else:
    print('The graph is connected.')
    
component=[]

for index,a in enumerate(G.nodes()):
    if G.node[a]['check']!=-1:
        continue
    node_list=[]
    for b in range(len(lap_matrix.getA()[index])):
        if lap_matrix.getA()[index][b]!=0:
            node_list.append(G.nodes()[b])
            G.node[G.nodes()[b]]['check']=0
    component.append(node_list)
print('There are {0} disconnected components in this graph:'.format(len(component)))
for a in range(len(component)):
    print(component[a])







            
    
