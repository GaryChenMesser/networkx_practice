#find out if a graph is bipartite or not
#the input graph must be connected

import networkx as nx

#function
def bfs_check():
    for b in G.nodes():
        if(G.node[b]['part']==-1):
            return 1
    return 0

G=nx.Graph()

#G.add_edges_from([('a','b'),('a',7),('b',2),('b',7),(2,3),(2,5),(2,8),(3,4),(3,5),(4,5),(5,6),(6,7),(6,8),(7,8)])
G.add_edges_from([(0,1),(2,3),(1,3),(2,4),(2,5),(3,6)])

#set every node attribute 'part' to -1
for a in G.nodes():
    G.node[a]['part']=-1
    G.node[a]['check']=-1

bipart=0
now=True
step=0
G.node[0]['check']=step
G.node[0]['part']=now
step+=1
now=not now

while bfs_check():
    for a in G.nodes():
        if G.node[a]['check']==step-1:
            print('a=',a)
            G.node[a]['check']=-1
            for b in G.neighbors(a):
                if G.node[b]['part']==-1:
                    G.node[b]['part']=now
                    G.node[b]['check']=step

                else:
                    if G.node[b]['part']!=now:
                        print('This graph is not bipartite.')
                        bipart=1
                        break
            else:
                continue
            break
    step+=1
    now=not now
    if bipart ==1:
        break
if bipart==0:
    print('This graph is bipartite.')


        
    
    
