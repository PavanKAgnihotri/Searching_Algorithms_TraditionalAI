#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 18:04:55 2024

@author: pavan
"""

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

def add_edge(node_1, node_2, cost):
	adj[all_nodes.index(node_1), all_nodes.index(node_2)] = cost

# Construct the graph
add_edge('S', 'A', 3)
add_edge('S', 'D', 2)
add_edge('D', 'B', 1)
add_edge('D', 'E', 4)
add_edge('A', 'B', 5)
add_edge('A', 'C', 10)
add_edge('B', 'C', 2)
add_edge('B', 'E', 1)
add_edge('C', 'G', 4)
add_edge('E', 'G', 3)

print('Adjacency matrix:')
print(adj)

heuristic = {'S':7,'A':9,'B':4,'C':2,'D':5,'E':3,'G':0}

# Status of each node
visited = np.zeros((N))

# Parent
parent = np.zeros((N))
parent[:] = -1

def A_star_graph(start):
    nodes = {start}
    came_from = {}
    
    g = {n: float('inf') for n in all_nodes}
    g[start] = 0
    
    f = {n: float('inf') for n in all_nodes}
    f[start] = heuristic[start]
    
    while nodes:
        cur = min(nodes, key=lambda n: f[n])
        
        # Remove the current node from the open set
        nodes.remove(cur)
        
        if cur == goal_state:
            path = []
            while cur in came_from:
                path.append(cur)
                cur = came_from[cur]
            path.append(start)
            path.reverse()
            print('Path:', path)
            print('Cost:', int(g[goal_state]))
            return
        
        cur_idx = all_nodes.index(cur)
        for neighbor_idx in range(N):
            if adj[cur_idx, neighbor_idx] > 0:  
                neighbor = all_nodes[neighbor_idx]
                cumulative_g = g[cur] + adj[cur_idx, neighbor_idx]
                
                if cumulative_g < g[neighbor]:
                    came_from[neighbor] = cur
                    g[neighbor] = cumulative_g
                    f[neighbor] = g[neighbor] + heuristic[neighbor]
                    nodes.add(neighbor)
    
    #return None, float('inf')
    print('No path found')
    
A_star_graph(start_state)