#implementation of some properties of a graph
import networkx as nx
import numpy.matlib as np
G=nx.Graph()

#enter the graph
#the graph must be connected
#for example
G.add_nodes_from([0,1,2,3,4,5,6,7,8])
G.add_edges_from([(0,1),(0,7),(1,2),(1,7),(2,3),(2,5),(2,8),(3,4),(3,5),(4,5),(5,6),(6,7),(6,8),(7,8)])

#set every node attribute 'check' to -1
for a in range(G.number_of_nodes()):
    G.node[a]['check']=-1

#function
'''
def bfs(n,d):
    neighbor=G.neighbors(n)
    for e in range((len(neighbor))):
        if(G.node[neighbor[e]]['check']==0):
            G.node[neighbor[e]]['check']=d
    for e in range((len(neighbor))):
        if(G.node[neighbor[e]]['check']==d):
            bfs(n
'''
def bfs_check():
    a=0;
    for b in range(G.number_of_nodes()):
        if(G.node[b]['check']!=-1):
            a=a+1;
    if(a==G.number_of_nodes()):
        return 0
    else:
        return 1

def check_1():
    c=0
    for a in range(G.number_of_nodes()):
        for b in range(G.number_of_nodes()):
            if((a!=b)and(mul_matrix.getA()[a][b]==0)):
                return 1
                c=1;
                break
        if(c==1):
            break
    if(c==0):
        return 0

#initialize a zero matrix called matrix
'''    
matrix=[]
for a in range(G.number_of_nodes()):
	matrix.append([])
	for b in range(G.number_of_nodes()):
		matrix[a].append(0)
'''
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
#----------------------------------d_(a,b)----------------------------------
#shortest path between a,b : d_(a,b)......(1)
#using matrix multiplication
mul=np.identity(G.number_of_nodes())
mul_matrix=matrix.copy()
#buffer=ad_matrix
count=0
while(check_1()):
    mul=(mul)*(ad_matrix)
    count=count+1
    for a in range(G.number_of_nodes()):
        for b in range(G.number_of_nodes()):
            if((a!=b)and((mul.getA()[a][b])!=0)and(mul_matrix.getA()[a][b]==0)):
                mul_matrix.getA()[a][b]=count
    
print('shortest path matrix using matrix multiplication:','\n',mul_matrix)
'''buffer=ad_matrix
for a in range(G.number_of_nodes()):
    for b in range(G.number_of_nodes()):
        while(buffer[a][b]==0):
            buffer*=buffer
        d_(a,b)[a][b]=buffer[a][b]
        buffer=matrix
'''
#shortest path between a,b : d_(a,b)......(2)
#using BFS
bfs_matrix=matrix.copy()
for a in range(G.number_of_nodes()):
    G.node[a]['check']=0
    e=0
    while(bfs_check()):
        for f in range(G.number_of_nodes()):
            if(G.node[f]['check']==e):
                neighbor=G.neighbors(f)
                for g in range((len(neighbor))):
                    if(G.node[neighbor[g]]['check']==-1):
                        G.node[neighbor[g]]['check']=e+1
        e=e+1
    for b in range(G.number_of_nodes()):
        if(a!=b):
            bfs_matrix.getA()[a][b]=G.node[b]['check']
    for c in range(G.number_of_nodes()):
        G.node[c]['check']=-1
print ('shortest path matrix using bfs:','\n',bfs_matrix)
        
#number of shortest paths between a,b : N_(a,b)
number_matrix=mul.copy()
print('number of shortest paths matrix:','\n',number_matrix)

#diameter : d_max
d_max=count
print('diameter:',d_max)
#average path length : <d>
#d=sum(sum(bfs_matrix.getA()*number_matrix.getA()))/(sum(sum(number_matrix.getA()))-diagonal)
ds=sum(sum(bfs_matrix.getA()))/(G.number_of_nodes()*G.number_of_nodes())
print('average path length:',ds)

