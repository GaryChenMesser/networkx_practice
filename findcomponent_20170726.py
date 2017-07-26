#find components in the graph

import networkx as nx

G=nx.Graph()

#enter the graph here
#G.add_nodes_from([0,1,2,3,4,5,6,7,8])
#G.add_edges_from([(0,1),(0,7),(1,2),(1,7),(2,3),(2,5),(2,8),(3,4),(3,5),(4,5),(5,6),(6,7),(6,8),(7,8)])

G.add_nodes_from([0,1,2,3,4,5,6,7,8,9,10,11,12,13])
G.add_edges_from([(0,1),(1,2),(2,3),(3,4),(1,3),(5,6),(6,7),(5,7),(7,8),(9,11),(9,10),(10,11),(12,13)])

#set every node attribute 'check' to -1
for a in range(G.number_of_nodes()):
    G.node[a]['check']=-1

def check():
    for a in range(len(neighbor)):
        if G.node[neighbor[a]]['check']==-1:
            return 1
            break
        else:
            if a==len(neighbor)-1:
                return 0

e=0
component=[]

for b in range(G.number_of_nodes()):
    if G.node[b]['check']!=-1:
        continue
    node_list=[]
    check1=1
    G.node[b]['check']=e
    node_list.append(b)
    e+=1
    while check1:
        check1=0
        for d in range(G.number_of_nodes()):
            if G.node[d]['check']==e-1:
                neighbor=G.neighbors(d)
                check1+=check()
                for c in range(len(neighbor)):
                    if G.node[neighbor[c]]['check']==-1:
                        G.node[neighbor[c]]['check']=e
                        node_list.append(neighbor[c])
        e+=1
    component.append(G.subgraph(node_list))
if len(component)==1:
    print('This graph is connected.')
else:
    print('This graph is disconnected.','\n',' It can be divided into ',len(component),'disconnected components.')
    for a in range(len(component)):
        print(component[a].nodes())
    
