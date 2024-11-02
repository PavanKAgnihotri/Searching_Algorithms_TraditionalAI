import numpy as np

# Set of nodes
all_nodes = ['S', 'A', 'B', 'C', 'D', 'E', 'G']

# Start state
start_state = 'S'

# Goal state
goal_state = 'G'

# Number of nodes
N = len(all_nodes)

# Adjacency matrix
adj = np.zeros((N, N))

def add_edge(node_1, node_2):
	adj[all_nodes.index(node_1), all_nodes.index(node_2)] = 1

# Construct the graph
add_edge('S', 'A')
add_edge('S', 'D')
add_edge('D', 'B')
add_edge('D', 'E')
add_edge('A', 'B')
add_edge('A', 'C')
add_edge('B', 'C')
add_edge('B', 'E')
add_edge('C', 'G')
add_edge('E', 'G')

print('Adjacency matrix:')
print(adj)

heuristic = {'S':7,'A':9,'B':4,'C':2,'D':5,'E':3,'G':0}
visited = np.zeros((N))

parent = np.zeros((N))
parent[:] = -1

#u = start
    
def greedy(u):
    visited[all_nodes.index(u)] = 1
    neighbors = []
    while u != goal_state:
        idx = all_nodes.index(u)
        for i in range(N):
            if adj[idx,i] ==1 and visited[i] ==0:
                neighbors.append(i)
        
        if not neighbors:
            print('No path')
            return None
        next = min(neighbors,key=lambda x:heuristic[all_nodes[x]])
        visited[next] = 1
        parent[next] = idx
        u = all_nodes[next]
        
    print('Goal found:', u)
    path = []
    i = all_nodes.index(u)
    while i != -1:
        path.append(i)
        i = int(parent[i])
    path.reverse()
    path = [all_nodes[element] for element in path]
    print('Path:', path)

greedy(start_state)                